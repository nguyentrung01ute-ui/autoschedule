"""Unit tests kiểm thử logic tính toán lịch bật/tắt tài nguyên (desired_running).

Tác giả: Nguyễn Văn Thi - 24110334 (Nhóm DevOps & IaC)
Tuần 2: Triển khai kiểm thử đơn vị với pytest (11 test cases).
Bao gồm:
- Không có tag Schedule, tag rỗng, hoặc Project khác AutoSchedule
- Tag Schedule=off (luôn tắt bất kể thời gian)
- Trong và ngoài khung giờ hoạt động
- Biên bắt đầu (bao gồm) và biên kết thúc (không bao gồm)
- Cuối tuần (bị tắt khi lịch là Mon-Fri)
- Tag sai định dạng hoặc giờ bắt đầu bằng giờ kết thúc (bỏ qua, log cảnh báo)
- Lịch chạy qua đêm (22:00-06:00 kéo dài sang sáng hôm sau)
"""

import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

os.environ["TOPIC_ARN"] = "arn:aws:sns:us-east-1:000000000000:test"
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
os.environ["PROJECT_TAG"] = "AutoSchedule"
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from scheduler import desired_running  # noqa: E402

TZ = ZoneInfo("Asia/Ho_Chi_Minh")


def at(y, m, d, hh, mm):
    return datetime(y, m, d, hh, mm, tzinfo=TZ)


WORK = {"Project": "AutoSchedule", "Schedule": "08:00-17:00", "ScheduleDays": "Mon-Fri"}


def test_no_schedule_is_ignored():
    """Tài nguyên không có tag Schedule hoặc tag rỗng thì bỏ qua (trả về None)."""
    assert desired_running(WORK | {"Schedule": ""}, at(2026, 10, 5, 9, 0)) is None


def test_wrong_project_is_ignored():
    """Tài nguyên thuộc Project khác AutoSchedule thì bỏ qua (trả về None)."""
    assert desired_running(WORK | {"Project": "OtherProject"}, at(2026, 10, 5, 9, 0)) is None


def test_off_always_stopped():
    """Tag Schedule=off thì luôn ở trạng thái tắt (trả về False) bất kể giờ nào."""
    assert desired_running(WORK | {"Schedule": "off"}, at(2026, 10, 5, 9, 0)) is False


def test_inside_window():
    """Trong khung giờ hoạt động hợp lệ thì trả về True (được phép chạy)."""
    assert desired_running(WORK, at(2026, 10, 5, 9, 0)) is True


def test_before_window():
    """Trước khung giờ hoạt động thì trả về False (phải tắt)."""
    assert desired_running(WORK, at(2026, 10, 5, 7, 59)) is False


def test_start_boundary_inclusive():
    """Biên bắt đầu (08:00) bao gồm trong khung giờ, trả về True."""
    assert desired_running(WORK, at(2026, 10, 5, 8, 0)) is True


def test_end_boundary_exclusive():
    """Biên kết thúc (17:00) không bao gồm trong khung giờ, trả về False."""
    assert desired_running(WORK, at(2026, 10, 5, 17, 0)) is False


def test_weekend_stopped():
    """Ngày cuối tuần (thứ 7, CN) ngoài lịch Mon-Fri thì trả về False."""
    assert desired_running(WORK, at(2026, 10, 10, 9, 0)) is False


def test_invalid_tag_ignored():
    """Tag Schedule sai định dạng (ví dụ 'abc') thì bỏ qua (trả về None) và ghi log cảnh báo."""
    assert desired_running(WORK | {"Schedule": "abc"}, at(2026, 10, 5, 9, 0)) is None


def test_equal_times_are_rejected():
    """Giờ bắt đầu bằng giờ kết thúc (ví dụ 08:00-08:00) không hợp lệ, trả về None."""
    assert desired_running(WORK | {"Schedule": "08:00-08:00"}, at(2026, 10, 5, 9, 0)) is None


def test_overnight_window_continues_into_next_day():
    """Lịch chạy qua đêm (22:00-06:00) tính thêm buổi sáng hôm sau cho đến trước 06:00."""
    tags = {"Project": "AutoSchedule", "Schedule": "22:00-06:00", "ScheduleDays": "Mon-Fri"}
    assert desired_running(tags, at(2026, 10, 5, 23, 0)) is True
    assert desired_running(tags, at(2026, 10, 6, 3, 0)) is True
    assert desired_running(tags, at(2026, 10, 10, 3, 0)) is True
    assert desired_running(tags, at(2026, 10, 10, 6, 0)) is False

