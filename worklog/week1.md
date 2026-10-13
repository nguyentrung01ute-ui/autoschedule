# Worklog tuần 1 — AutoSchedule

## 1. Thông tin chung

- **Nhóm:** DevOps & IaC
- **Dự án:** AutoSchedule — tự động bật/tắt tài nguyên AWS theo lịch
- **Môi trường dự kiến:** AWS Learner Lab, Region `us-east-1` (có thể dùng `us-west-2` theo quy định lab)
- **Thành viên:** Nguyễn Văn Trung (24110365), Nguyễn Văn Thi (24110334)
- **Tổng thời lượng đã ghi nhận:** 16 giờ 50 phút
- **Ngày thực hiện:** Chưa xác nhận được ngày cụ thể cho từng công việc. Cần đối chiếu lịch làm việc thực tế trước khi nộp; không lấy ngày commit thay cho ngày thực hành.
- **Trạng thái minh chứng:** Đã xác nhận trên GitHub có 14 ảnh `week1-evidence-01.png` đến `week1-evidence-14.png` trong `docs/screenshots/`. Các link ảnh được liệt kê tại mục 3 và [danh mục minh chứng](../docs/week1-evidence.md). Việc ảnh tồn tại không tự động chứng minh mọi thông tin trong ảnh đều đủ rõ; cần đối chiếu nội dung ảnh trước khi nộp.

## 2. Phân công và kết quả theo thành viên

| Thành viên | Công việc được ghi nhận | Thời lượng | Link file-level liên quan |
|---|---|---:|---|
| **Nguyễn Văn Trung (24110365)** | Chuẩn bị repository và cấu trúc làm việc; thực hành tạo/cấu hình S3; thực hành tạo EC2 mẫu; tìm hiểu tài liệu AWS và kiến trúc. | **8 giờ 30 phút** | [Cấu hình chung](../scripts/config.sh) · [Tạo S3](../scripts/01_setup_s3.sh) · [Tạo EC2](../scripts/02_create_ec2.sh) · [Kiến trúc](../docs/architecture.md) |
| **Nguyễn Văn Thi (24110334)** | Thực hành tạo RDS MySQL và SageMaker Notebook mẫu; phối hợp chuẩn bị sơ đồ kiến trúc; tìm hiểu tài liệu AWS. | **8 giờ 20 phút** | [Tạo RDS](../scripts/03_create_rds.sh) · [Tạo SageMaker Notebook](../scripts/04_create_sagemaker.sh) · [Kiến trúc](../docs/architecture.md) |
| **Cả hai thành viên** | Cùng tìm hiểu EventBridge, boto3 và giới hạn AWS Learner Lab; rà soát trạng thái tài nguyên, worklog và các yêu cầu minh chứng. Phân chia chi tiết theo buổi cần được xác nhận với nhật ký thực tế. | Đã tính trong tổng giờ của từng thành viên; không cộng thêm lần nữa. | [Kế hoạch dự án và phân công Tuần 1](../PROJECT_PLAN.md) · [Runbook Tuần 1](../docs/week1-runbook.md) · [Lệnh kiểm tra trạng thái](../scripts/05_status.sh) |


## 3. Nhật ký công việc và liên kết kiểm chứng

