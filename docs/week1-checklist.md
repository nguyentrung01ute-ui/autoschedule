# Checklist Tuần 1

## Trạng thái thực hành

Theo báo cáo Tuần 1 do nhóm cung cấp, tài liệu có 14 ảnh nhúng và ghi nhận các kết quả thực hành bên dưới. Ảnh hiện nằm trong file báo cáo DOCX đính kèm, chưa được tách thành các file ảnh riêng trong repository. Các trạng thái dưới đây phản ánh báo cáo tại thời điểm chụp, không khẳng định trạng thái AWS hiện tại.

- [x] Thực hiện bước cấu hình S3 bucket, tag, Block Public Access và mã hóa
- [x] Thực hiện tạo EC2 mẫu và cấu hình tag theo bài thực hành
- [x] Thực hiện tạo RDS mẫu và cấu hình tag theo bài thực hành
- [x] Thực hiện tạo SageMaker Notebook mẫu và cấu hình tag theo bài thực hành
- [x] Chuẩn bị sơ đồ/thiết kế kiến trúc trong `docs/architecture.md`
- [x] Thực hiện kiểm tra tài nguyên bằng `scripts/05_status.sh`
- [x] Hoàn thành phần thực hành Tuần 1 theo xác nhận của người thực hiện

## Việc còn thiếu trên GitHub

- [ ] Tách/tải ảnh gốc nhúng trong báo cáo DOCX lên `docs/screenshots/` và liên kết lại trong worklog
- [ ] Bổ sung ảnh IAM Roles/ARN của `LabRole`: báo cáo hiện tại tự ghi nhận ảnh IAM Policies chưa đủ để chứng minh LabRole
- [ ] Kiểm tra ảnh minh chứng thể hiện Account ID, Region, thời gian, trạng thái và tag phù hợp
- [ ] Cập nhật ngày thực hiện thực tế trong `worklog/week1.md` (hiện chưa xác nhận)
- [ ] Xác nhận và ghi lại việc dừng/dọn tài nguyên sau thực hành; không suy đoán trạng thái hiện tại

## Kết quả được ghi trong báo cáo nhóm

- **S3:** bucket `autoschedule-465409046652-us-east-1`; báo cáo ghi nhận Block Public Access bật, SSE-S3 và tag Project/Owner.
- **EC2:** `autoschedule-ec2`, loại `t3.nano`, báo cáo ghi nhận Running và 2/2 checks passed; 4 tag trên instance và volume.
- **RDS:** `autoschedule-db`, MySQL `db.t3.micro`, 20 GiB gp3, Single-AZ, không public; báo cáo ghi nhận trạng thái Available và 4 tag.
- **SageMaker:** `autoschedule-nb`, `ml.t3.medium`, volume 5 GB, dùng LabRole; báo cáo ghi nhận InService và 4 tag.
- **Giới hạn minh chứng:** báo cáo nêu ảnh IAM Policies chưa đủ chứng minh LabRole. Ảnh là bằng chứng lịch sử trong báo cáo, không xác nhận trạng thái hiện tại.

## Lệnh tham khảo

Chạy trong CloudShell ở region được phép (`us-east-1` hoặc `us-west-2`):

```bash
aws sts get-caller-identity
aws configure get region
date -u

chmod +x scripts/*.sh
./scripts/01_setup_s3.sh
./scripts/02_create_ec2.sh
./scripts/03_create_rds.sh
./scripts/04_create_sagemaker.sh
./scripts/05_status.sh
```

> Ghi chú: Các mục thực hành được đánh dấu hoàn thành dựa trên xác nhận của người thực hiện. Chưa có ảnh/log AWS trong repository để kiểm tra độc lập các giá trị cụ thể hoặc trạng thái hiện tại của tài nguyên.
