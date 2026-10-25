# Khai báo sử dụng AI — Tuần 3

## 1. Công cụ được sử dụng
- **Công cụ:** Claude (Anthropic).
- **Mô hình / Phiên bản:** Claude Sonnet 5.5.
- **Phạm vi sử dụng trong Tuần 3:**
  - Hỗ trợ tham khảo cú pháp và quy trình tạo lịch tự kích hoạt EventBridge Scheduler (do AWS Console thay đổi giao diện không còn kiểu rule "Schedule" trực tiếp ở Advanced Rule Builder).
  - Tham khảo cấu trúc tham số lệnh `aws cloudformation deploy` trong script `scripts/07_deploy.sh` để truyền biến S3 key động và ARN role LabRole.
  - Tham khảo danh mục rà soát bảo mật hạ tầng trên AWS (kiểm tra rò rỉ secret/key trong mã nguồn, thiết lập Security Group, cấu hình mã hóa và Block Public Access cho S3, RDS).
  - Hỗ trợ dàn ý quy trình gây lỗi có chủ đích để kiểm thử CloudWatch Alarm (`autoschedule-errors`) và cơ chế tự phục hồi về trạng thái OK.

## 2. Cách nhóm sử dụng và kiểm tra
Nhóm sinh viên chịu trách nhiệm hoàn toàn về toàn bộ mã nguồn, cấu hình hạ tầng và kết quả thực nghiệm trên hệ sinh thái AWS Learner Lab:
- Cấu hình lịch EventBridge Scheduler và CloudFormation template (`infra/template.yaml`) do sinh viên tự đối chiếu với tài liệu chính thức của AWS, kiểm tra tương thích quyền của `LabRole`.
- Các thao tác dọn dẹp tài nguyên thủ công, chạy script đóng gói `07_deploy.sh`, upload artifact lên S3 và deploy stack đều được sinh viên thực hiện trực tiếp trên AWS CloudShell.
- Quá trình kiểm thử tự kích hoạt (INT-10a, INT-10b, INT-11), kiểm thử xóa/tạo lại stack (INT-12, INT-13) và kiểm thử CloudWatch Alarm (INT-14) được sinh viên trực tiếp kích hoạt, quan sát log CloudWatch thực tế và thu thập đủ 34 ảnh minh chứng rõ nét thời gian thực.
- Các lệnh quét bảo mật (`grep -rniE "password|secret|AKIA"`) được sinh viên thực hiện trên repository thực tế để kiểm tra triệt để không có mã độc hay credential lộ lọt.

## 3. Minh chứng Git
- **Commit thêm báo cáo Tuần 3:** [Commit 8a0adff](https://github.com/nguyentrung01ute-ui/autoschedule/commit/8a0adffbbc45e5c13281edb54f8ab820ec096090)
- **Commit cập nhật ảnh minh chứng Tuần 3 đợt 1 (01-11, 21-35):** [Commit add1c60](https://github.com/nguyentrung01ute-ui/autoschedule/commit/add1c60fc977a4a98dd9cbaee5f333fb1f692257)
- **Commit cập nhật ảnh minh chứng Tuần 3 đợt 2 (12-18):** [Commit 9a5f5ef](https://github.com/nguyentrung01ute-ui/autoschedule/commit/9a5f5ef4545d5ca3587053eef631525c34538d58)
