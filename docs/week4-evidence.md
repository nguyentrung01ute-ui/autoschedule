# Minh chứng Tuần 4 — AutoSchedule

> Tuần 4 (27/10/2026 – 02/11/2026). Số hình khớp với [báo cáo Tuần 4](../reports/Bao_cao_tuan4_Nhom_DevOps_IaC.docx).
> Hình 01–09 (dựng lại stack, test end-to-end INT-15, INT-16a/b) do Nguyễn Văn Trung thực hiện.
> Hình 10–16 (test lỗi, Alarm, chi phí) do Nguyễn Văn Thi phụ trách.

## Danh sách ảnh minh chứng (Hình 01–16)

| Ảnh | Nội dung | Ghi chú trong báo cáo |
|---|---|---|
| [week4-evidence-01.png](screenshots/week4-evidence-01.png) | Stack CloudFormation `autoschedule` ở trạng thái `CREATE_COMPLETE` (tab Resources) sau khi dựng lại bằng `./scripts/07_deploy.sh` | Hình 1 (INT-15) |
| [week4-evidence-02a.png](screenshots/week4-evidence-02a.png) | Email xác nhận subscription SNS sau khi dựng lại | Hình 2 (INT-15) |
| [week4-evidence-02b.png](screenshots/week4-evidence-02b.png) | Email báo cáo "[AutoSchedule] Running resources" nhận được sau khi dựng lại | Hình 2 (INT-15) |
| [week4-evidence-03.png](screenshots/week4-evidence-03.png) | Kết quả `06_set_schedule.sh` đặt lịch `08:00-23:59` `Mon-Sun` | Hình 3 (INT-16a) |
| [week4-evidence-04.png](screenshots/week4-evidence-04.png) | Log CloudWatch: `Actions` có `START` cho EC2, RDS và SageMaker | Hình 4 (INT-16a) |
| [week4-evidence-05.png](screenshots/week4-evidence-05.png) | EC2 ở trạng thái `Running` | Hình 5 (INT-16a) |
| [week4-evidence-06.png](screenshots/week4-evidence-06.png) | RDS ở trạng thái `Available` | Hình 6 (INT-16a) |
| [week4-evidence-07.png](screenshots/week4-evidence-07.png) | SageMaker Notebook ở trạng thái `InService` | Hình 7 (INT-16a) |
| [week4-evidence-08.png](screenshots/week4-evidence-08.png) | Log CloudWatch: `Actions` có `STOP` cho cả ba tài nguyên | Hình 8 (INT-16b) |
| [week4-evidence-09.png](screenshots/week4-evidence-09.png) | `05_status.sh` sau khi tắt: EC2 và SageMaker `Stopped`, RDS đang `Stopping` | Hình 9 (INT-16b) |
| [week4-evidence-10.png](screenshots/week4-evidence-10.png) | Lambda test event với EC2 tag `Schedule=abc`: log `Invalid schedule tag ... not enough values to unpack`, response `"actions": []` | Hình 10 (INT-17). Nguồn: báo cáo Tuần 2, Hình 25 |
| [week4-evidence-11.png](screenshots/week4-evidence-11.png) | Gọi enforce khi tài nguyên đang chuyển trạng thái (Starting): response `"actions": []`, không start lần hai | Hình 11 (INT-18). Nguồn: báo cáo Tuần 2, Hình 19 |
| [week4-evidence-12.jpg](screenshots/week4-evidence-12.jpg) | CloudWatch Alarm `autoschedule-errors` ở trạng thái `In alarm` (2026-10-25 04:20:49 UTC) | Hình 12 (INT-19). Nguồn: báo cáo Tuần 3, Hình 33 |
| [week4-evidence-13.jpg](screenshots/week4-evidence-13.jpg) | Email SNS `ALARM: "autoschedule-errors" in US East (N. Virginia)`, State Change `OK -> ALARM`, metric `AWS/Lambda Errors` | Hình 13 (INT-19). Nguồn: báo cáo Tuần 3, Hình 34 |
| [week4-evidence-14.jpg](screenshots/week4-evidence-14.jpg) | Alarm `autoschedule-errors` trở về `OK` (04:35:49 UTC) sau khi khôi phục `TOPIC_ARN` | Hình 14 (INT-19). Nguồn: báo cáo Tuần 3, Hình 35 |
| [week4-evidence-15.png](screenshots/week4-evidence-15.png) | Ngân sách AWS Academy Learner Lab tại thời điểm báo cáo: `Used $3.5 of $50` | Hình 15 |
| [week4-evidence-16.png](screenshots/week4-evidence-16.png) | AWS Pricing Calculator (US East N. Virginia): EC2 $4,44, SageMaker $36,70, RDS MySQL $54,86; tổng $96,00/tháng, $1.152,00/12 tháng | Hình 16 |

