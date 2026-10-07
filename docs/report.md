# Báo cáo cuối kỳ AutoSchedule

## 1. Giới thiệu
- Tên đề tài:
- Nhóm:
- GVHD: Huỳnh Xuân Phụng
- Region:
- Thành viên:

## 2. Bài toán và mục tiêu
Mô tả vấn đề lãng phí tài nguyên ngoài giờ học và mục tiêu tự động start/stop theo tag.

## 3. Kiến trúc
Chèn ảnh sơ đồ từ docs/architecture.md.

## 4. Thiết kế tag
| Tag | Giá trị ví dụ | Ý nghĩa |
|---|---|---|
| Project | AutoSchedule | Xác định tài nguyên thuộc project |
| Owner | sv01 | Chủ sở hữu |
| Schedule | 08:00-17:00 | Khung giờ chạy |
| ScheduleDays | Mon-Fri | Ngày chạy |

## 5. Triển khai
Mô tả S3, Lambda, EventBridge, EC2, RDS, SageMaker, SNS, CloudWatch và CloudFormation.

## 6. Kiểm thử
Dùng bảng trong docs/test-plan.md và chỉ điền kết quả dựa trên minh chứng thực tế.

## 7. Bảo mật
- Dùng LabRole/LabInstanceProfile theo quy định.
- Không tạo IAM user/role mới.
- Không commit mật khẩu/secret.
- RDS không public.
- Tài nguyên có Project/Owner.

## 8. Chi phí
Dùng docs/cost-analysis.md và số liệu thực tế/ước tính đã ghi nguồn.

## 9. Hạn chế
- Chu kỳ EventBridge 15 phút tạo độ trễ tối đa theo thiết kế.
- RDS tự start sau tối đa 7 ngày.
- LabRole có thể giới hạn một số API.
- Session Learner Lab có thể hết hạn.

## 10. AI hỗ trợ
Ghi rõ phần ChatGPT/LLM đã hỗ trợ, phần SV đã đọc, chạy, sửa và giải thích.

## 11. Kết luận
Tổng hợp kết quả đạt được và khả năng mở rộng.

## 12. Phụ lục
- Worklog tuần 1-4.
- Ảnh minh chứng.
- Link GitHub.
- Video demo.
