# Lộ trình hoàn chỉnh AutoSchedule

> Giả định tuần 1 bắt đầu 06/10/2026. Nếu nhóm bắt đầu ngày khác, dời các mốc tương ứng.
> Đặt file này tại `docs/ROADMAP.md` trong repo.

## 1. Hiện trạng repo (đối chiếu với kế hoạch)

| Hạng mục | File | Trạng thái |
|---|---|---|
| Mô tả và kế hoạch | `PROJECT_PLAN.md`, `README.md` | Xong |
| Mã Lambda | `src/scheduler.py` | Xong bản nháp, chưa chạy trên AWS |
| Unit test | `tests/test_schedule.py` | Xong, 9 test đạt trên máy cục bộ |
| CloudFormation | `infra/template.yaml` | Xong bản nháp, chưa deploy |
| Script tuần 1 | `scripts/*.sh` | Xong, chưa chạy trên AWS |
| Sơ đồ, checklist tuần 1 | `docs/architecture.md`, `docs/week1-checklist.md` | Xong |
| Worklog | `worklog/week1..4.md` | Mẫu trống |
| Minh chứng | `docs/screenshots/` | Trống |
| Báo cáo, kịch bản demo, phân tích chi phí | | Chưa có |

## 2. Việc còn thiếu trong repo (bổ sung theo tuần)

| Tuần | File cần thêm | Mục đích |
|---|---|---|
| 2 | `scripts/06_set_schedule.sh` | Đổi nhanh tag Schedule để test bật/tắt |
| 2 | `tests/events/enforce.json`, `report.json` | Test event cho Lambda |
| 3 | `scripts/07_deploy.sh` | Đóng gói zip, upload S3, deploy stack bằng một lệnh |
| 3 | Dashboard trong `infra/template.yaml` | CloudWatch Dashboard |
| 4 | `docs/test-results.md` | Bảng kết quả kiểm thử end-to-end |
| 4 | `docs/cost-analysis.md` | Tính chi phí và mức tiết kiệm |
| 4 | `docs/report.md` | Báo cáo cuối kỳ |
| 4 | `docs/demo-script.md` | Kịch bản video demo |

## 3. Lịch chi tiết

### Tuần 1 (06/10 - 12/10): Nền tảng

| ID | Việc | SV | Giờ | Minh chứng | Xong khi |
|---|---|---|---|---|---|
| 1.1 | Sửa `OWNER` trong `scripts/config.sh`, chạy `01_setup_s3.sh` | A | 1 | Ảnh bucket (tag, Block Public Access) | Bucket có tag, mã hóa, chặn public |
| 1.2 | Chạy `02_create_ec2.sh` | A | 1.5 | Ảnh EC2 có cột tag | Instance running |
| 1.3 | Chạy `03_create_rds.sh` | B | 2 | Ảnh RDS `available` | Có tag Schedule |
| 1.4 | Chạy `04_create_sagemaker.sh` | B | 1.5 | Ảnh Notebook `InService` | Có tag Schedule |
| 1.5 | Chụp ảnh `05_status.sh` và sơ đồ `docs/architecture.md` | B | 1 | Ảnh CLI có Account ID, Region, thời gian | |
| 1.6 | Đọc tài liệu EventBridge, boto3, giới hạn lab | A+B | 4 | Ghi chú trong worklog | |
| 1.7 | Điền `worklog/week1.md`, dừng tài nguyên cuối buổi | A+B | 1 | | Mỗi SV ≥ 8 giờ |

### Tuần 2 (13/10 - 19/10): Chức năng lõi

| ID | Việc | SV | Giờ | Minh chứng |
|---|---|---|---|---|
| 2.1 | Chạy `pytest`, đọc và giải thích `desired_running()` | A | 2 | Ảnh pytest 9 passed |
| 2.2 | Tạo SNS topic, xác nhận email | B | 1 | Ảnh subscription Confirmed |
| 2.3 | Tạo Lambda thủ công (LabRole, Python 3.12, timeout 120s, biến môi trường) | B | 2 | Ảnh cấu hình Lambda |
| 2.4 | Test EC2 bật/tắt qua đổi tag | A | 3 | Log `START/STOP EC2` |
| 2.5 | Test RDS và SageMaker bật/tắt | B | 3 | Log `START/STOP RDS/SageMaker` |
| 2.6 | Test: không tag, `off`, tag sai, đang `starting` | A+B | 2 | Bảng kết quả |
| 2.7 | Test báo cáo `{"action":"report"}` | B | 1 | Ảnh email SNS |
| 2.8 | Worklog, cập nhật Git | A+B | 1 | |

