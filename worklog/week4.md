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
- **Minh chứng:** Đã cập nhật đủ bộ ảnh minh chứng Tuần 4 (Hình 01–16, gồm `02a`, `02b`) trong `docs/screenshots/`; danh mục tại [docs/week4-evidence.md](../docs/week4-evidence.md)
- **Báo cáo chính thức:** [reports/Bao_cao_tuan4_Nhom_DevOps_IaC.docx](../reports/Bao_cao_tuan4_Nhom_DevOps_IaC.docx)
- **Video demo:** [Google Drive](https://drive.google.com/file/d/1gMQxJKQ81sfH3KW3673XL4wAbYJkwzjC/view?usp=sharing) (9 phút 32 giây)

---

## 2. Phân công, kết quả và commit minh chứng

| Thành viên | Nhiệm vụ cụ thể | Thời lượng | File liên quan | Link commit |
|---|---|---:|---|---|
| **Nguyễn Văn Trung (24110365)** | - **Dựng lại hệ thống từ đầu bằng một lệnh (`INT-15`):** Xóa stack `autoschedule` rồi dựng lại bằng một lệnh `./scripts/07_deploy.sh` đạt `CREATE_COMPLETE`; xác nhận email subscription SNS và chạy test event `report` nhận email báo cáo tài nguyên (Hình 01, 02a, 02b).<br>- **Kiểm thử end-to-end bằng lịch ngắn (`INT-16a`, `INT-16b`):** Đặt khung giờ ngắn bao trùm giờ test (`08:00-23:59`, `Mon-Sun`) bằng `scripts/06_set_schedule.sh` khi cả 3 tài nguyên đang `Stopped`, theo dõi EventBridge (`rate(15 minutes)`) tự động `START` lúc 23:00 và ổn định lúc 23:04 (`EC2 Running`, `RDS Available`, `SageMaker InService` — Hình 03–07). Sau đó đổi sang khung giờ ngoài giờ test (`08:00-09:00`), theo dõi EventBridge tự động `STOP` lúc 23:10 và kiểm tra trạng thái bằng `scripts/05_status.sh` lúc 23:11 (Hình 08–09).<br>- **Dọn dẹp toàn bộ tài nguyên:** Thực hiện `aws cloudformation delete-stack --stack-name autoschedule`, chạy `./scripts/99_cleanup.sh --bucket` xóa EC2, RDS, SageMaker Notebook và S3 bucket, xóa CloudWatch Dashboard và kiểm tra tay các dịch vụ trên AWS Console (`us-east-1`).<br>- **Cập nhật tài liệu & báo cáo:** Bổ sung `INT-15`, `INT-16a`, `INT-16b` vào `docs/test-plan.md`, viết mục Tuần 4 và quy trình Dọn dẹp trong `README.md`, upload Hình 01–09 và báo cáo Word Tuần 4. | **8 giờ 43 phút** | • [scripts/07_deploy.sh](../scripts/07_deploy.sh)<br>• [scripts/06_set_schedule.sh](../scripts/06_set_schedule.sh)<br>• [scripts/05_status.sh](../scripts/05_status.sh)<br>• [scripts/99_cleanup.sh](../scripts/99_cleanup.sh)<br>• [README.md](../README.md)<br>• [docs/test-plan.md](../docs/test-plan.md)<br>• [reports/Bao_cao_tuan4_Nhom_DevOps_IaC.docx](../reports/Bao_cao_tuan4_Nhom_DevOps_IaC.docx) | • [Commit b3196b4](https://github.com/nguyentrung01ute-ui/autoschedule/commit/b3196b48759b6176f752eedc6d5c98c408847888): Thêm báo cáo Word Tuần 4.<br>• Commit bổ sung ảnh minh chứng Hình 01–09 (gồm `02a`, `02b`), `INT-15/16a/16b`, mục Tuần 4 & Dọn dẹp trong `README.md` và worklog. |
| **Nguyễn Văn Thi (24110334)** | - **Test lỗi và Alarm (INT-17, INT-18, INT-19):** tag `Schedule=abc` → log `Invalid schedule tag`, `Actions: []`; gọi enforce khi tài nguyên đang chuyển trạng thái → không start lần hai; gây lỗi bằng `TOPIC_ARN` sai → Alarm `In alarm`, email cảnh báo, về `OK`.<br>- **Tính chi phí và mức tiết kiệm:** nhập cấu hình EC2/RDS/SageMaker vào AWS Pricing Calculator ($96,00/tháng 24/7), quy đổi theo lịch 195/730 giờ (≈ $25,64, tiết kiệm ≈ 73%); chụp ngân sách Learner Lab ($3,5 / $50).<br>- **Tổng hợp báo cáo Tuần 1–4:** điền `docs/report.md`, `docs/cost-analysis.md`, bổ sung INT-11–14 và INT-17–19 vào `docs/test-plan.md`, viết khai báo AI Tuần 4, cập nhật ROADMAP và danh mục ảnh. | **8 giờ 41 phút** | • [docs/week4-evidence.md](../docs/week4-evidence.md)<br>• [docs/cost-analysis.md](../docs/cost-analysis.md)<br>• [docs/report.md](../docs/report.md)<br>• [docs/test-plan.md](../docs/test-plan.md) | • [Commit 1c77812](https://github.com/nguyentrung01ute-ui/autoschedule/commit/1c77812d0444021e395db45397f9f7523325312f): Ảnh minh chứng Hình 10–16, test plan, chi phí, báo cáo cuối kỳ, khai báo AI. |
| **Cả hai thành viên** | Quay video demo, hoàn thiện báo cáo, cập nhật worklog và commit lên Git, ôn vấn đáp. | Đã tính trong tổng giờ | [docs/ROADMAP.md](../docs/ROADMAP.md) | Đồng bộ trên nhánh `main`. |

---

## 3. Nhật ký công việc và liên kết kiểm chứng (phần Nguyễn Văn Trung — 8 giờ 43 phút)

| Ngày | Hạng mục công việc | Thời lượng | Có dùng AI? | Sản phẩm / File kiểm tra | Minh chứng |
|---|---|---:|---|---|---|
| 28/10/2026 | Xóa stack cũ và dựng lại toàn bộ hệ thống từ đầu bằng một lệnh `./scripts/07_deploy.sh`, xác nhận email subscription SNS và chạy test event `report` (`INT-15`) | 1 giờ 30 phút | Có (tham khảo kịch bản kiểm tra tái lập) | [scripts/07_deploy.sh](../scripts/07_deploy.sh) · [infra/template.yaml](../infra/template.yaml) | [Hình 1](../docs/screenshots/week4-evidence-01.png) · [Hình 2a](../docs/screenshots/week4-evidence-02a.png) · [Hình 2b](../docs/screenshots/week4-evidence-02b.png) |
| 29/10/2026 | Đặt lịch ngắn (`Schedule=08:00-23:59`, `Mon-Sun`) bằng `06_set_schedule.sh` và theo dõi EventBridge tự động `START` cả 3 tài nguyên EC2, RDS, SageMaker (`INT-16a`) | 1 giờ 45 phút | Có (tham khảo cách chọn khung giờ chờ RDS/SageMaker ổn định) | [scripts/06_set_schedule.sh](../scripts/06_set_schedule.sh) · [scripts/05_status.sh](../scripts/05_status.sh) | [Hình 3](../docs/screenshots/week4-evidence-03.png) · [Hình 4](../docs/screenshots/week4-evidence-04.png) · [Hình 5](../docs/screenshots/week4-evidence-05.png) · [Hình 6](../docs/screenshots/week4-evidence-06.png) · [Hình 7](../docs/screenshots/week4-evidence-07.png) |
| 29/10/2026 | Đổi lịch sang ngoài khung giờ (`08:00-09:00`), theo dõi EventBridge tự động `STOP` cả 3 tài nguyên và kiểm tra trạng thái sau khi tắt bằng `05_status.sh` (`INT-16b`) | 1 giờ 15 phút | Không | [scripts/06_set_schedule.sh](../scripts/06_set_schedule.sh) · [scripts/05_status.sh](../scripts/05_status.sh) | [Hình 8](../docs/screenshots/week4-evidence-08.png) · [Hình 9](../docs/screenshots/week4-evidence-09.png) |
| 30/10/2026 | Dọn dẹp toàn bộ tài nguyên (`aws cloudformation delete-stack`, `./scripts/99_cleanup.sh --bucket`, xóa Dashboard) và kiểm tra tay các dịch vụ trên AWS Console (`us-east-1`) | 1 giờ 13 phút | Có (tham khảo checklist rà soát tài nguyên sót) | [scripts/99_cleanup.sh](../scripts/99_cleanup.sh) · [README.md](../README.md) | Đã đối chiếu đủ 6 hạng mục kiểm tra sau dọn dẹp tại Mục 2.6 báo cáo Tuần 4 |
| 31/10/2026 | Bổ sung `INT-15`, `INT-16a`, `INT-16b` vào `docs/test-plan.md`, viết mục Tuần 4 & mục Dọn dẹp trong `README.md`, chuẩn bị ảnh minh chứng 01–09 và hoàn thiện báo cáo Tuần 4 | 1 giờ 30 phút | Có (hỗ trợ rà soát trình bày tài liệu) | [docs/test-plan.md](../docs/test-plan.md) · [README.md](../README.md) · [Báo cáo Tuần 4](../reports/Bao_cao_tuan4_Nhom_DevOps_IaC.docx) | [Commit b3196b4](https://github.com/nguyentrung01ute-ui/autoschedule/commit/b3196b48759b6176f752eedc6d5c98c408847888) · [docs/screenshots/](../docs/screenshots/) |
| 31/10/2026 | Phối hợp quay video demo tổng kết (9 phút 32 giây), ghi nhận worklog Tuần 4, đồng bộ Git và ôn tập câu hỏi vấn đáp | 1 giờ 30 phút | Có (tham khảo bố cục kịch bản demo ≤ 10 phút) | [worklog/week4.md](week4.md) · [docs/demo-script.md](../docs/demo-script.md) | [Video demo](https://drive.google.com/file/d/1gMQxJKQ81sfH3KW3673XL4wAbYJkwzjC/view?usp=sharing) |

---

## 4. Nhật ký công việc và liên kết kiểm chứng (phần Nguyễn Văn Thi — 8 giờ 41 phút)

| Hạng mục công việc | Có dùng AI? | Sản phẩm | Minh chứng |
|---|---|---|---|
| Test tag `Schedule` sai định dạng (INT-17) | Không | Lambda test event | [Hình 10](../docs/screenshots/week4-evidence-10.png) |
| Test gọi enforce khi tài nguyên đang chuyển trạng thái (INT-18) | Không | Lambda test event | [Hình 11](../docs/screenshots/week4-evidence-11.png) |
| Test Alarm `autoschedule-errors`: ALARM → email → OK (INT-19) | Có (tham khảo kịch bản) | CloudWatch / SNS | [Hình 12](../docs/screenshots/week4-evidence-12.jpg) · [Hình 13](../docs/screenshots/week4-evidence-13.jpg) · [Hình 14](../docs/screenshots/week4-evidence-14.jpg) |
| Ghi nhận ngân sách Learner Lab | Không | AWS Academy | [Hình 15](../docs/screenshots/week4-evidence-15.png) |
| Tính chi phí bằng AWS Pricing Calculator và mức tiết kiệm | Có (tham khảo cách quy đổi) | [docs/cost-analysis.md](../docs/cost-analysis.md) | [Hình 16](../docs/screenshots/week4-evidence-16.png) |
| Tổng hợp báo cáo cuối kỳ, test plan, ROADMAP, khai báo AI | Có (hỗ trợ trình bày) | [docs/report.md](../docs/report.md) · [docs/test-plan.md](../docs/test-plan.md) · [docs/ai-disclosure-week4.md](../docs/ai-disclosure-week4.md) | [Commit 1c77812](https://github.com/nguyentrung01ute-ui/autoschedule/commit/1c77812d0444021e395db45397f9f7523325312f) |



---

## 5. Tổng hợp thời lượng Tuần 4

| Thành viên | MSSV | Vai trò | Tổng thời gian |
|---|---|---|---:|
| **Nguyễn Văn Trung** | 24110365 | Nhóm trưởng (DevOps & IaC) | **8 giờ 43 phút** |
| **Nguyễn Văn Thi** | 24110334 | Thành viên (DevOps & IaC) | **8 giờ 41 phút** |
| **Tổng cộng cả nhóm** | | | **17 giờ 24 phút** |

*Cả hai thành viên đều đáp ứng thời lượng tối thiểu 8 giờ/tuần.*

---

## 6. Tài liệu liên quan

- [Danh mục minh chứng Tuần 4](../docs/week4-evidence.md)
- [Kế hoạch kiểm thử](../docs/test-plan.md)
- [Hướng dẫn Tuần 4 & Dọn dẹp (README)](../README.md)
- [Phân tích chi phí](../docs/cost-analysis.md)
- [Báo cáo cuối kỳ](../docs/report.md)
- [Báo cáo Word Tuần 4 (.docx)](../reports/Bao_cao_tuan4_Nhom_DevOps_IaC.docx)
- [Khai báo sử dụng AI Tuần 4](../docs/ai-disclosure-week4.md)
- [Roadmap](../docs/ROADMAP.md)
- [Worklog Tuần 3](week3.md)
