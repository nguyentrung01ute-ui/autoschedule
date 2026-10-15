# Worklog tuần 1 — AutoSchedule

## 1. Thông tin chung

- **Nhóm:** DevOps & IaC
- **Dự án:** AutoSchedule — tự động bật/tắt tài nguyên AWS theo lịch học
- **Môi trường:** AWS Learner Lab, Region `us-east-1` (dùng IAM role có sẵn `LabRole`)
- **Thành viên:** 
  - Nguyễn Văn Trung (MSSV: 24110365)
  - Nguyễn Văn Thi (MSSV: 24110334)
- **Tổng thời lượng đã ghi nhận:** 16 giờ 50 phút
- **Trạng thái minh chứng:** Đã ghi nhận 16 ảnh minh chứng (`week1-evidence-01.png` đến `week1-evidence-16-account-region.png`) trong thư mục `docs/screenshots/` và được liên kết tại [danh mục minh chứng](../docs/week1-evidence.md).

---

## 2. Liên kết Mã Nguồn và Template Dự Án (Tiêu chí 3)

Để đáp ứng đầy đủ yêu cầu minh chứng mã nguồn trực tiếp (Tiêu chí 3), toàn bộ các file mã nguồn phát triển và template triển khai được liên kết dưới đây:

| Hạng mục mã nguồn | File trong repo | Link trực tiếp trên GitHub | Mô tả tóm tắt |
|---|---|---|---|
| **Mã nguồn Lambda chính** | `src/scheduler.py` | [src/scheduler.py](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/src/scheduler.py) | Hàm Lambda Python 3.12 xử lý quét tag, so khớp lịch UTC sang `Asia/Ho_Chi_Minh`, gọi API bật/tắt EC2/RDS/SageMaker và gửi báo cáo SNS. |
| **Hạ tầng dưới dạng mã (IaC)** | `infra/template.yaml` | [infra/template.yaml](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/infra/template.yaml) | CloudFormation template đóng gói Lambda, EventBridge rules, SNS topic, CloudWatch log group và Alarm. |
| **Kiểm thử tự động** | `tests/test_schedule.py` | [tests/test_schedule.py](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/tests/test_schedule.py) | Unit tests với pytest kiểm tra logic hàm tính lịch `desired_running()` (khung giờ thường, qua đêm, ngày trong tuần). |
| **Sự kiện kiểm thử mẫu** | `tests/events/enforce.json` | [tests/events/enforce.json](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/tests/events/enforce.json) | Event payload mô phỏng EventBridge gọi kiểm tra lịch bật/tắt tài nguyên. |
| **Sự kiện báo cáo mẫu** | `tests/events/report.json` | [tests/events/report.json](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/tests/events/report.json) | Event payload mô phỏng EventBridge gọi tạo báo cáo gửi qua SNS. |
| **Cấu hình môi trường** | `scripts/config.sh` | [scripts/config.sh](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/scripts/config.sh) | Định nghĩa biến môi trường chung (`PROJECT`, `OWNER`, `SCHEDULE`, `LAB_ROLE_ARN`). |
| **Script khởi tạo S3** | `scripts/01_setup_s3.sh` | [scripts/01_setup_s3.sh](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/scripts/01_setup_s3.sh) | Tạo S3 bucket lưu trữ deployment package, kích hoạt Block Public Access và SSE-S3. |
| **Script khởi tạo EC2** | `scripts/02_create_ec2.sh` | [scripts/02_create_ec2.sh](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/scripts/02_create_ec2.sh) | Tạo EC2 `t3.nano` mẫu, phân vùng EBS 8 GiB gp3 và gắn 4 tag chuẩn. |
| **Script khởi tạo RDS** | `scripts/03_create_rds.sh` | [scripts/03_create_rds.sh](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/scripts/03_create_rds.sh) | Tạo RDS MySQL `db.t3.micro`, 20 GiB gp3, Single-AZ, non-public và gắn 4 tag chuẩn. |
| **Script khởi tạo SageMaker** | `scripts/04_create_sagemaker.sh` | [scripts/04_create_sagemaker.sh](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/scripts/04_create_sagemaker.sh) | Tạo SageMaker Notebook `ml.t3.medium`, ổ đĩa 5 GB, gán IAM Role `LabRole` và gắn 4 tag chuẩn. |
| **Script kiểm tra trạng thái** | `scripts/05_status.sh` | [scripts/05_status.sh](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/scripts/05_status.sh) | Liệt kê nhanh trạng thái và tag của toàn bộ tài nguyên phục vụ kiểm tra. |

