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
| **Nguyễn Văn Trung (24110365)** | - **Phát triển AWS Lambda core**: Phân tích hàm `desired_running()`, hoàn thiện logic điều khiển tài nguyên trên Lambda và xử lý timezone.<br>- **Tạo Lambda thủ công & cấu hình**: Tạo function trên AWS Console với cấu hình runtime Python 3.12, role `LabRole`, memory 128 MB, timeout 120s và biến môi trường.<br>- **Kiểm thử EC2 & báo cáo SNS**: Kiểm thử START/STOP EC2 qua tag, test trường hợp tag sai định dạng, tag `off`, không tag Schedule và test nhận email báo cáo SNS.<br>- **Soạn thảo và định dạng báo cáo Word**: Tổng hợp nội dung chung, sắp xếp hình ảnh minh chứng và rà soát báo cáo trước khi nộp. | **8 giờ 40 phút** | • [src/scheduler.py](../src/scheduler.py)<br>• [tests/events/enforce.json](../tests/events/enforce.json)<br>• [tests/events/report.json](../tests/events/report.json) | • [Commit e91853a](https://github.com/nguyentrung01ute-ui/autoschedule/commit/e91853a7d54a3fbf44324e8625db8b3738afe856): `fix: harden scheduler logic and pagination`.<br>• [Báo cáo Word Tuần 2](../reports/Bao_cao_tuan2_Nhom_DevOps_IaC.docx) và [danh mục minh chứng](../docs/week2-evidence.md) là các sản phẩm tài liệu liên quan. |
| **Cả hai thành viên** | Phối hợp chạy kiểm thử tích hợp end-to-end trên AWS Learner Lab, xác minh log CloudWatch đối chiếu với console, rà soát kết quả kiểm thử và hoàn thiện hồ sơ báo cáo. | Đã tính trong tổng giờ | [Kế hoạch](../PROJECT_PLAN.md) · [Scheduler](../src/scheduler.py) · [Báo cáo Tuần 2](week2.md) | Phối hợp đồng bộ kết quả trên nhánh chính `main`. |

---

## 4. Nhật ký công việc và liên kết kiểm chứng thực tế

Mục này tách từng đầu việc thành dòng riêng để dễ đối chiếu giữa **nhiệm vụ – mã nguồn/tài liệu – minh chứng**. Các liên kết file là nơi kiểm tra sản phẩm hiện có; ảnh AWS chứng minh thao tác/kết quả thực tế. Việc ghi nhận phối hợp không có nghĩa một thành viên làm thay toàn bộ phần việc của người còn lại.

| Hạng mục công việc | Người phụ trách | File kiểm tra / mã kiểm thử / sản phẩm | Trạng thái & liên kết kiểm chứng |
|---|---|---|---|
| Chạy pytest kiểm thử logic hàm `desired_running()` (11 tests passed) | Nguyễn Văn Thi | [tests/test_schedule.py](../tests/test_schedule.py) | [Ảnh pytest 11 passed](../docs/screenshots/week2-evidence-01-pytest-11-passed.png) |
| Tạo SNS topic `autoschedule-report` và xác nhận email subscription | Nguyễn Văn Thi | AWS SNS Console | [Ảnh SNS subscription Confirmed](../docs/screenshots/week2-evidence-02-sns-confirmed.png) |
| Cấu hình tag ban đầu cho RDS (`Schedule=08:00-17:00`, `ScheduleDays=Mon-Sun`) | Nguyễn Văn Thi | AWS RDS Console | [Ảnh trạng thái RDS](../docs/screenshots/week2-evidence-09-rds-stopped.png) · [Ảnh tag RDS](../docs/screenshots/week2-evidence-10-rds-tags.png) |
| Cấu hình tag ban đầu cho SageMaker Notebook (`ScheduleDays=Mon-Fri`) | Nguyễn Văn Thi | AWS SageMaker Console | [Ảnh trạng thái SageMaker](../docs/screenshots/week2-evidence-11-sagemaker-stopped.png) · [Ảnh tag SageMaker](../docs/screenshots/week2-evidence-12-sagemaker-tags.png) |
| Test START SageMaker trong giờ: Pending → InService (INT-06) | Nguyễn Văn Thi | SageMaker Console | [Ảnh Pending](../docs/screenshots/week2-evidence-15-sagemaker-pending.png) · [Ảnh InService](../docs/screenshots/week2-evidence-16-sagemaker-inservice.png) |
| Test START RDS trong giờ: Starting → Available (INT-04) | Nguyễn Văn Thi | RDS Console | [Ảnh Starting](../docs/screenshots/week2-evidence-17-rds-starting.png) · [Ảnh Available](../docs/screenshots/week2-evidence-18-rds-available.png) |
| Test bỏ qua tài nguyên đang chuyển trạng thái (Actions: `[]`) | Nguyễn Văn Thi | CloudWatch Logs / Lambda Console | [Ảnh log bỏ qua tài nguyên đang chuyển trạng thái](../docs/screenshots/week2-evidence-19-enforce-in-progress-skip.png) |
| Test STOP RDS ngoài khung giờ (INT-03) | Nguyễn Văn Thi | RDS Console | [Ảnh RDS chuyển Stopping](../docs/screenshots/week2-evidence-22-rds-stopping.png) |
| Test STOP SageMaker ngoài khung giờ (INT-05) | Nguyễn Văn Thi | SageMaker Console | [Ảnh SageMaker Stopped](../docs/screenshots/week2-evidence-23-sagemaker-stopped.png) |
| Phát triển và rà soát phần xử lý AWS Lambda: điều phối `enforce`, thu thập tài nguyên và gửi báo cáo `report` | Nguyễn Văn Trung | [src/scheduler.py](../src/scheduler.py) | [Event enforce](../tests/events/enforce.json) · [Event report](../tests/events/report.json) · [Cấu hình Lambda](../docs/screenshots/week2-evidence-05-lambda-general-config.png) · [Biến môi trường Lambda](../docs/screenshots/week2-evidence-06-lambda-env-vars.png) |
| Phân tích logic hàm `desired_running()`: kiểm tra Project/Schedule, `off`, lịch hợp lệ và lịch qua đêm | Nguyễn Văn Trung | [Hàm desired_running trong scheduler.py](../src/scheduler.py) | [Mã nguồn scheduler](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/src/scheduler.py) · [Kết quả kiểm thử lịch](../docs/screenshots/week2-evidence-01-pytest-11-passed.png). Ảnh pytest thuộc phần kiểm thử do Nguyễn Văn Thi chạy; không quy kết kết quả pytest cho riêng Trung. |
| Thiết kế/đối chiếu các tình huống kiểm thử tích hợp cho lịch chạy và trường hợp biên | Nguyễn Văn Trung | [Kế hoạch kiểm thử](../docs/test-plan.md) · [Event enforce](../tests/events/enforce.json) | Các tình huống thực tế: [Schedule sai định dạng](../docs/screenshots/week2-evidence-24-ec2-tag-schedule-abc.png) · [Log tag không hợp lệ](../docs/screenshots/week2-evidence-26-cloudwatch-invalid-schedule-tag.png) · [Thiếu Schedule](../docs/screenshots/week2-evidence-28-enforce-no-schedule-tag-skip.png) · [Schedule=off](../docs/screenshots/week2-evidence-30-enforce-schedule-off-stop.png) |
| Kiểm thử START/STOP EC2 theo lịch trong/ngoài giờ (INT-01, INT-02) | Nguyễn Văn Trung | EC2 Console / CloudWatch Logs | [EC2 stopped ban đầu](../docs/screenshots/week2-evidence-07-ec2-stopped.png) · [Tag EC2](../docs/screenshots/week2-evidence-08-ec2-tags.png) · [Log START](../docs/screenshots/week2-evidence-13-enforce-start-log.png) · [EC2 Running](../docs/screenshots/week2-evidence-14-ec2-running.png) · [Log STOP](../docs/screenshots/week2-evidence-20-enforce-stop-log.png) · [EC2 Stopped sau enforce](../docs/screenshots/week2-evidence-21-ec2-stopped-after-enforce.png) |
| Kiểm thử trường hợp biên: Schedule sai định dạng, thiếu tag Schedule và `Schedule=off` (INT-07, INT-08 và tình huống off) | Nguyễn Văn Trung | EC2 Console / CloudWatch Logs | [Tag abc](../docs/screenshots/week2-evidence-24-ec2-tag-schedule-abc.png) · [Kết quả tag sai](../docs/screenshots/week2-evidence-25-enforce-invalid-tag-result.png) · [Log invalid tag](../docs/screenshots/week2-evidence-26-cloudwatch-invalid-schedule-tag.png) · [Gỡ tag Schedule](../docs/screenshots/week2-evidence-27-ec2-tag-schedule-removed.png) · [Bỏ qua khi thiếu tag](../docs/screenshots/week2-evidence-28-enforce-no-schedule-tag-skip.png) · [EC2 với Schedule=off](../docs/screenshots/week2-evidence-29-ec2-running-schedule-off.png) · [Lệnh STOP](../docs/screenshots/week2-evidence-30-enforce-schedule-off-stop.png) · [Trạng thái Stopped](../docs/screenshots/week2-evidence-31-ec2-stopped-schedule-off.png) |
| Tạo AWS Lambda function trên AWS Console và cấu hình runtime Python 3.12, role `LabRole`, memory, timeout và biến môi trường | Nguyễn Văn Trung | [Mã nguồn Lambda](../src/scheduler.py) | [Cấu hình chung Lambda](../docs/screenshots/week2-evidence-05-lambda-general-config.png) · [Biến môi trường Lambda](../docs/screenshots/week2-evidence-06-lambda-env-vars.png) |\n| Kiểm thử Lambda gửi báo cáo tài nguyên qua SNS (INT-09) | Nguyễn Văn Trung | [Event report](../tests/events/report.json) · [Mã nguồn report](../src/scheduler.py) | [Test event report](../docs/screenshots/week2-evidence-03-report-test-event.png) · [Chạy report](../docs/screenshots/week2-evidence-32-run-report-event.png) · [Kết quả Lambda](../docs/screenshots/week2-evidence-33-report-result.png) · [Email nhận từ SNS](../docs/screenshots/week2-evidence-34-report-email.png) |
| Quản lý mã nguồn, theo dõi commit và đồng bộ thay đổi lên GitHub | Nguyễn Văn Trung | [Lịch sử commit của scheduler.py](https://github.com/nguyentrung01ute-ui/autoschedule/commits/main/src/scheduler.py) · [Lịch sử commit toàn repo](https://github.com/nguyentrung01ute-ui/autoschedule/commits/main) | [Commit harden scheduler logic and pagination](https://github.com/nguyentrung01ute-ui/autoschedule/commit/e91853a7d54a3fbf44324e8625db8b3738afe856). Liên kết thể hiện lịch sử mã nguồn; chỉ dùng làm bằng chứng phần Trung khi xác nhận đúng tài khoản/commit mình thực hiện. |
| Soạn thảo/định dạng báo cáo Word và tổng hợp nội dung chung | Nguyễn Văn Trung | [Báo cáo Tuần 2 (.docx)](../reports/Bao_cao_tuan2_Nhom_DevOps_IaC.docx) | [Danh mục minh chứng Tuần 2](../docs/week2-evidence.md) · [Thư mục ảnh](../docs/screenshots/) |
| Thu thập, đặt tên và sắp xếp ảnh minh chứng để dễ đối chiếu với báo cáo | Nguyễn Văn Trung | [Danh mục minh chứng Tuần 2](../docs/week2-evidence.md) | [Thư mục ảnh minh chứng](../docs/screenshots/) · [README thư mục ảnh](../docs/screenshots/README.md) |
| Phối hợp rà soát nội dung, kết quả kiểm thử và liên kết trước khi nộp | Cả hai | [Worklog Tuần 2](week2.md) · [Báo cáo Word Tuần 2](../reports/Bao_cao_tuan2_Nhom_DevOps_IaC.docx) | Đối chiếu bảng kết quả kiểm thử với [34 ảnh minh chứng Tuần 2](../docs/week2-evidence.md); trạng thái cuối cùng cần được cả hai thành viên xác nhận. |

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
