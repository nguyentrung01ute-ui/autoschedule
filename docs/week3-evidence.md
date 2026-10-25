# Minh chứng Tuần 3 — AutoSchedule

## Danh sách ảnh minh chứng

| Ảnh | Nội dung | Ghi chú trong báo cáo |
|---|---|---|
| [week3-evidence-01.png](screenshots/week3-evidence-01.png) | Danh sách hai lịch trong EventBridge Scheduler (trạng thái Enabled, target Lambda `autoschedule`) | Hình 1 |
| [week3-evidence-02.png](screenshots/week3-evidence-02.png) | Lịch `autoschedule-enforce-manual`: Rate-based, rate(15 minutes), múi giờ Asia/Saigon (UTC+07:00) | Hình 2 |
| [week3-evidence-03.png](screenshots/week3-evidence-03.png) | Lịch `autoschedule-report-manual`: Cron-based, cron(0 8 * * ? *), múi giờ Asia/Saigon (UTC+07:00) | Hình 3 |
| [week3-evidence-04.png](screenshots/week3-evidence-04.png) | Tag của EC2 và trạng thái Stopped trước khi lịch chạy | Hình 4 |
| [week3-evidence-05.png](screenshots/week3-evidence-05.png) | EC2 tự chuyển sang Running do lịch kích hoạt (INT-10a) | Hình 5 |
| [week3-evidence-06.png](screenshots/week3-evidence-06.png) | Log CloudWatch có `Actions: ['START EC2']`, giờ khớp với lúc EC2 bật | Hình 6 |
| [week3-evidence-07.png](screenshots/week3-evidence-07.png) | Tag đổi sang khung giờ không bao trùm giờ hiện tại, EC2 đang Running | Hình 7 |
| [week3-evidence-08.png](screenshots/week3-evidence-08.png) | EC2 tự chuyển sang Stopped và log có `Actions: ['STOP EC2']` (INT-10b) | Hình 8 |
| [week3-evidence-09.png](screenshots/week3-evidence-09.png) | Biểu đồ Invocations của Lambda (tab Monitor) cho thấy các lần chạy theo chu kỳ | Hình 9 |
| [week3-evidence-10.png](screenshots/week3-evidence-10.png) | Email "[AutoSchedule] Running resources" nhận được khi lịch report chạy (INT-11) | Hình 10 |
| [week3-evidence-11.png](screenshots/week3-evidence-11.png) | Log stream của Lambda tương ứng lần chạy report tự động | Hình 11 |
| [week3-evidence-12a.png](screenshots/week3-evidence-12a.png) | Danh sách Lambda function sau khi xóa tài nguyên thủ công | Hình 12 (phần Lambda) |
| [week3-evidence-12b.png](screenshots/week3-evidence-12b.png) | Danh sách SNS topic sau khi xóa tài nguyên thủ công | Hình 12 (phần SNS) |
| [week3-evidence-13.png](screenshots/week3-evidence-13.png) | Stack CloudFormation `autoschedule` ở trạng thái `CREATE_COMPLETE` (INT-12) | Hình 13 |
| [week3-evidence-14.png](screenshots/week3-evidence-14.png) | Tab Resources của CloudFormation stack `autoschedule` | Hình 14 |
| [week3-evidence-15.png](screenshots/week3-evidence-15.png) | Tab Events của CloudFormation stack `autoschedule` | Hình 15 |
| [week3-evidence-16.png](screenshots/week3-evidence-16.png) | Tab Outputs của CloudFormation stack `autoschedule` | Hình 16 |
| [week3-evidence-17.png](screenshots/week3-evidence-17.png) | Hai EventBridge rule do CloudFormation stack tạo | Hình 17 |
| [week3-evidence-18.png](screenshots/week3-evidence-18.png) | Email xác nhận subscription SNS topic sau khi deploy bằng CloudFormation | Hình 18 |
| [week3-evidence-21.png](screenshots/week3-evidence-21.png) | RDS `autoschedule-db`: `Publicly accessible = No`, Security Group default | Hình 21 |
| [week3-evidence-22.png](screenshots/week3-evidence-22.png) | Cấu hình RDS: Master username admin, Master password ẩn, `Encryption: Enabled` | Hình 22 |
| [week3-evidence-23.png](screenshots/week3-evidence-23.png) | Security Group default: một rule inbound với nguồn là chính security group, không mở `0.0.0.0/0` | Hình 23 |
| [week3-evidence-24.png](screenshots/week3-evidence-24.png) | S3 bucket: `Block all public access = On` (cả 4 mục) | Hình 24 |
| [week3-evidence-25.png](screenshots/week3-evidence-25.png) | S3 bucket: Default encryption `SSE-S3` | Hình 25 |
| [week3-evidence-26.png](screenshots/week3-evidence-26.png) | Lambda `autoschedule`: Memory 128 MB, Timeout 2 phút | Hình 26 |
| [week3-evidence-27.png](screenshots/week3-evidence-27.png) | Log group `/aws/lambda/autoschedule` với thời gian lưu trữ `Retention = 1 week` (7 ngày) | Hình 27 |
| [week3-evidence-28.png](screenshots/week3-evidence-28.png) | Kết quả lệnh grep kiểm tra không có mật khẩu/access key trong mã nguồn (`src`, `infra`, `scripts`) | Hình 28 |
| [week3-evidence-29.png](screenshots/week3-evidence-29.png) | Dashboard `autoschedule-dashboard` giám sát Invocations, Errors, Duration của Lambda | Hình 29 |
| [week3-evidence-30.png](screenshots/week3-evidence-30.png) | CloudWatch Alarm `autoschedule-errors` ở trạng thái `OK` trước khi thử | Hình 30 |
| [week3-evidence-31.png](screenshots/week3-evidence-31.png) | Tạm sửa biến môi trường `TOPIC_ARN` thành giá trị sai để thử nghiệm gây lỗi Alarm | Hình 31 |
| [week3-evidence-32.png](screenshots/week3-evidence-32.png) | Test event report thất bại: lỗi `InvalidClientTokenId` khi gọi `sns.publish` | Hình 32 |
| [week3-evidence-33.png](screenshots/week3-evidence-33.png) | Alarm `autoschedule-errors` chuyển sang trạng thái `In alarm` (04:20:49 UTC) (INT-14) | Hình 33 |
| [week3-evidence-34.png](screenshots/week3-evidence-34.png) | Email cảnh báo `"ALARM: autoschedule-errors in US East (N. Virginia)"` nhận được từ SNS | Hình 34 |
| [week3-evidence-35.png](screenshots/week3-evidence-35.png) | Alarm `autoschedule-errors` tự động trở về trạng thái `OK` sau 15 phút khắc phục (04:35:49 UTC) | Hình 35 |

