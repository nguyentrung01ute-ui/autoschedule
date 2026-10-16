# Worklog tuần 2 — AutoSchedule

## 1. Thông tin chung

- **Nhóm:** DevOps & IaC
- **Dự án:** AutoSchedule — tự động bật/tắt tài nguyên AWS theo lịch học
- **Môi trường:** AWS Learner Lab, Region `us-east-1` (dùng IAM role có sẵn `LabRole`)
- **Thời gian thực hiện:** Tuần 2 (13/10/2026 – 19/10/2026)
- **Thành viên:** 
  - Nguyễn Văn Thi (MSSV: 24110334)
  - Nguyễn Văn Trung (MSSV: 24110365)
- **Tổng thời lượng đã ghi nhận:** 17 giờ 17 phút
  - **Nguyễn Văn Thi:** 8 giờ 37 phút
  - **Nguyễn Văn Trung:** 8 giờ 40 phút
- **Trạng thái minh chứng:** Đã cập nhật đủ 34 ảnh minh chứng Tuần 2 trong `docs/screenshots/`; danh mục và mô tả từng ảnh được liên kết tại [docs/week2-evidence.md](../docs/week2-evidence.md).

---

## 2. Liên kết Mã Nguồn và Kiểm thử Tuần 2 (Tiêu chí 3)

| Hạng mục mã nguồn | File trong repo | Link trực tiếp trên GitHub | Mô tả tóm tắt |
|---|---|---|---|
| **Bộ kiểm thử tự động (11 tests)** | `tests/test_schedule.py` | [tests/test_schedule.py](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/tests/test_schedule.py) | 11 unit test case với pytest kiểm thử toàn diện logic hàm `desired_running()` (khung giờ thường, qua đêm 22:00-06:00, cuối tuần, tag sai, tag off, không có tag, giờ bắt đầu = kết thúc). |
| **Mã nguồn Lambda chính** | `src/scheduler.py` | [src/scheduler.py](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/src/scheduler.py) | Hàm Lambda Python 3.12 tích hợp xử lý bật/tắt EC2, RDS, SageMaker và gửi email tổng hợp tài nguyên đang chạy qua SNS. |
| **Sự kiện kiểm thử enforce** | `tests/events/enforce.json` | [tests/events/enforce.json](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/tests/events/enforce.json) | Test event `{"action":"enforce"}` mô phỏng kích hoạt bật/tắt tài nguyên theo lịch. |
| **Sự kiện kiểm thử report** | `tests/events/report.json` | [tests/events/report.json](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/tests/events/report.json) | Test event `{"action":"report"}` gọi Lambda tổng hợp tài nguyên đang chạy và publish vào SNS. |

---

## 3. Phân công, Kết quả và Commit Minh Chứng Phát Triển (Tiêu chí 6)

