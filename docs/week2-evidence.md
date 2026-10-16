# Minh chứng Tuần 2 — AutoSchedule

## Danh sách ảnh minh chứng

| Ảnh | Nội dung | Ghi chú trong báo cáo |
|---|---|---|
| [week2-evidence-01-pytest-11-passed.png](screenshots/week2-evidence-01-pytest-11-passed.png) | Kết quả chạy pytest: 11 test passed | Hình 1 |
| [week2-evidence-02-sns-confirmed.png](screenshots/week2-evidence-02-sns-confirmed.png) | Subscription của SNS topic `autoschedule-report` ở trạng thái Confirmed | Hình 2 |
| [week2-evidence-09-rds-stopped.png](screenshots/week2-evidence-09-rds-stopped.png) | RDS ở trạng thái Stopped (16:36) trước khi test | Hình 9 |
| [week2-evidence-10-rds-tags.png](screenshots/week2-evidence-10-rds-tags.png) | Tag của RDS: `Schedule=08:00-17:00`, `ScheduleDays=Mon-Sun` | Hình 10 |
| [week2-evidence-11-sagemaker-stopped.png](screenshots/week2-evidence-11-sagemaker-stopped.png) | SageMaker Notebook ở trạng thái Stopped (16:36) trước khi test | Hình 11 |
| [week2-evidence-12-sagemaker-tags.png](screenshots/week2-evidence-12-sagemaker-tags.png) | Tag của SageMaker Notebook: `Schedule=08:00-17:00`, `ScheduleDays=Mon-Fri` | Hình 12 |
| [week2-evidence-15-sagemaker-pending.png](screenshots/week2-evidence-15-sagemaker-pending.png) | SageMaker Notebook chuyển sang Pending khi gọi enforce trong giờ (16:40) | Hình 15 |
| [week2-evidence-16-sagemaker-inservice.png](screenshots/week2-evidence-16-sagemaker-inservice.png) | SageMaker Notebook đạt trạng thái InService (16:49) | Hình 16 |
| [week2-evidence-17-rds-starting.png](screenshots/week2-evidence-17-rds-starting.png) | RDS chuyển sang Starting khi gọi enforce trong giờ (16:41) | Hình 17 |
| [week2-evidence-18-rds-available.png](screenshots/week2-evidence-18-rds-available.png) | RDS đạt trạng thái Available (16:48) | Hình 18 |
| [week2-evidence-19-enforce-in-progress-skip.png](screenshots/week2-evidence-19-enforce-in-progress-skip.png) | Enforce lúc 16:42: Actions: `[]` vì tài nguyên đang chuyển trạng thái | Hình 19 |
| [week2-evidence-22-rds-stopping.png](screenshots/week2-evidence-22-rds-stopping.png) | RDS chuyển sang Stopping khi gọi enforce ngoài giờ (17:02) | Hình 22 |
| [week2-evidence-23-sagemaker-stopped.png](screenshots/week2-evidence-23-sagemaker-stopped.png) | SageMaker Notebook chuyển sang Stopped khi gọi enforce ngoài giờ (17:03) | Hình 23 |

---

## Bảng kết quả kiểm thử Tuần 2

| ID | Tài nguyên | Thao tác | Kết quả mong đợi | Kết quả thực tế | Kết quả |
|---|---|---|---|---|:---:|
| **INT-01** | EC2 | Schedule ngoài giờ, đang chạy | STOP EC2, trạng thái Stopped | Log STOP lúc 17:01; EC2 Stopped lúc 17:02 | ☑ Đạt |
| **INT-02** | EC2 | Schedule trong giờ, đang tắt | START EC2, trạng thái Running | Log START lúc 16:39; EC2 Running lúc 16:40 | ☑ Đạt |
| **INT-03** | RDS | Ngoài giờ | STOP RDS, trạng thái Stopped | Log STOP lúc 17:01; RDS chuyển Stopping lúc 17:02 (Hình 22) | ☑ Đạt |
| **INT-04** | RDS | Trong giờ | START RDS, trạng thái Available | Log START lúc 16:39; Starting 16:41 (Hình 17); Available 16:48 (Hình 18) | ☑ Đạt |
| **INT-05** | SageMaker | Ngoài giờ | STOP SageMaker, trạng thái Stopped | Log STOP lúc 17:01; Stopped lúc 17:03 (Hình 23) | ☑ Đạt |
| **INT-06** | SageMaker | Trong giờ | START SageMaker, trạng thái InService | Log START lúc 16:39; Pending 16:40 (Hình 15); InService 16:49 (Hình 16) | ☑ Đạt |
| **INT-07** | EC2 | Không có tag Schedule | Không có hành động | Xóa tag Schedule; enforce lúc 16:40: Actions: `[]`, EC2 vẫn Stopped | ☑ Đạt |
| **--** | EC2 | Schedule=off | Luôn bị tắt | Schedule=off, EC2 Running (16:43); enforce lúc 16:44: STOP EC2; EC2 Stopped lúc 16:47 | ☑ Đạt |
| **INT-08** | EC2 | Schedule=abc | Log cảnh báo, không start/stop | Actions: `[]` và CloudWatch log "Invalid schedule tag" | ☑ Đạt |
| **--** | RDS / SageMaker | Gọi khi đang Starting | Bỏ qua, không start lần hai | Enforce lúc 16:42 cho Actions: `[]` (Hình 19) | ☑ Đạt |
| **INT-09** | SNS | Event report | Nhận email báo cáo | Report chạy thành công; email "[AutoSchedule] Running resources" nhận lúc 16:52 | ☑ Đạt |

---

## Liên kết sản phẩm Tuần 2 trên GitHub

1. **Bộ kiểm thử pytest:** [tests/test_schedule.py](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/tests/test_schedule.py)
2. **Worklog Tuần 2:** [worklog/week2.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/worklog/week2.md)
3. **Mã nguồn Lambda:** [src/scheduler.py](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/src/scheduler.py)
4. **Báo cáo Tuần 2 (DOCX):** [reports/Bao_cao_tuan2_Nhom_DevOps_IaC.docx](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/reports/Bao_cao_tuan2_Nhom_DevOps_IaC.docx)
5. **Khai báo sử dụng AI Tuần 2:** [docs/ai-disclosure-week2.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/docs/ai-disclosure-week2.md)