---

## Bảng kết quả kiểm thử Tuần 3

| ID | Thành phần | Thao tác | Kết quả mong đợi | Kết quả thực tế | Kết quả |
|---|---|---|---|---|:---:|
| **INT-10a** | EventBridge | Tag trong giờ, EC2 Stopped, chờ chu kỳ | Lambda tự chạy, EC2 Running | Lambda tự chạy, EC2 chuyển sang Running (Hình 4–6) | ☑ Đạt |
| **INT-10b** | EventBridge | Tag ngoài giờ, EC2 Running, chờ chu kỳ | Lambda tự chạy, EC2 Stopped | Lambda tự chạy, EC2 chuyển sang Stopped (Hình 7–9) | ☑ Đạt |
| **INT-11** | EventBridge | Lịch report đến giờ | Nhận email báo cáo tự động | Nhận email báo cáo "[AutoSchedule] Running resources" (Hình 10–11) | ☑ Đạt |
| **INT-12** | CloudFormation | Deploy stack lần 1 qua script `07_deploy.sh` | Stack đạt `CREATE_COMPLETE` | Stack `CREATE_COMPLETE`, tạo đầy đủ tài nguyên (Hình 13–18) | ☑ Đạt |
| **INT-13** | CloudFormation | Xóa stack (`delete-stack`) và deploy lại | Stack đạt `CREATE_COMPLETE` lần 2 | Stack `CREATE_COMPLETE` lần 2, chứng minh tính tái lập của IaC | ☑ Đạt |
| **INT-14** | CloudWatch | Gây lỗi Lambda (sai `TOPIC_ARN`) | Alarm chuyển `ALARM`, nhận email, sau đó tự phục hồi về `OK` | Lambda lỗi `InvalidClientTokenId`; alarm `In alarm` lúc 04:20:49 UTC, nhận email cảnh báo; tự về `OK` lúc 04:35:49 UTC (Hình 31–35) | ☑ Đạt |

