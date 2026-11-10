# Tổng hợp phân công thành viên theo tuần — AutoSchedule

Nguồn đối chiếu:
- **Trong báo cáo Word (doc):** `reports/Bao_cao_tuan{1..4}_Nhom_DevOps_IaC.docx` (mục "Phân công và số giờ").
- **Ngoài doc (file trong repo):** `worklog/week{1..4}.md` (chi tiết nhiệm vụ, file, commit).

**Thành viên:** Nguyễn Văn Trung (24110365, nhóm trưởng) · Nguyễn Văn Thi (24110334)

---

## Tuần 1 — Thiết kế và dựng nền tảng

| Thành viên | Phân công | Sản phẩm / commit | Giờ |
|---|---|---|---:|
| **Trung** | Khởi tạo repo, `PROJECT_PLAN.md`, CI/CD; tạo S3 và EC2 mẫu, script kiểm tra trạng thái; phát triển Lambda `scheduler.py` và CloudFormation `template.yaml` | `PROJECT_PLAN.md`, `scripts/config.sh`, `01_setup_s3.sh`, `02_create_ec2.sh`, `05_status.sh`, `src/scheduler.py`, `infra/template.yaml`; commit `af6090b`, `2debfac`, `e91853a` | 8h30 |
| **Thi** | Thiết kế kiến trúc (luồng Enforce/Report, timezone UTC→ICT, quy ước tag, ràng buộc Learner Lab); viết runbook tuần 1; script tạo RDS MySQL và SageMaker Notebook | `docs/architecture.md`, `docs/week1-runbook.md`, `03_create_rds.sh`, `04_create_sagemaker.sh`; commit `1fd8d61`, `68cce06`, `8bbadaa` | 8h20 |
| **Cả hai** | Tìm hiểu EventBridge, boto3, giới hạn Learner Lab; rà soát tài nguyên và worklog | commit `ce66c72` | (đã tính) |

**Tổng nhóm:** 16h50

## Tuần 2 — Unit test, SNS, kiểm thử Lambda thủ công

| Thành viên | Phân công | Sản phẩm / commit | Giờ |
|---|---|---|---:|
| **Trung** | Phát triển Lambda core, phân tích `desired_running()`, xử lý timezone; tạo Lambda thủ công (Python 3.12, `LabRole`, 128 MB, timeout 120s, biến môi trường); kiểm thử EC2 START/STOP, tag sai/`off`/không có tag, email báo cáo SNS; soạn và định dạng báo cáo Word, sắp xếp ảnh minh chứng | `src/scheduler.py`, `tests/events/*.json`; commit `e91853a`; báo cáo Word tuần 2 | 8h40 |
| **Thi** | Tạo SNS topic `autoschedule-report` và xác nhận subscription; viết 11 unit test pytest cho `desired_running()`; kiểm thử tích hợp RDS và SageMaker (START/STOP, bỏ qua khi đang chuyển trạng thái); soạn phần báo cáo RDS/SageMaker/SNS (INT-03 đến INT-06); quản lý Git cá nhân | `tests/test_schedule.py`, `worklog/week2.md`, `docs/screenshots/`; commit `c90a945`, `9f54fe9` | 8h37 |
| **Cả hai** | Chạy kiểm thử end-to-end, đối chiếu log CloudWatch với console, rà soát và hoàn thiện báo cáo | — | (đã tính) |

**Tổng nhóm:** 17h17

## Tuần 3 — EventBridge tự kích hoạt, CloudFormation, bảo mật

| Thành viên | Phân công | Sản phẩm / commit | Giờ |
|---|---|---|---:|
| **Trung** | Tạo 2 lịch EventBridge Scheduler thủ công (enforce mỗi 15 phút, report 08:00 VN); kiểm thử tự kích hoạt (INT-10a/10b/11); rà soát bảo mật theo 10 tiêu chuẩn; CloudWatch Dashboard và kiểm thử Alarm (INT-14) | `infra/template.yaml`, `worklog/week3.md`, `docs/week3-evidence.md`; commit `add1c60`, `8a0adff` | 8h28 |
| **Thi** | Xóa tài nguyên tạo thủ công (2 lịch, Lambda, SNS, log group); hoàn thiện `07_deploy.sh`; deploy CloudFormation lần 1 (INT-12); xóa và dựng lại stack (INT-13); đặt tên, phân loại, upload 34 ảnh minh chứng; biên tập báo cáo tuần 3 | `scripts/07_deploy.sh`, `reports/Bao_cao_tuan3_...docx`, `docs/screenshots/`; commit `9a5f5ef`, `8a0adff` | 8h37 |
| **Cả hai** | Thống nhất cấu hình template, đối chiếu yêu cầu bảo mật, theo dõi log CloudWatch, hoàn thiện báo cáo | — | (đã tính) |

