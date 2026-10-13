# Worklog tuần 1 — AutoSchedule

## 1. Thông tin chung

- **Nhóm:** DevOps & IaC
- **Dự án:** AutoSchedule — tự động bật/tắt tài nguyên AWS theo lịch
- **Môi trường dự kiến:** AWS Learner Lab, Region `us-east-1` (có thể dùng `us-west-2` theo quy định lab)
- **Thành viên:** Nguyễn Văn Trung (24110365), Nguyễn Văn Thi (24110334)
- **Tổng thời lượng đã ghi nhận:** 16 giờ 50 phút
- **Ngày thực hiện:** Chưa xác nhận được ngày cụ thể cho từng công việc. Cần đối chiếu lịch làm việc thực tế trước khi nộp; không lấy ngày commit thay cho ngày thực hành.
- **Trạng thái minh chứng:** Báo cáo Tuần 1 do nhóm cung cấp được ghi nhận có 14 ảnh nhúng. Tại thời điểm cập nhật worklog này, các ảnh chưa được xác nhận đã tách thành file riêng và tải lên `docs/screenshots/`. Vì vậy, link mã nguồn bên dưới là link file-level để kiểm tra nội dung repository, không thay thế cho ảnh chứng minh thao tác AWS thực tế.

## 2. Phân công và kết quả theo thành viên

| Thành viên | Công việc được ghi nhận | Thời lượng | Link file-level liên quan |
|---|---|---:|---|
| **Nguyễn Văn Trung (24110365)** | Chuẩn bị repository và cấu trúc làm việc; thực hành tạo/cấu hình S3; thực hành tạo EC2 mẫu; tìm hiểu tài liệu AWS và kiến trúc. | **8 giờ 30 phút** | [Cấu hình chung](../scripts/config.sh) · [Tạo S3](../scripts/01_setup_s3.sh) · [Tạo EC2](../scripts/02_create_ec2.sh) · [Kiến trúc](../docs/architecture.md) |
| **Nguyễn Văn Thi (24110334)** | Thực hành tạo RDS MySQL và SageMaker Notebook mẫu; phối hợp chuẩn bị sơ đồ kiến trúc; tìm hiểu tài liệu AWS. | **8 giờ 20 phút** | [Tạo RDS](../scripts/03_create_rds.sh) · [Tạo SageMaker Notebook](../scripts/04_create_sagemaker.sh) · [Kiến trúc](../docs/architecture.md) |
| **Cả hai thành viên** | Cùng tìm hiểu EventBridge, boto3 và giới hạn AWS Learner Lab; rà soát trạng thái tài nguyên, worklog và các yêu cầu minh chứng. Phân chia chi tiết theo buổi cần được xác nhận với nhật ký thực tế. | Đã tính trong tổng giờ của từng thành viên; không cộng thêm lần nữa. | [Kế hoạch dự án và phân công Tuần 1](../PROJECT_PLAN.md) · [Runbook Tuần 1](../docs/week1-runbook.md) · [Lệnh kiểm tra trạng thái](../scripts/05_status.sh) |

> **Lưu ý về phân công:** Bảng trên ghi lại phần việc hiện có trong worklog và kế hoạch dự án. Chỉ giữ các đầu việc mà từng thành viên thực sự đã thực hiện; nếu có khác biệt, sửa lại trước khi nộp.

## 3. Nhật ký công việc và liên kết kiểm chứng

| Hạng mục | Người phụ trách theo ghi nhận hiện tại | File/nguồn kiểm tra | Trạng thái minh chứng |
|---|---|---|---|
| Chuẩn bị repository, cấu hình môi trường và quy ước tag | Nguyễn Văn Trung | [PROJECT_PLAN.md](../PROJECT_PLAN.md) · [scripts/config.sh](../scripts/config.sh) | File kế hoạch và script có trên GitHub; cần ảnh/log thực tế để xác minh thao tác đã chạy. |
| Tạo và cấu hình S3 (tag, Block Public Access, mã hóa mặc định) | Nguyễn Văn Trung | [scripts/01_setup_s3.sh](../scripts/01_setup_s3.sh) | Cần tải ảnh S3 gốc vào `docs/screenshots/` và liên kết trực tiếp bên dưới khi đã có file. |
| Tạo EC2 mẫu và gắn tag | Nguyễn Văn Trung | [scripts/02_create_ec2.sh](../scripts/02_create_ec2.sh) | Cần ảnh trạng thái EC2 và tags thực tế. |
| Tạo RDS MySQL mẫu | Nguyễn Văn Thi | [scripts/03_create_rds.sh](../scripts/03_create_rds.sh) | Cần ảnh trạng thái RDS, cấu hình và tags thực tế. |
| Tạo SageMaker Notebook mẫu dùng LabRole | Nguyễn Văn Thi | [scripts/04_create_sagemaker.sh](../scripts/04_create_sagemaker.sh) · [Yêu cầu IAM](../docs/iam-requirements.md) | Cần ảnh trạng thái Notebook, tags và role thực tế; ảnh IAM Policies đơn lẻ chưa đủ để chứng minh LabRole. |
| Kiểm tra Account/Region/thời gian và trạng thái tài nguyên | Cả hai | [scripts/05_status.sh](../scripts/05_status.sh) · [Runbook Tuần 1](../docs/week1-runbook.md) | Cần lưu log/ảnh đầu ra thực tế; không đánh dấu đã xác minh nếu chưa có bằng chứng. |
| Sơ đồ kiến trúc và quy ước tag | Cả hai; Nguyễn Văn Thi phối hợp chuẩn bị sơ đồ theo worklog | [docs/architecture.md](../docs/architecture.md) · [PROJECT_PLAN.md](../PROJECT_PLAN.md) | File kiến trúc có trên GitHub. Nếu giảng viên yêu cầu sơ đồ draw.io gốc, cần liên kết file gốc riêng. |
| Tập hợp ảnh và rà soát minh chứng | Cả hai | [Danh mục minh chứng Tuần 1](../docs/week1-evidence.md) | Danh mục ghi nhận 14 ảnh nhúng trong báo cáo nhóm; chưa xác nhận các PNG đã được tải lên repository. |

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
- [ ] Tách 14 ảnh gốc từ báo cáo nhóm và tải lên `docs/screenshots/` bằng tên khớp với [danh mục minh chứng](../docs/week1-evidence.md).
- [ ] Thêm link trực tiếp tới từng ảnh PNG đã tải lên; không để link tới file chưa tồn tại.
- [ ] Bổ sung ảnh/log thể hiện Account ID, Region, thời gian, trạng thái và tags của các tài nguyên AWS.
- [ ] Bổ sung minh chứng LabRole phù hợp nếu được yêu cầu; không dùng riêng ảnh IAM Policies để kết luận đã xác minh role.
- [ ] Kiểm tra không có access key, secret, session token hoặc dữ liệu nhạy cảm trong ảnh/log trước khi commit.

## 7. Tài liệu Tuần 1 liên quan

- [Kế hoạch dự án và phân công ban đầu](../PROJECT_PLAN.md)
- [Runbook Tuần 1](../docs/week1-runbook.md)
- [Danh mục minh chứng Tuần 1](../docs/week1-evidence.md)
- [Sơ đồ/ghi chú kiến trúc](../docs/architecture.md)
- [Script kiểm tra trạng thái AWS](../scripts/05_status.sh)
