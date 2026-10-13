# Checklist Tuần 1

## Trạng thái thực hành

Theo xác nhận của người thực hiện, toàn bộ công việc thực hành Tuần 1 đã hoàn thành. Checklist này phân biệt việc đã thực hành với việc đã đưa minh chứng lên GitHub; nội dung bên dưới không phải kết quả AWS được xác minh độc lập từ repository.

- [x] Thực hiện bước cấu hình S3 bucket, tag, Block Public Access và mã hóa
- [x] Thực hiện tạo EC2 mẫu và cấu hình tag theo bài thực hành
- [x] Thực hiện tạo RDS mẫu và cấu hình tag theo bài thực hành
- [x] Thực hiện tạo SageMaker Notebook mẫu và cấu hình tag theo bài thực hành
- [x] Chuẩn bị sơ đồ/thiết kế kiến trúc trong `docs/architecture.md`
- [x] Thực hiện kiểm tra tài nguyên bằng `scripts/05_status.sh`
- [x] Hoàn thành phần thực hành Tuần 1 theo xác nhận của người thực hiện

## Việc còn thiếu trên GitHub

- [ ] Tải ảnh AWS Console/CLI đang lưu trên máy tính lên `docs/screenshots/`
- [ ] Kiểm tra ảnh minh chứng thể hiện Account ID, Region, thời gian, trạng thái và tag phù hợp
- [ ] Cập nhật ngày thực hiện thực tế trong `worklog/week1.md` (hiện chưa xác nhận)
- [ ] Xác nhận và ghi lại việc dừng/dọn tài nguyên sau thực hành; không suy đoán trạng thái hiện tại

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