### Tuần 3 (20/10 - 26/10): Tích hợp, bảo mật, giám sát, IaC

| ID | Việc | SV | Giờ | Minh chứng |
|---|---|---|---|---|
| 3.1 | Tạo 2 EventBridge rule thủ công, quan sát kích hoạt | B | 2 | Ảnh rule, log tự kích hoạt |
| 3.2 | Xóa tài nguyên thủ công trước khi deploy IaC | A | 0.5 | |
| 3.3 | Viết `scripts/07_deploy.sh`, deploy stack | A | 3 | Ảnh stack `CREATE_COMPLETE` |
| 3.4 | Xóa stack rồi tạo lại | A+B | 1 | Ảnh lần 2 thành công |
| 3.5 | Rà soát bảo mật theo `PROJECT_PLAN.md` mục 6 | B | 1.5 | Danh sách kiểm |
| 3.6 | CloudWatch Dashboard và thử gây lỗi cho Alarm | B | 2 | Ảnh Alarm OK và ALARM |
| 3.7 | Worklog, commit | A+B | 1 | |

### Tuần 4 (27/10 - 02/11): Kiểm thử tổng thể, tối ưu, dọn dẹp, báo cáo, demo

| ID | Việc | SV | Giờ | Minh chứng |
|---|---|---|---|---|
| 4.1 | Dựng lại từ đầu bằng một lệnh | A | 1 | Ảnh deploy |
| 4.2 | Test end-to-end với lịch ngắn (bật 10 phút) cho cả 3 loại | A+B | 2 | `docs/test-results.md` |
| 4.3 | Test lỗi và Alarm gửi email | B | 1 | Ảnh email cảnh báo |
| 4.4 | Tính chi phí và mức tiết kiệm | B | 2 | `docs/cost-analysis.md` |
| 4.5 | Viết báo cáo | A+B | 3 | `docs/report.md` |
| 4.6 | Quay video demo ≤ 10 phút | A+B | 1.5 | Video |
| 4.7 | Dọn dẹp bằng `scripts/99_cleanup.sh --bucket` | A | 1 | Ảnh console trống |
| 4.8 | Ôn vấn đáp, worklog cuối | A+B | 1.5 | |

## 4. Mốc kiểm soát

| Mốc | Ngày | Điều kiện |
|---|---|---|
| M1 | 12/10 | 3 tài nguyên có tag, sơ đồ xong |
| M2 | 19/10 | Lambda bật/tắt đúng cho cả 3 loại bằng tay |
| M3 | 26/10 | Stack tự chạy theo lịch, có email báo cáo |
| M4 | 02/11 | Báo cáo, video, Git, worklog đủ; tài nguyên đã dọn |

## 5. Rủi ro cần theo dõi

| Rủi ro | Cách xử lý |
|---|---|
| Hết ngân sách lab | Dọn tài nguyên cuối mỗi buổi, theo dõi số dư lab |
| Lab session hết hạn làm ngừng EventBridge | Kiểm tra lại sau mỗi lần Start Lab |
| Script mất quyền thực thi khi tải từ web | Chạy `chmod +x scripts/*.sh` |
| `AccessDenied` ở một API của LabRole | Ghi lỗi, xử lý bằng `try/except`, nêu trong báo cáo |
| RDS tự bật lại sau 7 ngày | Lambda tắt lại ở chu kỳ kế tiếp |
| Khung qua đêm bị lệch ngày | Ghi vào mục Hạn chế |

## 6. Tiêu chí hoàn thành

- [ ] Lambda xử lý đúng EC2, RDS, SageMaker
- [ ] EventBridge tự chạy; email báo cáo hằng ngày
- [ ] Stack dựng lại từ đầu bằng một lệnh
- [ ] Alarm lỗi Lambda hoạt động
- [ ] Mọi tài nguyên có tag Project/Owner
- [ ] Có bảng kiểm thử, phân tích chi phí, báo cáo, video demo
- [ ] Worklog đủ 4 tuần, mỗi SV ≥ 8 giờ/tuần
- [ ] Đã dọn dẹp tài nguyên
