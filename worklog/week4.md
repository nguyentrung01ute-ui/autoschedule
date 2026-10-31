# Worklog tuần 4 — AutoSchedule

## 1. Thông tin chung

- **Nhóm:** DevOps & IaC
- **Dự án:** AutoSchedule — tự động bật/tắt tài nguyên AWS theo lịch học
- **Môi trường:** AWS Learner Lab, Region `us-east-1` (dùng IAM role có sẵn `LabRole`)
- **Thời gian thực hiện:** Tuần 4 (27/10/2026 – 02/11/2026)
- **Thành viên:**
  - Nguyễn Văn Trung (MSSV: 24110365) — Nhóm trưởng
  - Nguyễn Văn Thi (MSSV: 24110334) — Thành viên
- **Tổng thời lượng đã ghi nhận:** 17 giờ 24 phút
  - **Nguyễn Văn Trung:** 8 giờ 43 phút
  - **Nguyễn Văn Thi:** 8 giờ 41 phút
- **Minh chứng:** [docs/week4-evidence.md](../docs/week4-evidence.md)
- **Báo cáo chính thức:** [reports/Bao_cao_tuan4_Nhom_DevOps_IaC.docx](../reports/Bao_cao_tuan4_Nhom_DevOps_IaC.docx)
- **Video demo:** [Google Drive](https://drive.google.com/file/d/1gMQxJKQ81sfH3KW3673XL4wAbYJkwzjC/view?usp=sharing) (9 phút 32 giây)

---

## 2. Phân công, kết quả và commit minh chứng

| Thành viên | Nhiệm vụ cụ thể | Thời lượng | File liên quan | Link commit |
|---|---|---:|---|---|
| **Nguyễn Văn Trung (24110365)** | Dựng lại hệ thống bằng một lệnh `./scripts/07_deploy.sh` (INT-15); đặt lịch ngắn bằng `06_set_schedule.sh` và theo dõi test end-to-end EC2, RDS, SageMaker (INT-16a/b); dọn dẹp tài nguyên (`delete-stack`, `99_cleanup.sh --bucket`) và kiểm tra tay tài nguyên còn sót. *(Chi tiết và Hình 01–09 do Trung cập nhật.)* | **8 giờ 43 phút** | [reports/Bao_cao_tuan4_Nhom_DevOps_IaC.docx](../reports/Bao_cao_tuan4_Nhom_DevOps_IaC.docx) | • [Commit b3196b4](https://github.com/nguyentrung01ute-ui/autoschedule/commit/b3196b48759b6176f752eedc6d5c98c408847888): Thêm báo cáo Word Tuần 4. |
| **Nguyễn Văn Thi (24110334)** | - **Test lỗi và Alarm (INT-17, INT-18, INT-19):** tag `Schedule=abc` → log `Invalid schedule tag`, `Actions: []`; gọi enforce khi tài nguyên đang chuyển trạng thái → không start lần hai; gây lỗi bằng `TOPIC_ARN` sai → Alarm `In alarm`, email cảnh báo, về `OK`.<br>- **Tính chi phí và mức tiết kiệm:** nhập cấu hình EC2/RDS/SageMaker vào AWS Pricing Calculator ($96,00/tháng 24/7), quy đổi theo lịch 195/730 giờ (≈ $25,64, tiết kiệm ≈ 73%); chụp ngân sách Learner Lab ($3,5 / $50).<br>- **Tổng hợp báo cáo Tuần 1–4:** điền `docs/report.md`, `docs/cost-analysis.md`, bổ sung INT-11–14 và INT-17–19 vào `docs/test-plan.md`, viết khai báo AI Tuần 4, cập nhật ROADMAP và danh mục ảnh. | **8 giờ 41 phút** | • [docs/week4-evidence.md](../docs/week4-evidence.md)<br>• [docs/cost-analysis.md](../docs/cost-analysis.md)<br>• [docs/report.md](../docs/report.md)<br>• [docs/test-plan.md](../docs/test-plan.md) | • [Commit 1c77812](https://github.com/nguyentrung01ute-ui/autoschedule/commit/1c77812d0444021e395db45397f9f7523325312f): Ảnh minh chứng Hình 10–16, test plan, chi phí, báo cáo cuối kỳ, khai báo AI. |
| **Cả hai thành viên** | Quay video demo, hoàn thiện báo cáo, cập nhật worklog và commit lên Git, ôn vấn đáp. | Đã tính trong tổng giờ | [docs/ROADMAP.md](../docs/ROADMAP.md) | Đồng bộ trên nhánh `main`. |

---

## 3. Nhật ký công việc và liên kết kiểm chứng (phần Nguyễn Văn Thi)

| Hạng mục công việc | Có dùng AI? | Sản phẩm | Minh chứng |
|---|---|---|---|
| Test tag `Schedule` sai định dạng (INT-17) | Không | Lambda test event | [Hình 10](../docs/screenshots/week4-evidence-10.png) |
| Test gọi enforce khi tài nguyên đang chuyển trạng thái (INT-18) | Không | Lambda test event | [Hình 11](../docs/screenshots/week4-evidence-11.png) |
| Test Alarm `autoschedule-errors`: ALARM → email → OK (INT-19) | Có (tham khảo kịch bản) | CloudWatch / SNS | [Hình 12](../docs/screenshots/week4-evidence-12.jpg) · [Hình 13](../docs/screenshots/week4-evidence-13.jpg) · [Hình 14](../docs/screenshots/week4-evidence-14.jpg) |
| Ghi nhận ngân sách Learner Lab | Không | AWS Academy | [Hình 15](../docs/screenshots/week4-evidence-15.png) |
| Tính chi phí bằng AWS Pricing Calculator và mức tiết kiệm | Có (tham khảo cách quy đổi) | [docs/cost-analysis.md](../docs/cost-analysis.md) | [Hình 16](../docs/screenshots/week4-evidence-16.png) |
| Tổng hợp báo cáo cuối kỳ, test plan, ROADMAP, khai báo AI | Có (hỗ trợ trình bày) | [docs/report.md](../docs/report.md) · [docs/test-plan.md](../docs/test-plan.md) · [docs/ai-disclosure-week4.md](../docs/ai-disclosure-week4.md) | [Commit 1c77812](https://github.com/nguyentrung01ute-ui/autoschedule/commit/1c77812d0444021e395db45397f9f7523325312f) |

> Hình 10–14 dùng lại từ minh chứng thực tế Tuần 2 (Hình 25, 19) và Tuần 3 (Hình 33–35), đã ghi nguồn trong báo cáo.

---

## 4. Tổng hợp thời lượng Tuần 4

| Thành viên | MSSV | Vai trò | Tổng thời gian |
|---|---|---|---:|
| **Nguyễn Văn Trung** | 24110365 | Nhóm trưởng (DevOps & IaC) | **8 giờ 43 phút** |
| **Nguyễn Văn Thi** | 24110334 | Thành viên (DevOps & IaC) | **8 giờ 41 phút** |
| **Tổng cộng cả nhóm** | | | **17 giờ 24 phút** |

*Cả hai thành viên đều đáp ứng thời lượng tối thiểu 8 giờ/tuần.*

---

## 5. Tài liệu liên quan

- [Danh mục minh chứng Tuần 4](../docs/week4-evidence.md)
- [Kế hoạch kiểm thử](../docs/test-plan.md)
- [Phân tích chi phí](../docs/cost-analysis.md)
- [Báo cáo cuối kỳ](../docs/report.md)
- [Khai báo sử dụng AI Tuần 4](../docs/ai-disclosure-week4.md)
- [Roadmap](../docs/ROADMAP.md)
- [Worklog Tuần 3](week3.md)
