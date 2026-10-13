# Minh chứng AWS — Tuần 1

Thư mục này lưu các ảnh minh chứng của báo cáo Tuần 1. Hiện có 14 ảnh `week1-evidence-01.png` đến `week1-evidence-14.png` và sơ đồ `autoschedule-infrastructure.png`.

## Minh chứng hiện có

- Sơ đồ kiến trúc AutoSchedule.
- Ảnh khởi động AWS Learner Lab và ảnh IAM Policies.
- Ảnh S3 Block Public Access, tags và default encryption.
- Ảnh EC2 Running, instance tags và EBS volume tags.
- Ảnh RDS Available, cấu hình và tags.
- Ảnh SageMaker Notebook InService và tags.
- Ảnh kiểm tra EC2/EBS và tài nguyên còn sót.

Danh mục và liên kết tới từng ảnh: [docs/week1-evidence.md](../week1-evidence.md).

## Minh chứng còn thiếu hoặc cần xác minh trước khi nộp

1. **Account ID, Region và thời gian thực hành:** chưa có ảnh được xác định rõ trong danh mục hiện tại là bằng chứng đầy đủ cho cả ba thông tin. Nếu ảnh `week1-evidence-02.png` không hiển thị rõ các thông tin này, thêm ảnh AWS Console/Learner Lab thể hiện chúng.
2. **Role LabRole của SageMaker:** ảnh IAM Policies hiện tại chưa chứng minh Notebook đã được gán `LabRole`. Cần ảnh cấu hình SageMaker Notebook thể hiện execution role được chọn; nếu cần, thêm ảnh IAM Roles thể hiện tên/ARN của role.
3. **Kết quả chạy `scripts/05_status.sh`:** chưa có ảnh đầu ra riêng được liệt kê trong bộ 14 ảnh. Nếu báo cáo dùng script này để khẳng định trạng thái tài nguyên, lưu đầu ra thực tế và thêm ảnh/log vào thư mục.
4. **Đối chiếu nội dung từng ảnh:** cần mở các ảnh hiện có để xác nhận chữ, trạng thái tài nguyên, tags và cấu hình đều đọc được. Không thể kết luận chỉ từ việc file ảnh tồn tại.

## Kiểm tra trước khi commit

- [x] Có đủ 14 ảnh PNG theo danh mục.
- [ ] Xác minh ảnh có hiển thị Account ID, Region và thời gian cần thiết.
- [ ] Bổ sung bằng chứng SageMaker sử dụng `LabRole`.
- [ ] Bổ sung đầu ra `scripts/05_status.sh` nếu dùng làm bằng chứng kiểm tra.
- [ ] Kiểm tra ảnh/log không để lộ access key, secret key, session token hoặc dữ liệu nhạy cảm.

Chỉ thêm ảnh chụp/log thực tế từ môi trường đã thực hành. Không tạo ảnh minh họa thay cho kết quả AWS và không suy đoán ngày hoặc trạng thái nếu nguồn không chứng minh được.