---

## 3. Phân công, Kết quả và Commit Minh Chứng Phát Triển (Tiêu chí 6)

| Thành viên | Nhiệm vụ cụ thể | Thời lượng | Link file mã nguồn / tài liệu liên quan | Link Commit minh chứng công việc phát triển |
|---|---|---:|---|---|
| **Nguyễn Văn Thi (24110334)** | - **Thiết kế kiến trúc hệ thống**: Xây dựng tài liệu kiến trúc, phân tích 2 luồng Enforce & Report, cơ chế timezone UTC sang ICT, quy ước tag và ràng buộc Learner Lab.<br>- **Xây dựng tài liệu runbook**: Soạn thảo quy trình thực hành tuần 1, pre-flight check, hướng dẫn tạo tài nguyên, verify `LabRole` và checklist dọn dẹp.<br>- **Chuẩn bị tài nguyên RDS & SageMaker**: Viết và chuẩn hóa script tạo RDS MySQL (`03_create_rds.sh`) và SageMaker Notebook (`04_create_sagemaker.sh`). | **8 giờ 20 phút** | • [docs/architecture.md](../docs/architecture.md)<br>• [docs/week1-runbook.md](../docs/week1-runbook.md)<br>• [scripts/03_create_rds.sh](../scripts/03_create_rds.sh)<br>• [scripts/04_create_sagemaker.sh](../scripts/04_create_sagemaker.sh)<br>• [src/scheduler.py](../src/scheduler.py) | • [Commit 1fd8d61](https://github.com/nguyentrung01ute-ui/autoschedule/commit/1fd8d61): Hoàn thiện thiết kế kiến trúc và luồng EventBridge.<br>• [Commit 68cce06](https://github.com/nguyentrung01ute-ui/autoschedule/commit/68cce06): Xây dựng runbook vận hành và quy trình kiểm thử Tuần 1.<br>• [Commit 8bbadaa](https://github.com/nguyentrung01ute-ui/autoschedule/commit/8bbadaa): Chuẩn hóa script tạo và cấu hình RDS, SageMaker. |
| **Nguyễn Văn Trung (24110365)** | - **Khởi tạo repository và tài liệu kế hoạch**: Xây dựng cấu trúc thư mục, `PROJECT_PLAN.md`, cấu hình CI/CD.<br>- **Chuẩn bị tài nguyên S3 & EC2**: Viết script tạo S3 bucket (`01_setup_s3.sh`), EC2 instance (`02_create_ec2.sh`) và script kiểm tra (`05_status.sh`).<br>- **Phát triển mã nguồn Lambda & CloudFormation**: Hoàn thiện logic hàm Lambda (`scheduler.py`) và CloudFormation template (`template.yaml`). | **8 giờ 30 phút** | • [PROJECT_PLAN.md](../PROJECT_PLAN.md)<br>• [scripts/config.sh](../scripts/config.sh)<br>• [scripts/01_setup_s3.sh](../scripts/01_setup_s3.sh)<br>• [scripts/02_create_ec2.sh](../scripts/02_create_ec2.sh)<br>• [src/scheduler.py](../src/scheduler.py)<br>• [infra/template.yaml](../infra/template.yaml) | • [Commit af6090b](https://github.com/nguyentrung01ute-ui/autoschedule/commit/af6090b): Khởi tạo project, Lambda, CloudFormation và kế hoạch.<br>• [Commit 2debfac](https://github.com/nguyentrung01ute-ui/autoschedule/commit/2debfac): Củng cố CloudFormation deployment và xử lý quyền.<br>• [Commit e91853a](https://github.com/nguyentrung01ute-ui/autoschedule/commit/e91853a): Tối ưu logic scheduler và phân trang API. |
| **Cả hai thành viên** | Cùng tìm hiểu EventBridge, boto3 và giới hạn AWS Learner Lab; rà soát trạng thái tài nguyên, worklog và các yêu cầu minh chứng. | Đã tính trong tổng giờ | [Kế hoạch](../PROJECT_PLAN.md) · [Runbook](../docs/week1-runbook.md) · [Status script](../scripts/05_status.sh) | [Commit ce66c72](https://github.com/nguyentrung01ute-ui/autoschedule/commit/ce66c72): Đồng bộ kiến trúc với hành vi thực tế của scheduler. |

---

## 4. Nhật ký công việc và liên kết kiểm chứng thực tế

| Hạng mục | Người phụ trách | File kiểm tra | Trạng thái minh chứng |
|---|---|---|---|
| Chuẩn bị repository, cấu hình môi trường và quy ước tag | Nguyễn Văn Trung | [PROJECT_PLAN.md](../PROJECT_PLAN.md) · [scripts/config.sh](../scripts/config.sh) | File kế hoạch và script có trên GitHub; kiểm tra log khởi tạo. |
| Tạo và cấu hình S3 (tag, Block Public Access, mã hóa SSE-S3) | Nguyễn Văn Trung | [scripts/01_setup_s3.sh](../scripts/01_setup_s3.sh) | [Ảnh S3 Block Public Access — evidence-04](../docs/screenshots/week1-evidence-04.png) · [Ảnh S3 tags và mã hóa — evidence-05](../docs/screenshots/week1-evidence-05.png) |
| Tạo EC2 mẫu và gắn tag | Nguyễn Văn Trung | [scripts/02_create_ec2.sh](../scripts/02_create_ec2.sh) | [Ảnh EC2 Running — evidence-06](../docs/screenshots/week1-evidence-06.png) · [Ảnh EC2 tags — evidence-07](../docs/screenshots/week1-evidence-07.png) · [Ảnh EBS tags — evidence-08](../docs/screenshots/week1-evidence-08.png) |
| Tạo RDS MySQL mẫu | Nguyễn Văn Thi | [scripts/03_create_rds.sh](../scripts/03_create_rds.sh) | [Ảnh RDS Available — evidence-09](../docs/screenshots/week1-evidence-09.png) · [Ảnh RDS configuration — evidence-10](../docs/screenshots/week1-evidence-10.png) · [Ảnh RDS tags — evidence-11](../docs/screenshots/week1-evidence-11.png) |
| Tạo SageMaker Notebook mẫu dùng LabRole | Nguyễn Văn Thi | [scripts/04_create_sagemaker.sh](../scripts/04_create_sagemaker.sh) · [Yêu cầu IAM](../docs/iam-requirements.md) | [Ảnh SageMaker InService — evidence-12](../docs/screenshots/week1-evidence-12.png) · [Ảnh SageMaker tags — evidence-13](../docs/screenshots/week1-evidence-13.png) · [Ảnh execution role LabRole — evidence-15](../docs/screenshots/week1-evidence-15-sagemaker-execution-role.png) |
| Thiết kế kiến trúc và luồng xử lý EventBridge | Nguyễn Văn Thi | [docs/architecture.md](../docs/architecture.md) | [Ảnh sơ đồ kiến trúc — evidence-01](../docs/screenshots/week1-evidence-01.png) · [Ảnh sơ đồ hạ tầng](../docs/screenshots/autoschedule-infrastructure.png) |
| Xây dựng tài liệu runbook vận hành | Nguyễn Văn Thi | [docs/week1-runbook.md](../docs/week1-runbook.md) | Đã cập nhật chi tiết các bước thực hiện và checklist vận hành trên Learner Lab. |
| Kiểm tra Account ID, Region và trạng thái tài nguyên | Cả hai | [scripts/05_status.sh](../scripts/05_status.sh) | [Ảnh khởi động Learner Lab — evidence-02](../docs/screenshots/week1-evidence-02.png) · [Ảnh Account ID và Region — evidence-16](../docs/screenshots/week1-evidence-16-account-region.png) |
| Kiểm tra tài nguyên còn sót (EBS, Snapshots) | Cả hai | [scripts/05_status.sh](../scripts/05_status.sh) | [Ảnh kiểm tra EC2/EBS — evidence-14](../docs/screenshots/week1-evidence-14.png) |

---

## 5. Khai báo sử dụng AI (Tiêu chí 7)

Trong tuần 1, nhóm sử dụng **Claude (bản thông thường; chưa xác nhận model/version cụ thể)** để hỗ trợ tham khảo, tổ chức và diễn đạt tài liệu dự án. Bảng dưới đây ghi rõ mục đích sử dụng và phần sinh viên tự rà soát, chỉnh sửa. Không ghi thêm công cụ hoặc phiên bản AI chưa được xác nhận.

| Tên công cụ AI | Mục đích sử dụng | Công việc sinh viên tự thực hiện (kiểm chứng & sửa đổi) | Link commit minh chứng |
|---|---|---|---|
| **Claude (bản thông thường; chưa xác nhận model/version cụ thể)** | Hỗ trợ tham khảo cấu trúc tài liệu kiến trúc và cách trình bày luồng phối hợp giữa EventBridge, Lambda và SNS. | Sinh viên tự đối chiếu nội dung với mục tiêu dự án và giới hạn AWS Learner Lab, sau đó rà soát và chỉnh sửa tài liệu kiến trúc trong repository. | [Commit 1fd8d61](https://github.com/nguyentrung01ute-ui/autoschedule/commit/1fd8d61db48a09362c802cdfe4efa5b47d433d2b) |
| **Claude (bản thông thường; chưa xác nhận model/version cụ thể)** | Hỗ trợ tham khảo cách tổ chức Runbook Tuần 1 và checklist kiểm tra tài nguyên. | Sinh viên tự rà soát, chỉnh sửa các bước hướng dẫn và đối chiếu các thao tác AWS với ảnh minh chứng thực tế có trong repository; không xem một thao tác là đã hoàn tất nếu chưa có bằng chứng. | [Commit 68cce06](https://github.com/nguyentrung01ute-ui/autoschedule/commit/68cce0684e522a4c18b7327ffb363c28b78a8cc2) |
| **Claude (bản thông thường; chưa xác nhận model/version cụ thể)** | Hỗ trợ tham khảo cách diễn đạt logic lập lịch và xử lý múi giờ trong tài liệu/mã nguồn scheduler. | Sinh viên tự đọc và rà soát mã nguồn, chỉnh sửa theo yêu cầu dự án; chỉ ghi nhận việc kiểm thử hoặc triển khai là hoàn tất khi có kết quả kiểm chứng tương ứng. | [Commit scheduler](https://github.com/nguyentrung01ute-ui/autoschedule/commit/e91853a) |

**Lưu ý:** Chỉ thay tên công cụ thành một phiên bản cụ thể (ví dụ Claude 3.5 Sonnet hoặc ChatGPT GPT-4o) nếu nhóm xác nhận thực sự đã sử dụng phiên bản đó. Các mô tả về việc chạy lệnh, tạo tài nguyên hoặc kiểm thử cũng cần khớp với công việc thực tế và minh chứng của nhóm.

---

## 6. Tổng hợp thời lượng

| Thành viên | Tổng thời gian |
|---|---:|
| Nguyễn Văn Trung (MSSV: 24110365) | 8 giờ 30 phút |
| Nguyễn Văn Thi (MSSV: 24110334) | 8 giờ 20 phút |
| **Tổng nhóm** | **16 giờ 50 phút** |

---

## 7. Tài liệu Tuần 1 liên quan

- [Kế hoạch dự án và phân công ban đầu](../PROJECT_PLAN.md)
- [Runbook Tuần 1](../docs/week1-runbook.md)
- [Danh mục minh chứng Tuần 1](../docs/week1-evidence.md)
- [Sơ đồ/ghi chú kiến trúc](../docs/architecture.md)
- [Khai báo sử dụng AI chi tiết](../docs/ai-disclosure-week1.md)
- [Script kiểm tra trạng thái AWS](../scripts/05_status.sh)
