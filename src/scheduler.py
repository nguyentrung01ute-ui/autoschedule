import os
from datetime import datetime
from zoneinfo import ZoneInfo
import boto3

TZ = ZoneInfo(os.environ.get("TZ_NAME", "Asia/Ho_Chi_Minh"))
TOPIC_ARN = os.environ["TOPIC_ARN"]
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

ec2 = boto3.client("ec2")
rds = boto3.client("rds")
sm = boto3.client("sagemaker")
sns = boto3.client("sns")


def parse_days(text):
    parts = [p.strip() for p in text.split("-")]
    if len(parts) == 1:
        a = b = DAYS.index(parts[0])
    else:
        a, b = DAYS.index(parts[0]), DAYS.index(parts[1])
    return a, b


def desired_running(tags, now):
    """True = nên chạy, False = nên tắt, None = không quản lý."""
    sched = tags.get("Schedule")
    if not sched:
        return None
    if sched.strip().lower() == "off":
        return False
    try:
        start, end = [x.strip() for x in sched.split("-")]
        a, b = parse_days(tags.get("ScheduleDays", "Mon-Sun"))
    except ValueError:
        print(f"Tag không hợp lệ: {tags}")
        return None

    wd = now.weekday()
    day_ok = (a <= wd <= b) if a <= b else (wd >= a or wd <= b)
    t = now.strftime("%H:%M")
    if start < end:                       # khung giờ trong ngày
        in_window = start <= t < end
    else:                                 # khung giờ qua đêm, ví dụ 22:00-06:00
        in_window = t >= start or t < end
    return day_ok and in_window


# ---------- Thu thập tài nguyên: mỗi loại trả về dict chuẩn ----------
def list_ec2():
    out = []
    pages = ec2.get_paginator("describe_instances").paginate(
        Filters=[{"Name": "tag-key", "Values": ["Schedule"]},
                 {"Name": "instance-state-name", "Values": ["running", "stopped"]}])
    for p in pages:
        for r in p["Reservations"]:
            for i in r["Instances"]:
                tags = {t["Key"]: t["Value"] for t in i.get("Tags", [])}
                out.append(dict(type="EC2", id=i["InstanceId"], tags=tags,
                                running=i["State"]["Name"] == "running",
                                start=lambda i=i: ec2.start_instances(InstanceIds=[i["InstanceId"]]),
                                stop=lambda i=i: ec2.stop_instances(InstanceIds=[i["InstanceId"]])))
    return out


def list_rds():
    out = []
    for db in rds.describe_db_instances()["DBInstances"]:
        if db["DBInstanceStatus"] not in ("available", "stopped"):
            continue
        tl = rds.list_tags_for_resource(ResourceName=db["DBInstanceArn"])["TagList"]
        tags = {t["Key"]: t["Value"] for t in tl}
        ident = db["DBInstanceIdentifier"]
        out.append(dict(type="RDS", id=ident, tags=tags,
                        running=db["DBInstanceStatus"] == "available",
                        start=lambda ident=ident: rds.start_db_instance(DBInstanceIdentifier=ident),
                        stop=lambda ident=ident: rds.stop_db_instance(DBInstanceIdentifier=ident)))
    return out


def list_sagemaker():
    out = []
    for nb in sm.list_notebook_instances()["NotebookInstances"]:
        if nb["NotebookInstanceStatus"] not in ("InService", "Stopped"):
            continue
        tl = sm.list_tags(ResourceArn=nb["NotebookInstanceArn"])["Tags"]
        tags = {t["Key"]: t["Value"] for t in tl}
        name = nb["NotebookInstanceName"]
        out.append(dict(type="SageMaker", id=name, tags=tags,
                        running=nb["NotebookInstanceStatus"] == "InService",
                        start=lambda name=name: sm.start_notebook_instance(NotebookInstanceName=name),
                        stop=lambda name=name: sm.stop_notebook_instance(NotebookInstanceName=name)))
    return out


def collect():
    res = []
    for fn in (list_ec2, list_rds, list_sagemaker):
        try:
            res += fn()
        except Exception as e:  # một dịch vụ lỗi không làm hỏng các dịch vụ khác
            print(f"Lỗi {fn.__name__}: {e}")
    return res


# ---------- Hành động ----------
def enforce(now):
    actions = []
    for r in collect():
        want = desired_running(r["tags"], now)
        if want is None or want == r["running"]:
            continue
        try:
            (r["start"] if want else r["stop"])()
            actions.append(f'{"START" if want else "STOP"} {r["type"]} {r["id"]}')
        except Exception as e:
            actions.append(f'LỖI {r["type"]} {r["id"]}: {e}')
    print("Actions:", actions)
    return actions


def report(now):
    running = [r for r in collect() if r["running"]]
    lines = [f'- {r["type"]:<10} {r["id"]}  (Schedule={r["tags"].get("Schedule")})' for r in running]
    body = (f"Báo cáo tài nguyên đang chạy lúc {now:%Y-%m-%d %H:%M} ({TZ.key})\n"
            f"Tổng: {len(running)}\n\n" + ("\n".join(lines) or "Không có tài nguyên nào đang chạy."))
    sns.publish(TopicArn=TOPIC_ARN, Subject="[AutoSchedule] Tài nguyên đang chạy", Message=body)
    return body


def lambda_handler(event, context):
    now = datetime.now(TZ)
    if event.get("action") == "report":
        return {"report": report(now)}
    return {"actions": enforce(now)}
