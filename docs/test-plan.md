# Test Plan

## Unit test
    python -m pytest -q

Kiểm tra: không có Schedule, Project khác, off, trong/ngoài khung giờ, biên bắt đầu/kết thúc, cuối tuần, tag sai, giờ bằng nhau và lịch qua đêm.

## AWS integration test

| ID | Tài nguyên | Thao tác | Kết quả mong đợi |
|---|---|---|---|
| INT-01 | EC2 | Schedule ngoài giờ | EC2 stopped |
| INT-02 | EC2 | Schedule trong giờ | EC2 running |
| INT-03 | RDS | Ngoài giờ | RDS stopped |
| INT-04 | RDS | Trong giờ | RDS available |
| INT-05 | SageMaker | Ngoài giờ | Notebook Stopped |
| INT-06 | SageMaker | Trong giờ | Notebook InService |
| INT-07 | Không có Schedule | Không đổi tag | Không bị tác động |
| INT-08 | Schedule sai | Gọi Lambda | Log cảnh báo, không start/stop |
| INT-09 | Report event | action=report | Email SNS |
| INT-10 | EventBridge | Chờ chu kỳ | Lambda được invoke |

Không ghi PASS nếu chưa có log/ảnh/trạng thái thực tế.