| Thành viên | Nhiệm vụ cụ thể | Thời lượng | Link file mã nguồn / tài liệu liên quan | Link Commit minh chứng công việc phát triển |
|---|---|---:|---|---|
| **Nguyễn Văn Thi (24110334)** | - **Tích hợp SNS**: Tạo SNS topic `autoschedule-report` (Standard), gắn tag (`Project`, `Owner`), đăng ký subscription qua Email và xác nhận Confirmed.<br>- **Viết kiểm thử tự động pytest**: Xây dựng 11 unit test cases kiểm thử hàm `desired_running()` trong `tests/test_schedule.py` bao quát các trường hợp biên và lịch qua đêm.<br>- **Kiểm thử tích hợp RDS & SageMaker**: Thực hiện kiểm thử chuyển trạng thái START trong giờ (RDS Starting $\rightarrow$ Available, SageMaker Pending $\rightarrow$ InService), STOP ngoài giờ (RDS Stopping, SageMaker Stopped) và kiểm tra bỏ qua tài nguyên đang chuyển trạng thái (Actions rỗng `[]`).<br>- **Soạn thảo báo cáo & tổng hợp văn bản**: Soạn thảo các phần kiểm thử RDS/SageMaker/SNS, tổng hợp bảng kết quả kiểm thử (INT-03 đến INT-06), rà soát và hoàn thiện báo cáo Tuần 2.<br>- **Quản lý Git cá nhân**: Thực hiện commit và push code kiểm thử, ảnh minh chứng và worklog. | **8 giờ 37 phút** | • [tests/test_schedule.py](../tests/test_schedule.py)<br>• [worklog/week2.md](week2.md)<br>• [docs/screenshots/](../docs/screenshots/) | • [Commit c90a945](https://github.com/nguyentrung01ute-ui/autoschedule/commit/c90a9459bcdbbfb20c0471f9081164f22fec1a43): Hoàn thiện 11 unit test case kiểm thử logic desired_running.<br>• [Commit 9f54fe9](https://github.com/nguyentrung01ute-ui/autoschedule/commit/9f54fe9d21a7c0304917d16fc189fd7e26522d5e): Thêm bằng chứng và kết quả kiểm thử tích hợp RDS, SageMaker và SNS. |
| **Nguyễn Văn Trung (24110365)** | - **Phát triển AWS Lambda core**: Phân tích hàm `desired_running()`, hoàn thiện logic điều khiển tài nguyên trên Lambda và xử lý timezone.<br>- **Tạo Lambda thủ công & cấu hình**: Tạo function trên AWS Console với cấu hình runtime Python 3.12, role `LabRole`, memory 128 MB, timeout 120s và biến môi trường.<br>- **Kiểm thử EC2 & báo cáo SNS**: Kiểm thử START/STOP EC2 qua tag, test trường hợp tag sai định dạng, tag `off`, không tag Schedule và test nhận email báo cáo SNS.<br>- **Soạn thảo và định dạng báo cáo Word**: Tổng hợp nội dung chung, sắp xếp hình ảnh minh chứng và rà soát báo cáo trước khi nộp. | **8 giờ 40 phút** | • [src/scheduler.py](../src/scheduler.py)<br>• [tests/events/enforce.json](../tests/events/enforce.json)<br>• [tests/events/report.json](../tests/events/report.json) | • [Commit b26bf3b](https://github.com/nguyentrung01ute-ui/autoschedule/commit/b26bf3b): Cập nhật mã nguồn và tài liệu liên quan.<br>• [Commit 6916329](https://github.com/nguyentrung01ute-ui/autoschedule/commit/6916329): Điều chỉnh nội dung và liên kết minh chứng tuần. |
| **Cả hai thành viên** | Phối hợp chạy kiểm thử tích hợp end-to-end trên AWS Learner Lab, xác minh log CloudWatch đối chiếu với console, rà soát kết quả kiểm thử và hoàn thiện hồ sơ báo cáo. | Đã tính trong tổng giờ | [Kế hoạch](../PROJECT_PLAN.md) · [Scheduler](../src/scheduler.py) · [Báo cáo Tuần 2](week2.md) | Phối hợp đồng bộ kết quả trên nhánh chính `main`. |

---

## 4. Nhật ký công việc và liên kết kiểm chứng thực tế

| Hạng mục công việc | Người phụ trách | File kiểm tra / Mã kiểm thử | Trạng thái & Ảnh minh chứng thực tế |
|---|---|---|---|
| Chạy pytest kiểm thử logic hàm `desired_running()` (11 tests passed) | Nguyễn Văn Thi | [tests/test_schedule.py](../tests/test_schedule.py) | [week2-evidence-01-pytest-11-passed.png](../docs/screenshots/week2-evidence-01-pytest-11-passed.png) (Hình 1 trong báo cáo) |
| Tạo SNS topic `autoschedule-report` và xác nhận email subscription | Nguyễn Văn Thi | AWS SNS Console | [week2-evidence-02-sns-confirmed.png](../docs/screenshots/week2-evidence-02-sns-confirmed.png) (Hình 2: Trạng thái Confirmed) |
| Cấu hình tag ban đầu cho RDS (`Schedule=08:00-17:00`, `ScheduleDays=Mon-Sun`) | Nguyễn Văn Thi | AWS RDS Console | [week2-evidence-09-rds-stopped.png](../docs/screenshots/week2-evidence-09-rds-stopped.png) · [week2-evidence-10-rds-tags.png](../docs/screenshots/week2-evidence-10-rds-tags.png) |
| Cấu hình tag ban đầu cho SageMaker Notebook (`ScheduleDays=Mon-Fri`) | Nguyễn Văn Thi | AWS SageMaker Console | [week2-evidence-11-sagemaker-stopped.png](../docs/screenshots/week2-evidence-11-sagemaker-stopped.png) · [week2-evidence-12-sagemaker-tags.png](../docs/screenshots/week2-evidence-12-sagemaker-tags.png) |
| Test START SageMaker trong giờ: trạng thái Pending $\rightarrow$ InService (INT-06) | Nguyễn Văn Thi | SageMaker Console | [week2-evidence-15-sagemaker-pending.png](../docs/screenshots/week2-evidence-15-sagemaker-pending.png) · [week2-evidence-16-sagemaker-inservice.png](../docs/screenshots/week2-evidence-16-sagemaker-inservice.png) |
| Test START RDS trong giờ: trạng thái Starting $\rightarrow$ Available (INT-04) | Nguyễn Văn Thi | RDS Console | [week2-evidence-17-rds-starting.png](../docs/screenshots/week2-evidence-17-rds-starting.png) · [week2-evidence-18-rds-available.png](../docs/screenshots/week2-evidence-18-rds-available.png) |
| Test bỏ qua tài nguyên đang chuyển trạng thái (Actions: []) | Nguyễn Văn Thi | CloudWatch Logs / Lambda Console | [week2-evidence-19-enforce-in-progress-skip.png](../docs/screenshots/week2-evidence-19-enforce-in-progress-skip.png) (Hình 19 trong báo cáo) |
| Test STOP RDS ngoài khung giờ: trạng thái chuyển Stopping (INT-03) | Nguyễn Văn Thi | RDS Console | [week2-evidence-22-rds-stopping.png](../docs/screenshots/week2-evidence-22-rds-stopping.png) (Hình 22 trong báo cáo) |
| Test STOP SageMaker ngoài khung giờ: trạng thái Stopped (INT-05) | Nguyễn Văn Thi | SageMaker Console | [week2-evidence-23-sagemaker-stopped.png](../docs/screenshots/week2-evidence-23-sagemaker-stopped.png) (Hình 23 trong báo cáo) |
| Kiểm thử START/STOP EC2 qua đổi tag (INT-01, INT-02) | Nguyễn Văn Trung | EC2 Console / CloudWatch Logs | [Hình 7](../docs/screenshots/week2-evidence-07-ec2-stopped.png) · [Hình 8](../docs/screenshots/week2-evidence-08-ec2-tags.png) · [Hình 13](../docs/screenshots/week2-evidence-13-enforce-start-log.png) · [Hình 14](../docs/screenshots/week2-evidence-14-ec2-running.png) · [Hình 20](../docs/screenshots/week2-evidence-20-enforce-stop-log.png) · [Hình 21](../docs/screenshots/week2-evidence-21-ec2-stopped-after-enforce.png) |
| Kiểm thử tag sai định dạng, tag `off`, không tag (INT-07, INT-08) | Nguyễn Văn Trung | EC2 Console / CloudWatch Logs | [Hình 24](../docs/screenshots/week2-evidence-24-ec2-tag-schedule-abc.png) · [Hình 25](../docs/screenshots/week2-evidence-25-enforce-invalid-tag-result.png) · [Hình 26](../docs/screenshots/week2-evidence-26-cloudwatch-invalid-schedule-tag.png) · [Hình 27](../docs/screenshots/week2-evidence-27-ec2-tag-schedule-removed.png) · [Hình 28](../docs/screenshots/week2-evidence-28-enforce-no-schedule-tag-skip.png) · [Hình 29](../docs/screenshots/week2-evidence-29-ec2-running-schedule-off.png) · [Hình 30](../docs/screenshots/week2-evidence-30-enforce-schedule-off-stop.png) · [Hình 31](../docs/screenshots/week2-evidence-31-ec2-stopped-schedule-off.png) |
| Kiểm thử gửi báo cáo qua SNS với event `{"action":"report"}` (INT-09) | Cả hai | Lambda / AWS SNS / Gmail | [Hình 3](../docs/screenshots/week2-evidence-03-report-test-event.png) · [Hình 32](../docs/screenshots/week2-evidence-32-run-report-event.png) · [Hình 33](../docs/screenshots/week2-evidence-33-report-result.png) · [Hình 34](../docs/screenshots/week2-evidence-34-report-email.png) (Email nhận lúc 16:52) |
| Soạn thảo, hoàn thiện báo cáo và đồng bộ Git Tuần 2 | Cả hai | [worklog/week2.md](week2.md) | Hoàn thành và cập nhật trên nhánh `main` |

---

## 5. Khai báo sử dụng AI (Tiêu chí 7)

Trong Tuần 2, nhóm sử dụng **Claude** với mục đích hỗ trợ kỹ thuật và quy trình kiểm thử theo đúng quy định minh bạch của môn học:

| Tên công cụ AI | Mục đích sử dụng | Công việc sinh viên tự thực hiện (kiểm chứng & sửa đổi) | Link commit minh chứng |
|---|---|---|---|
| **Claude** | Tham khảo cú pháp và hoàn thiện các ca kiểm thử pytest cho hàm `desired_running()` bao phủ các trường hợp biên (lịch qua đêm, đổi múi giờ ICT). | Sinh viên Nguyễn Văn Thi tự đọc hiểu thuật toán, tự viết code kiểm thử, chạy trực tiếp `pytest` trên môi trường thực tế đạt 11/11 passed và bổ sung docstring giải thích. | [Commit c90a945](https://github.com/nguyentrung01ute-ui/autoschedule/commit/c90a9459bcdbbfb20c0471f9081164f22fec1a43) |
| **Claude** | Tham khảo quy trình kiểm thử tích hợp bật/tắt RDS, SageMaker và kịch bản bắt sự kiện đang chuyển trạng thái (`Starting`, `Pending`). | Sinh viên Nguyễn Văn Thi tự thao tác trên AWS Learner Lab, đổi tag thực tế, gọi test event enforce trên Lambda console, theo dõi quá trình chuyển trạng thái và thu thập ảnh minh chứng. | [Commit 9f54fe9](https://github.com/nguyentrung01ute-ui/autoschedule/commit/9f54fe9d21a7c0304917d16fc189fd7e26522d5e) |
| **Claude** | Hỗ trợ cấu trúc dàn ý bảng kết quả kiểm thử (INT-01 đến INT-09) và các lưu ý kỹ thuật khi stop RDS/SageMaker. | Sinh viên tự đối chiếu kết quả thực tế từ CloudWatch Logs, ghi nhận thời gian thực hiện chính xác và biên tập nội dung vào báo cáo Word/Markdown. | [Commit c90a945](https://github.com/nguyentrung01ute-ui/autoschedule/commit/c90a9459bcdbbfb20c0471f9081164f22fec1a43) |

---

## 6. Tổng hợp thời lượng Tuần 2

| Thành viên | MSSV | Vai trò | Tổng thời gian |
|---|---|---|---:|
| **Nguyễn Văn Thi** | 24110334 | Thành viên (DevOps & IaC) | **8 giờ 37 phút** |
| **Nguyễn Văn Trung** | 24110365 | Nhóm trưởng (DevOps & IaC) | **8 giờ 40 phút** |
| **Tổng cộng cả nhóm** | | | **17 giờ 17 phút** |

*Cả hai thành viên đều đáp ứng và vượt mức thời lượng tối thiểu 8 giờ/tuần theo quy định của đồ án.*

---

## 7. Tài liệu Tuần 2 liên quan

- [Kế hoạch dự án tổng thể](../PROJECT_PLAN.md)
- [Mã nguồn kiểm thử tự động pytest](../tests/test_schedule.py)
- [Mã nguồn xử lý Lambda core](../src/scheduler.py)
- [Thư mục ảnh minh chứng thực tế](../docs/screenshots/)
- [Báo cáo Tuần 1](../worklog/week1.md)
