import os
from datetime import datetime, time
from zoneinfo import ZoneInfo

import boto3

TZ_NAME = os.environ.get("TZ_NAME", "Asia/Ho_Chi_Minh")
TZ = ZoneInfo(TZ_NAME)
TOPIC_ARN = os.environ.get("TOPIC_ARN", "")
PROJECT_TAG = os.environ.get("PROJECT_TAG", "AutoSchedule")
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

ec2 = boto3.client("ec2")
rds = boto3.client("rds")
sm = boto3.client("sagemaker")
sns = boto3.client("sns")


def parse_clock(value):
    try:
        hour, minute = (int(x) for x in value.split(":"))
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            raise ValueError
        return time(hour, minute)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid time: {value}")


def parse_days(text):
    parts = [p.strip().title()[:3] for p in text.split("-")]
    if len(parts) not in (1, 2) or any(p not in DAYS for p in parts):
        raise ValueError(f"Invalid ScheduleDays: {text}")
    return DAYS.index(parts[0]), DAYS.index(parts[-1])


def day_in_range(day, start_day, end_day):
    return start_day <= day <= end_day if start_day <= end_day else day >= start_day or day <= end_day


def desired_running(tags, now):
    """True=start, False=stop, None=not managed."""
    if tags.get("Project") != PROJECT_TAG:
        return None

    sched = tags.get("Schedule", "").strip()
    if not sched:
        return None
    if sched.lower() == "off":
        return False

    try:
        start_text, end_text = [x.strip() for x in sched.split("-")]
        start = parse_clock(start_text)
        end = parse_clock(end_text)
        start_day, end_day = parse_days(tags.get("ScheduleDays", "Mon-Sun"))
    except ValueError as exc:
        print(f"Invalid schedule tag: {tags}; {exc}")
        return None

    if start == end:
        print(f"Invalid schedule tag: equal start/end is ambiguous: {tags}")
        return None

    current_time = now.timetz().replace(tzinfo=None)
    weekday = now.weekday()

    if start < end:
        return day_in_range(weekday, start_day, end_day) and start <= current_time < end

    previous_day = (weekday - 1) % 7
    evening_part = day_in_range(weekday, start_day, end_day) and current_time >= start
    morning_part = day_in_range(previous_day, start_day, end_day) and current_time < end
    return evening_part or morning_part


def _tags(items):
    return {item["Key"]: item["Value"] for item in items}


def list_ec2():
    out = []
    pages = ec2.get_paginator("describe_instances").paginate(
        Filters=[
            {"Name": "tag:Project", "Values": [PROJECT_TAG]},
            {"Name": "tag-key", "Values": ["Schedule"]},
            {"Name": "instance-state-name", "Values": ["running", "stopped"]},
        ]
    )
    for page in pages:
        for reservation in page["Reservations"]:
            for instance in reservation["Instances"]:
                tags = _tags(instance.get("Tags", []))
                iid = instance["InstanceId"]
                out.append({
                    "type": "EC2",
                    "id": iid,
                    "tags": tags,
                    "running": instance["State"]["Name"] == "running",
                    "start": lambda iid=iid: ec2.start_instances(InstanceIds=[iid]),
                    "stop": lambda iid=iid: ec2.stop_instances(InstanceIds=[iid]),
                })
    return out


def list_rds():
    out = []
    for page in rds.get_paginator("describe_db_instances").paginate():
        for db in page["DBInstances"]:
            if db["DBInstanceStatus"] not in ("available", "stopped"):
                continue
            tags = _tags(rds.list_tags_for_resource(ResourceName=db["DBInstanceArn"])["TagList"])
            if tags.get("Project") != PROJECT_TAG or "Schedule" not in tags:
                continue
            ident = db["DBInstanceIdentifier"]
            out.append({
                "type": "RDS",
                "id": ident,
                "tags": tags,
                "running": db["DBInstanceStatus"] == "available",
                "start": lambda ident=ident: rds.start_db_instance(DBInstanceIdentifier=ident),
                "stop": lambda ident=ident: rds.stop_db_instance(DBInstanceIdentifier=ident),
            })
    return out


def list_sagemaker():
    out = []
    for page in sm.get_paginator("list_notebook_instances").paginate():
        for nb in page["NotebookInstances"]:
            if nb["NotebookInstanceStatus"] not in ("InService", "Stopped"):
                continue
            tags = _tags(sm.list_tags(ResourceArn=nb["NotebookInstanceArn"])["Tags"])
            if tags.get("Project") != PROJECT_TAG or "Schedule" not in tags:
                continue
            name = nb["NotebookInstanceName"]
            out.append({
                "type": "SageMaker",
                "id": name,
                "tags": tags,
                "running": nb["NotebookInstanceStatus"] == "InService",
                "start": lambda name=name: sm.start_notebook_instance(NotebookInstanceName=name),
                "stop": lambda name=name: sm.stop_notebook_instance(NotebookInstanceName=name),
            })
    return out


def collect():
    resources = []
    for fn in (list_ec2, list_rds, list_sagemaker):
        try:
            resources.extend(fn())
        except Exception as exc:
            print(f"ERROR {fn.__name__}: {exc}")
    return resources


def enforce(now):
    actions = []
    for resource in collect():
        desired = desired_running(resource["tags"], now)
        if desired is None or desired == resource["running"]:
            continue
        action = "START" if desired else "STOP"
        try:
            (resource["start"] if desired else resource["stop"])()
            actions.append(f"{action} {resource['type']} {resource['id']}")
        except Exception as exc:
            actions.append(f"ERROR {resource['type']} {resource['id']}: {exc}")
    print(f"Actions: {actions}")
    return actions


def report(now):
    if not TOPIC_ARN:
        raise RuntimeError("TOPIC_ARN is required for report events")
    running = [resource for resource in collect() if resource["running"]]
    lines = [
        f"- {r['type']:<10} {r['id']} (Schedule={r['tags'].get('Schedule')})"
        for r in running
    ]
    body = (
        f"AutoSchedule report: {now:%Y-%m-%d %H:%M} ({TZ_NAME})\n"
        f"Running managed resources: {len(running)}\n\n"
        + ("\n".join(lines) or "No managed resources are running.")
    )
    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject="[AutoSchedule] Running resources",
        Message=body,
    )
    return body


def lambda_handler(event, context):
    event = event or {}
    now = datetime.now(TZ)
    if event.get("action") == "report":
        return {"report": report(now)}
    return {"actions": enforce(now)}