**Tổng nhóm:** 17h05

## Tuần 4 — End-to-end, test lỗi, chi phí, demo, dọn dẹp

| Thành viên | Phân công | Sản phẩm / commit | Giờ |
|---|---|---|---:|
| **Trung** | Dựng lại hệ thống bằng một lệnh `07_deploy.sh` (INT-15); test end-to-end lịch ngắn START/STOP bằng `06_set_schedule.sh` và `05_status.sh` (INT-16a/16b); dọn dẹp (`delete-stack`, `99_cleanup.sh --bucket`, kiểm tra tay trên Console); bổ sung INT-15/16 vào `test-plan.md`, viết mục Tuần 4 và Dọn dẹp trong `README.md`, upload ảnh 01–09 | `scripts/06_set_schedule.sh`, `99_cleanup.sh`, `docs/test-plan.md`, `README.md`; commit `b3196b4` | 8h43 |
| **Thi** | Test lỗi và Alarm (INT-17 tag sai, INT-18 đang chuyển trạng thái, INT-19 `TOPIC_ARN` sai); tính chi phí và mức tiết kiệm (Pricing Calculator: \$96/tháng chạy 24/7 → ≈\$25,64 theo lịch, tiết kiệm ≈73%); tổng hợp báo cáo tuần 1–4 (`report.md`, `cost-analysis.md`, test plan INT-11–14, 17–19, khai báo AI, ROADMAP) | `docs/week4-evidence.md`, `docs/cost-analysis.md`, `docs/report.md`, `docs/ai-disclosure-week4.md`; commit `1c77812` | 8h41 |
| **Cả hai** | Quay video demo (9 phút 32 giây), hoàn thiện báo cáo, cập nhật worklog, commit Git, ôn vấn đáp | `docs/demo-script.md`, `docs/ROADMAP.md`, video demo | (đã tính) |

**Tổng nhóm:** 17h24

---

## Tổng hợp cả 4 tuần

| Thành viên | T1 | T2 | T3 | T4 | Tổng |
|---|---:|---:|---:|---:|---:|
| Nguyễn Văn Trung | 8h30 | 8h40 | 8h28 | 8h43 | **34h21** |
| Nguyễn Văn Thi | 8h20 | 8h37 | 8h37 | 8h41 | **34h15** |
| **Cả nhóm** | 16h50 | 17h17 | 17h05 | 17h24 | **68h36** |

Cả hai thành viên đều đạt tối thiểu 8 giờ/tuần.

## Vai trò nổi bật

- **Trung:** hạ tầng và mã nguồn lõi (repo, S3/EC2, Lambda, CloudFormation), EventBridge, bảo mật, Dashboard, dựng lại một lệnh, test end-to-end, dọn dẹp.
- **Thi:** thiết kế kiến trúc và runbook, RDS/SageMaker, SNS, unit test pytest, script deploy IaC, test lỗi/Alarm, chi phí, tổng hợp báo cáo cuối kỳ.

## Điểm khác biệt giữa doc và worklog

- Báo cáo Word tuần 3 và 4 ghi phân công **ngắn hơn** worklog. Ví dụ Word tuần 3 không nêu `07_deploy.sh`, 10 tiêu chuẩn bảo mật hay 34 ảnh minh chứng. Word tuần 4 không nêu phần tài liệu (`test-plan.md`, `README.md`) của Trung.
- Worklog tuần 4 giao `07_deploy.sh` cho **Trung** chạy ở INT-15. Script này do **Thi** viết ở tuần 3.
- Số giờ của từng người và tổng nhóm **khớp** giữa Word và worklog ở cả 4 tuần.

