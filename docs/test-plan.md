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
| INT-11 | EventBridge (report) | Lịch report đến giờ | Nhận email báo cáo tự động |
| INT-12 | CloudFormation | Deploy stack lần 1 bằng `scripts/07_deploy.sh` | Stack `CREATE_COMPLETE` |
| INT-13 | CloudFormation | Xóa stack (`delete-stack`) rồi deploy lại | Stack `CREATE_COMPLETE` lần 2 |
| INT-14 | CloudWatch | Gây lỗi Lambda (`TOPIC_ARN` sai) | Alarm `ALARM`, có email, sau đó về `OK` |
| INT-17 | Lambda | Tag `Schedule` sai (`abc`) | Log `Invalid schedule tag`, `Actions: []` |
| INT-18 | Lambda | Gọi enforce khi tài nguyên đang chuyển trạng thái | Bỏ qua, không start lần hai |
| INT-19 | CloudWatch | Gây lỗi Lambda (`TOPIC_ARN` sai) | Alarm `ALARM`, có email, sau đó về `OK` |

## Kết quả thực tế

| ID | Kết quả | Minh chứng |
|---|:---:|---|
| INT-11 | ☑ Đạt | [Tuần 3, Hình 10–11](week3-evidence.md) |
| INT-12 | ☑ Đạt | [Tuần 3, Hình 13–18](week3-evidence.md) |
| INT-13 | ☑ Đạt | [Tuần 3](week3-evidence.md) (deploy lại bằng `07_deploy.sh`) |
| INT-14 | ☑ Đạt | [Tuần 3, Hình 31–35](week3-evidence.md) |
| INT-17 | ☑ Đạt | [Tuần 4, Hình 10](week4-evidence.md) |
| INT-18 | ☑ Đạt | [Tuần 4, Hình 11](week4-evidence.md) |
| INT-19 | ☑ Đạt | [Tuần 4, Hình 12–14](week4-evidence.md) |

INT-15, INT-16a, INT-16b (dựng lại bằng một lệnh, end-to-end lịch ngắn) do Nguyễn Văn Trung bổ sung.

Không ghi PASS nếu chưa có log/ảnh/trạng thái thực tế.