---

## Bảng rà soát bảo mật Tuần 3

| Hạng mục kiểm tra | Tiêu chuẩn đánh giá | Kết quả thực tế | Minh chứng | Trạng thái |
|---|---|---|---|:---:|
| **Phạm vi tác động** | Lambda chỉ quản lý tài nguyên có `Project=AutoSchedule` và `Schedule` | Hàm `desired_running()` kiểm tra chặt chẽ, bỏ qua tài nguyên không thuộc dự án | 11 unit tests passed (Tuần 2) | ☑ Đạt |
| **Bảo mật mã nguồn** | Không lưu mật khẩu, access key, secret key trong repo Git | Lệnh `grep -rniE "password\|secret\|AKIA" src infra scripts` chỉ thấy tham chiếu biến | Hình 28 | ☑ Đạt |
| **Truy cập cơ sở dữ liệu** | RDS không được mở ra Internet công cộng | `Publicly accessible = No` | Hình 21 | ☑ Đạt |
| **Mật khẩu cơ sở dữ liệu** | Mật khẩu RDS không nằm trong code, lưu trữ được mã hóa | Master password hiển thị dạng ẩn; `Encryption: Enabled` | Hình 22 | ☑ Đạt |
| **Tường lửa mạng** | Security Group không mở cổng DB/SSH ra Internet (`0.0.0.0/0`) | Chỉ dùng SG default với 1 inbound rule nội bộ từ chính SG đó | Hình 23 | ☑ Đạt |
| **Bảo mật lưu trữ S3** | S3 bucket chặn toàn bộ truy cập công cộng | `Block all public access = On` (bật đủ cả 4 tiêu chí) | Hình 24 | ☑ Đạt |
| **Mã hóa lưu trữ S3** | Mã hóa dữ liệu lưu trữ trên S3 bucket | `Default encryption: SSE-S3` | Hình 25 | ☑ Đạt |
| **Giới hạn tài nguyên Lambda** | Giới hạn bộ nhớ và thời gian chạy để tránh cạn ngân sách lab | Memory: 128 MB, Timeout: 2 phút (120 giây) | Hình 26 | ☑ Đạt |
| **Lưu trữ nhật ký** | Thời gian lưu log CloudWatch hợp lý để tiết kiệm chi phí | Log group `/aws/lambda/autoschedule` có `Retention = 1 week` (7 ngày) | Hình 27 | ☑ Đạt |
| **Phân loại tài nguyên** | Mọi tài nguyên đều được gắn nhãn định danh | Toàn bộ tài nguyên được gắn tag `Project=AutoSchedule` và `Owner` | Đã kiểm tra đối chiếu | ☑ Xong |

---

## Liên kết sản phẩm Tuần 3 trên GitHub

1. **Mã nguồn CloudFormation template:** [infra/template.yaml](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/infra/template.yaml)
2. **Script triển khai tự động:** [scripts/07_deploy.sh](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/scripts/07_deploy.sh)
3. **Báo cáo Tuần 3 (DOCX):** [reports/Bao_cao_tuan3_Nhom_DevOps_IaC.docx](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/reports/Bao_cao_tuan3_Nhom_DevOps_IaC.docx)
4. **Worklog Tuần 3:** [worklog/week3.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/worklog/week3.md)
5. **Khai báo sử dụng AI Tuần 3:** [docs/ai-disclosure-week3.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/docs/ai-disclosure-week3.md)
6. **Thư mục ảnh minh chứng:** [docs/screenshots/](https://github.com/nguyentrung01ute-ui/autoschedule/tree/main/docs/screenshots)