> [!NOTE]
> Hình 10–14 được dùng lại từ minh chứng Tuần 2 và Tuần 3 (đã ghi rõ nguồn trong báo cáo Word). Tuần 4 không gây lỗi lại để tránh tốn ngân sách lab; kết quả kiểm thử dựa trên các lần chạy thực tế đó.

---

## Bảng kết quả kiểm thử Tuần 4

| ID | Thành phần | Thao tác | Kết quả mong đợi | Kết quả thực tế | Kết quả |
|---|---|---|---|---|:---:|
| **INT-15** | CloudFormation | Xóa stack, dựng lại bằng một lệnh (`./scripts/07_deploy.sh`) | `CREATE_COMPLETE`, nhận email | Stack `CREATE_COMPLETE`; nhận email xác nhận subscription và email báo cáo (Hình 1–2) | ☑ Đạt |
| **INT-16a** | EventBridge | Lịch ngắn, EC2/RDS/SageMaker Stopped, chờ chu kỳ | Cả ba tự `START` | Lambda tự `START` lúc 23:00 cho EC2, RDS, SageMaker; cả ba ổn định lúc 23:04 (Hình 3–7) | ☑ Đạt |
| **INT-16b** | EventBridge | Hết khung giờ, chờ chu kỳ | Cả ba tự `STOP` | Lambda tự `STOP` lúc 23:10 cho cả ba; EC2 và SageMaker `Stopped`, RDS `Stopping` lúc 23:11 (Hình 8–9) | ☑ Đạt |
| **INT-17** | Lambda | Tag `Schedule` sai (`abc`) | Log cảnh báo, không start/stop | Log `Invalid schedule tag`, `Actions: []` (Hình 10) | ☑ Đạt |
| **INT-18** | Lambda | Gọi enforce khi tài nguyên đang chuyển trạng thái | Bỏ qua, không start lần hai | `Actions: []`, không gọi start lần hai (Hình 11) | ☑ Đạt |
| **INT-19** | CloudWatch | Gây lỗi Lambda (`TOPIC_ARN` sai) | Alarm `ALARM`, có email, sau đó về `OK` | Alarm `In alarm` lúc 04:20:49 UTC, nhận email cảnh báo, về `OK` lúc 04:35:49 UTC (Hình 12–14) | ☑ Đạt |

---

## Chi phí (Hình 15–16)

Chi tiết tính toán tại [docs/cost-analysis.md](cost-analysis.md).

| Tài nguyên | 24/7 (730 giờ) | Theo lịch (195 giờ) | Tiết kiệm |
|---|---:|---:|---:|
| EC2 t3.nano | ≈ $4,44 | ≈ $1,19 | ≈ $3,25 |
| RDS MySQL db.t3.micro | ≈ $54,86 | ≈ $14,65 | ≈ $40,21 |
| SageMaker ml.t3.medium | ≈ $36,70 | ≈ $9,80 | ≈ $26,90 |
| **Tổng** | **≈ $96,00** | **≈ $25,64** | **≈ $70,36 (73%)** |

---

## Liên kết sản phẩm Tuần 4 trên GitHub

1. **Báo cáo Tuần 4 (DOCX):** [reports/Bao_cao_tuan4_Nhom_DevOps_IaC.docx](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/reports/Bao_cao_tuan4_Nhom_DevOps_IaC.docx)
2. **Worklog Tuần 4:** [worklog/week4.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/worklog/week4.md)
3. **Kế hoạch kiểm thử:** [docs/test-plan.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/docs/test-plan.md)
4. **Phân tích chi phí:** [docs/cost-analysis.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/docs/cost-analysis.md)
5. **Báo cáo cuối kỳ:** [docs/report.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/docs/report.md)
6. **Khai báo sử dụng AI Tuần 4:** [docs/ai-disclosure-week4.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/docs/ai-disclosure-week4.md)
7. **Video demo:** [Google Drive](https://drive.google.com/file/d/1gMQxJKQ81sfH3KW3673XL4wAbYJkwzjC/view?usp=sharing)
