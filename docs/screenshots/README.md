# Minh chứng AWS — Tuần 1

Báo cáo `Bao_cao_tuan1_Nhom_DevOps&IaC.docx` được cung cấp có 14 ảnh nhúng (sơ đồ kiến trúc và ảnh AWS Console). Các ảnh hiện vẫn nằm bên trong DOCX, chưa được tách thành file ảnh riêng trong repository. Không có ảnh giả lập hoặc kết quả AWS được tạo thay thế trong thư mục này.

## Cần bổ sung

Tách ảnh gốc nhúng trong báo cáo DOCX và thêm vào thư mục này, rồi cập nhật liên kết trong [worklog tuần 1](../../worklog/week1.md). Báo cáo có ảnh S3 Block Public Access/tags/encryption, EC2 Running/tags, RDS Available/config/tags, SageMaker InService/tags và kiểm tra tài nguyên.

Gợi ý tên file (chỉ dùng sau khi có ảnh thật):
- `aws-identity-region-time.png` — Account ID, Region và thời gian.
- `s3-tags-public-access-encryption.png` — tags, Block Public Access và mã hóa của S3.
- `ec2-instance-tags.png` — EC2 và tags.
- `rds-status-tags.png` — RDS và tags.
- `sagemaker-status-tags.png` — SageMaker Notebook và tags.
- `status-script-output.png` — kết quả `scripts/05_status.sh`.

## Điểm cần lưu ý từ báo cáo

Báo cáo nhóm ghi rõ ảnh IAM Policies hiện tại chưa đủ để chứng minh `LabRole`/ARN; cần thay bằng ảnh trang IAM Roles/ARN nếu giảng viên yêu cầu chứng minh.

## Quy tắc

- Chỉ tải ảnh gốc đã chụp trong buổi thực hành; không dựng ảnh minh họa thay cho kết quả thật.
- Che thông tin nhạy cảm nếu ảnh có chứa thông tin không nên công khai.
- Không ghi ngày hoặc trạng thái tài nguyên nếu ảnh/log không hỗ trợ điều đó.
- Sau khi tải ảnh lên, cập nhật checklist và liên kết minh chứng trong worklog.
