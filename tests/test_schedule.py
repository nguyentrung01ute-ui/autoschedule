import os, sys
from datetime import datetime
from zoneinfo import ZoneInfo

os.environ["TOPIC_ARN"] = "arn:aws:sns:us-east-1:000000000000:test"
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from scheduler import desired_running  # noqa: E402

TZ = ZoneInfo("Asia/Ho_Chi_Minh")


def at(y, m, d, hh, mm):
    return datetime(y, m, d, hh, mm, tzinfo=TZ)

# 2026-10-05 là thứ Hai, 2026-10-10 là thứ Bảy
WORK = {"Schedule": "08:00-17:00", "ScheduleDays": "Mon-Fri"}


def test_no_tag_is_ignored():
    assert desired_running({}, at(2026, 10, 5, 9, 0)) is None

def test_off_always_stopped():
    assert desired_running({"Schedule": "off"}, at(2026, 10, 5, 9, 0)) is False

def test_inside_window():
    assert desired_running(WORK, at(2026, 10, 5, 9, 0)) is True

def test_before_window():
    assert desired_running(WORK, at(2026, 10, 5, 7, 59)) is False

def test_start_boundary_inclusive():
    assert desired_running(WORK, at(2026, 10, 5, 8, 0)) is True

def test_end_boundary_exclusive():
    assert desired_running(WORK, at(2026, 10, 5, 17, 0)) is False

def test_weekend_stopped():
    assert desired_running(WORK, at(2026, 10, 10, 9, 0)) is False

def test_invalid_tag_ignored():
    assert desired_running({"Schedule": "abc"}, at(2026, 10, 5, 9, 0)) is None

def test_overnight_window():
    tags = {"Schedule": "22:00-06:00"}
    assert desired_running(tags, at(2026, 10, 5, 23, 0)) is True
    assert desired_running(tags, at(2026, 10, 5, 3, 0)) is True
    assert desired_running(tags, at(2026, 10, 5, 12, 0)) is False
