# Báo cáo cuối kỳ AutoSchedule

## 1. Giới thiệu
- Tên đề tài: Tự động bật/tắt tài nguyên AWS theo giờ học để tiết kiệm ngân sách (AutoSchedule)
- Nhóm: DevOps & IaC
- GVHD: Huỳnh Xuân Phụng
- Region: `us-east-1` (US East, N. Virginia) — AWS Academy Learner Lab
- Thành viên:
  - Nguyễn Văn Trung (MSSV 24110365) — Nhóm trưởng
  - Nguyễn Văn Thi (MSSV 24110334) — Thành viên
- Repo: https://github.com/nguyentrung01ute-ui/autoschedule
- Video demo: [Google Drive](https://drive.google.com/file/d/1gMQxJKQ81sfH3KW3673XL4wAbYJkwzjC/view?usp=sharing) (9 phút 32 giây)

## 2. Bài toán và mục tiêu
Tài nguyên học tập (EC2, RDS, SageMaker Notebook) thường bị để chạy 24/7 dù chỉ dùng trong giờ học, gây lãng phí ngân sách Learner Lab ($50). AutoSchedule tự động start/stop tài nguyên dựa trên tag `Schedule` và `ScheduleDays`, chỉ tác động tới tài nguyên có `Project=AutoSchedule`, đồng thời gửi email báo cáo hằng ngày và cảnh báo khi Lambda lỗi.

## 3. Kiến trúc
Sơ đồ chi tiết: [docs/architecture.md](architecture.md) và [ảnh hạ tầng](screenshots/autoschedule-infrastructure.png).

- EventBridge `rate(15 minutes)` → Lambda `autoschedule` (Python 3.12, `LabRole`) → start/stop EC2, RDS, SageMaker qua boto3.
- EventBridge `cron(0 1 * * ? *)` (08:00 giờ VN) → Lambda `{"action":"report"}` → SNS → email.
- CloudWatch Logs (retention 7 ngày), Dashboard `autoschedule-dashboard`, Alarm `autoschedule-errors` (Errors ≥ 1) → SNS.

## 4. Thiết kế tag
| Tag | Giá trị ví dụ | Ý nghĩa |
|---|---|---|
| Project | AutoSchedule | Xác định tài nguyên thuộc project |
| Owner | sv01 | Chủ sở hữu |
| Schedule | 08:00-17:00 | Khung giờ chạy (`off` = luôn tắt) |
| ScheduleDays | Mon-Fri | Ngày chạy |

## 5. Triển khai
- **Tuần 1:** S3 (Block Public Access, SSE-S3), EC2 t3.nano, RDS MySQL db.t3.micro (private), SageMaker ml.t3.medium bằng `scripts/01`–`05`.
- **Tuần 2:** SNS topic + email, Lambda thủ công, test start/stop cả ba loại tài nguyên.
- **Tuần 3:** EventBridge tự kích hoạt; IaC bằng [infra/template.yaml](../infra/template.yaml) và [scripts/07_deploy.sh](../scripts/07_deploy.sh); Dashboard và Alarm.
- **Tuần 4:** Dựng lại bằng một lệnh, test end-to-end, test lỗi/Alarm, tính chi phí, video demo, dọn dẹp bằng `scripts/99_cleanup.sh --bucket`.

## 6. Kiểm thử
- Unit test: 11 test `pytest` passed (Tuần 2).
- Kiểm thử tích hợp: xem [docs/test-plan.md](test-plan.md). Tất cả các dòng INT-01 đến INT-19 có minh chứng đều đạt.

| Tuần | Phạm vi | Kết quả | Minh chứng |
|---|---|---|---|
| 2 | INT-01 đến INT-09 (start/stop, tag sai, `off`, không tag, report) | 11/11 đạt | [week2-evidence.md](week2-evidence.md) |
| 3 | INT-10a/b, INT-11 đến INT-14 | 6/6 đạt | [week3-evidence.md](week3-evidence.md) |
| 4 | INT-15, INT-16a/b, INT-17 đến INT-19 | 6/6 đạt | [week4-evidence.md](week4-evidence.md) |

## 7. Bảo mật
- Dùng LabRole/LabInstanceProfile theo quy định.
- Không tạo IAM user/role mới.
- Không commit mật khẩu/secret (đã quét `grep`, Tuần 3 Hình 28).
- RDS không public, bật mã hóa.
- S3 Block All Public Access, SSE-S3.
- Security Group không mở `0.0.0.0/0`.
- Tài nguyên có Project/Owner.

## 8. Chi phí
Chi tiết: [docs/cost-analysis.md](cost-analysis.md). Lịch 08:00-17:00 Mon-Fri chạy 45/168 giờ/tuần (giảm ≈ 73,2% giờ chạy).

| | 24/7 | Theo lịch | Tiết kiệm |
|---|---:|---:|---:|
| EC2 + RDS + SageMaker (theo tháng) | ≈ $96,00 | ≈ $25,64 | ≈ $70,36 (≈ 73%) |

Số liệu 24/7 lấy từ AWS Pricing Calculator; chi phí theo lịch là ước tính quy theo giờ chạy. Ngân sách Learner Lab đã dùng: $3,5 / $50.

## 9. Hạn chế
- Chu kỳ EventBridge 15 phút tạo độ trễ tối đa theo thiết kế.
- RDS tự start sau tối đa 7 ngày; RDS Stopped vẫn tính phí lưu trữ.
- Lambda chỉ xử lý tài nguyên ở trạng thái ổn định; tài nguyên đang chuyển trạng thái xử lý ở chu kỳ sau.
- Lịch qua đêm gắn với ngày bắt đầu.
- LabRole có thể giới hạn một số API.
- Session Learner Lab có thể hết hạn.

## 10. AI hỗ trợ
Nhóm dùng Claude (Anthropic) để tham khảo cấu hình, kịch bản kiểm thử, cách tính chi phí và cấu trúc tài liệu. Sinh viên tự đọc, chạy, sửa và giải thích mã/template, tự thao tác trên AWS. Chi tiết: [Tuần 2](ai-disclosure-week2.md), [Tuần 3](ai-disclosure-week3.md), [Tuần 4](ai-disclosure-week4.md).

## 11. Kết luận
Hệ thống tự động bật/tắt đúng EC2, RDS, SageMaker theo tag; EventBridge tự kích hoạt; email báo cáo hằng ngày và Alarm lỗi hoạt động; stack dựng lại được bằng một lệnh. Theo ước tính, lịch học 08:00-17:00 Mon-Fri giúp giảm khoảng 73% chi phí compute. Hướng mở rộng: hỗ trợ thêm loại tài nguyên (ECS, Auto Scaling Group), lịch theo ngày lễ, giao diện quản lý lịch.

## 12. Phụ lục
- Worklog: [Tuần 1](../worklog/week1.md), [Tuần 2](../worklog/week2.md), [Tuần 3](../worklog/week3.md), [Tuần 4](../worklog/week4.md).
- Ảnh minh chứng: [Tuần 1](week1-evidence.md), [Tuần 2](week2-evidence.md), [Tuần 3](week3-evidence.md), [Tuần 4](week4-evidence.md), [thư mục ảnh](screenshots/README.md).
- Báo cáo Word: [reports/](../reports/).
- Link GitHub: https://github.com/nguyentrung01ute-ui/autoschedule
- Video demo: [Google Drive](https://drive.google.com/file/d/1gMQxJKQ81sfH3KW3673XL4wAbYJkwzjC/view?usp=sharing).