| Hạng mục | Người phụ trách theo ghi nhận hiện tại | File/nguồn kiểm tra | Trạng thái minh chứng |
|---|---|---|---|
| Chuẩn bị repository, cấu hình môi trường và quy ước tag | Nguyễn Văn Trung | [PROJECT_PLAN.md](../PROJECT_PLAN.md) · [scripts/config.sh](../scripts/config.sh) | File kế hoạch và script có trên GitHub; cần ảnh/log thực tế để xác minh thao tác đã chạy. |
| Tạo và cấu hình S3 (tag, Block Public Access, mã hóa mặc định) | Nguyễn Văn Trung | [scripts/01_setup_s3.sh](../scripts/01_setup_s3.sh) · [Ảnh S3 Block Public Access — evidence-04](../docs/screenshots/week1-evidence-04.png) · [Ảnh S3 tags và mã hóa — evidence-05](../docs/screenshots/week1-evidence-05.png) | Ảnh đã có trên GitHub; cần mở kiểm tra độ rõ và đối chiếu đúng nội dung trước khi nộp. |
| Tạo EC2 mẫu và gắn tag | Nguyễn Văn Trung | [scripts/02_create_ec2.sh](../scripts/02_create_ec2.sh) · [Ảnh EC2 Running — evidence-06](../docs/screenshots/week1-evidence-06.png) · [Ảnh EC2 tags — evidence-07](../docs/screenshots/week1-evidence-07.png) · [Ảnh EBS tags — evidence-08](../docs/screenshots/week1-evidence-08.png) | Ảnh đã có trên GitHub; cần mở kiểm tra độ rõ và đối chiếu đúng nội dung trước khi nộp. |
| Tạo RDS MySQL mẫu | Nguyễn Văn Thi | [scripts/03_create_rds.sh](../scripts/03_create_rds.sh) · [Ảnh RDS Available — evidence-09](../docs/screenshots/week1-evidence-09.png) · [Ảnh RDS configuration — evidence-10](../docs/screenshots/week1-evidence-10.png) · [Ảnh RDS tags — evidence-11](../docs/screenshots/week1-evidence-11.png) | Ảnh đã có trên GitHub; cần mở kiểm tra độ rõ và đối chiếu đúng nội dung trước khi nộp. |
| Tạo SageMaker Notebook mẫu dùng LabRole | Nguyễn Văn Thi | [scripts/04_create_sagemaker.sh](../scripts/04_create_sagemaker.sh) · [Yêu cầu IAM](../docs/iam-requirements.md) · [Ảnh SageMaker InService — evidence-12](../docs/screenshots/week1-evidence-12.png) · [Ảnh SageMaker tags — evidence-13](../docs/screenshots/week1-evidence-13.png) · [Ảnh IAM Policies — evidence-03](../docs/screenshots/week1-evidence-03.png) | Ảnh Notebook và tags đã có; ảnh IAM Policies chưa đủ để chứng minh LabRole. Cần kiểm tra hoặc bổ sung ảnh role thực tế nếu được yêu cầu. |
| Kiểm tra Account/Region/thời gian và trạng thái tài nguyên | Cả hai | [scripts/05_status.sh](../scripts/05_status.sh) · [Runbook Tuần 1](../docs/week1-runbook.md) · [Ảnh khởi động Learner Lab — evidence-02](../docs/screenshots/week1-evidence-02.png) | Script và ảnh đã có trên GitHub; cần xác nhận ảnh/log thể hiện đủ Account ID, Region và thời gian trước khi kết luận đã kiểm chứng. |
| Sơ đồ kiến trúc và quy ước tag | Cả hai; Nguyễn Văn Thi phối hợp chuẩn bị sơ đồ theo worklog | [docs/architecture.md](../docs/architecture.md) · [PROJECT_PLAN.md](../PROJECT_PLAN.md) | File kiến trúc có trên GitHub. Nếu giảng viên yêu cầu sơ đồ draw.io gốc, cần liên kết file gốc riêng. |
| Sơ đồ kiến trúc | Cả hai; Nguyễn Văn Thi phối hợp chuẩn bị sơ đồ theo worklog | [Danh mục minh chứng Tuần 1](../docs/week1-evidence.md) · [Ảnh sơ đồ kiến trúc — evidence-01](../docs/screenshots/week1-evidence-01.png) · [Ảnh sơ đồ kiến trúc trong thư mục screenshots](../docs/screenshots/autoschedule-infrastructure.png) | Các file ảnh đã có trên GitHub; cần xác nhận sơ đồ ảnh và file kiến trúc là phiên bản đúng cần nộp. |
| Kiểm tra tài nguyên còn sót | Cả hai | [scripts/05_status.sh](../scripts/05_status.sh) · [Ảnh kiểm tra EC2/EBS — evidence-14](../docs/screenshots/week1-evidence-14.png) | Ảnh đã có trên GitHub; kiểm tra nội dung và độ rõ trước khi nộp. |
| Tập hợp ảnh và rà soát minh chứng | Cả hai | [Danh mục minh chứng Tuần 1](../docs/week1-evidence.md) · [Thư mục 14 ảnh](../docs/screenshots/) | Đã xác nhận 14 ảnh PNG có mặt trên GitHub. Cần đối chiếu từng ảnh với danh mục và kiểm tra không có dữ liệu nhạy cảm. |

## 4. Tổng hợp thời lượng

| Thành viên | Tổng thời gian |
|---|---:|
| Nguyễn Văn Trung (24110365) | 8 giờ 30 phút |
| Nguyễn Văn Thi (24110334) | 8 giờ 20 phút |
| **Tổng nhóm** | **16 giờ 50 phút** |

Các số giờ trên được giữ theo worklog/báo cáo nhóm hiện có. Không tự chia nhỏ thành số giờ cho từng hạng mục nếu chưa có nhật ký theo buổi để đối chiếu.

## 5. Khai báo sử dụng AI

Hai thành viên ghi nhận có sử dụng AI để tham khảo/hỗ trợ và đã rà soát lại nội dung. Khi nộp báo cáo, cần mô tả trung thực AI đã hỗ trợ phần nào và thành viên đã tự kiểm tra, chạy thử hoặc chỉnh sửa ra sao; không xem nội dung do AI tạo là bằng chứng cho thao tác AWS.

## 6. Việc cần hoàn tất trước khi nộp

- [ ] Xác nhận ngày thực hiện thực tế và đối chiếu số giờ của từng thành viên.
- [ ] Xác nhận lại phân công trên có đúng với đóng góp thực tế của từng người.
- [x] Xác nhận 14 ảnh PNG `week1-evidence-01.png` đến `week1-evidence-14.png` đã có trong [docs/screenshots](../docs/screenshots/).
- [x] Thêm các link trực tiếp tới ảnh hiện có trong mục 3; tiếp tục mở từng link để đối chiếu ảnh với hạng mục và [danh mục minh chứng](../docs/week1-evidence.md).
- [ ] Kiểm tra ảnh/log có thể hiện rõ Account ID, Region, thời gian, trạng thái và tags cần chứng minh; bổ sung ảnh/log nếu còn thiếu.
- [ ] Bổ sung minh chứng LabRole phù hợp nếu được yêu cầu; không dùng riêng ảnh IAM Policies để kết luận đã xác minh role.
- [ ] Kiểm tra không có access key, secret, session token hoặc dữ liệu nhạy cảm trong ảnh/log trước khi commit.

## 7. Tài liệu Tuần 1 liên quan

- [Kế hoạch dự án và phân công ban đầu](../PROJECT_PLAN.md)
- [Runbook Tuần 1](../docs/week1-runbook.md)
- [Danh mục minh chứng Tuần 1](../docs/week1-evidence.md)
- [Sơ đồ/ghi chú kiến trúc](../docs/architecture.md)
- [Script kiểm tra trạng thái AWS](../scripts/05_status.sh)
