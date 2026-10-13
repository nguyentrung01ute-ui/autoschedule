# Minh chứng Tuần 1 — AutoSchedule

Các ảnh trong thư mục này được trích nguyên dạng từ báo cáo DOCX Tuần 1 do nhóm cung cấp. Tên file được giữ theo thứ tự trong báo cáo để dễ đối chiếu. Ngày thực hiện cần được xác nhận riêng; ngày chụp không được suy đoán.

> **Trạng thái:** 14 ảnh PNG ban đầu và 2 ảnh bổ sung (`week1-evidence-15-sagemaker-execution-role.png`, `week1-evidence-16-account-region.png`) đã có trong `docs/screenshots/`. Việc file tồn tại chưa bảo đảm nội dung ảnh đủ rõ hoặc chứng minh đầy đủ mọi cấu hình; các điểm còn thiếu được nêu ở cuối tài liệu.

## Danh sách ảnh

| Ảnh | Nội dung | Ghi chú |
|---|---|---|
| [week1-evidence-01.png](screenshots/week1-evidence-01.png) | Sơ đồ kiến trúc AutoSchedule | Hình 1 trong báo cáo |
| [week1-evidence-02.png](screenshots/week1-evidence-02.png) | Khởi động AWS Learner Lab | Hình 2 |
| [week1-evidence-03.png](screenshots/week1-evidence-03.png) | IAM Policies | Chưa đủ để chứng minh LabRole; cần ảnh role/permission phù hợp |
| [week1-evidence-04.png](screenshots/week1-evidence-04.png) | S3 Block Public Access | Cấu hình bảo mật bucket |
| [week1-evidence-05.png](screenshots/week1-evidence-05.png) | S3 tags và default encryption | Cấu hình bucket |
| [week1-evidence-06.png](screenshots/week1-evidence-06.png) | EC2 Running và status checks | Trạng thái instance tại thời điểm chụp |
| [week1-evidence-07.png](screenshots/week1-evidence-07.png) | EC2 instance tags | Đối chiếu tag Project/Owner/Schedule |
| [week1-evidence-08.png](screenshots/week1-evidence-08.png) | EBS volume tags | Đối chiếu tag volume |
| [week1-evidence-09.png](screenshots/week1-evidence-09.png) | RDS Available | Trạng thái DB tại thời điểm chụp |
| [week1-evidence-10.png](screenshots/week1-evidence-10.png) | RDS configuration | Cấu hình DB |
| [week1-evidence-11.png](screenshots/week1-evidence-11.png) | RDS tags | Đối chiếu tag DB |
| [week1-evidence-12.png](screenshots/week1-evidence-12.png) | SageMaker Notebook InService | Trạng thái notebook tại thời điểm chụp |
| [week1-evidence-13.png](screenshots/week1-evidence-13.png) | SageMaker tags | Đối chiếu tag notebook |
| [week1-evidence-14.png](screenshots/week1-evidence-14.png) | EC2/EBS và kiểm tra tài nguyên còn sót | Đối chiếu dọn dẹp |\n| [week1-evidence-15-sagemaker-execution-role.png](screenshots/week1-evidence-15-sagemaker-execution-role.png) | SageMaker Notebook execution role | Ảnh bổ sung cho thấy IAM role ARN chứa `LabRole` |\n| [week1-evidence-16-account-region.png](screenshots/week1-evidence-16-account-region.png) | AWS Account ID và Region | Ảnh bổ sung hiển thị Account ID và `us-east-1`; kiểm tra ngày/giờ riêng nếu yêu cầu |

## Checklist trước khi nộp

- [x] Xác nhận 16 ảnh PNG bằng chứng đã có trong `docs/screenshots/`.
- [ ] Xác nhận ngày thực hiện và cập nhật `worklog/week1.md`; không dùng ngày commit làm ngày thực hành.
- [ ] Kiểm tra ảnh không để lộ access key, secret, session token, email riêng hoặc dữ liệu nhạy cảm.
- [x] Bổ sung ảnh cấu hình SageMaker thể hiện execution role `LabRole` tại [week1-evidence-15-sagemaker-execution-role.png](screenshots/week1-evidence-15-sagemaker-execution-role.png).
- [x] Bổ sung ảnh Account ID và Region tại [week1-evidence-16-account-region.png](screenshots/week1-evidence-16-account-region.png).\n- [ ] Xác minh/bổ sung thời gian thực hành nếu yêu cầu; ảnh Account/Region hiện chưa tự chứng minh ngày giờ chụp.
- [ ] Thêm đầu ra thực tế của `scripts/05_status.sh` nếu dùng script này làm bằng chứng trạng thái tài nguyên.
- [ ] Mở và đối chiếu từng ảnh để xác nhận trạng thái, tags và cấu hình đọc được.

## Các minh chứng cần bổ sung hoặc xác minh cụ thể

1. **SageMaker/LabRole:** đã bổ sung [ảnh cấu hình Notebook](screenshots/week1-evidence-15-sagemaker-execution-role.png) có IAM role ARN chứa `LabRole`.
2. **Account ID và Region:** đã bổ sung [ảnh AWS Console](screenshots/week1-evidence-16-account-region.png). Thời gian chụp/thực hành cần xác nhận riêng nếu giảng viên yêu cầu.
3. **Kết quả kiểm tra tài nguyên:** chưa có ảnh đầu ra riêng của `scripts/05_status.sh` trong danh sách 14 ảnh. Nếu dùng script làm bằng chứng, lưu đầu ra thực tế rồi thêm link tại đây và trong worklog.
4. **Ngày thực hiện:** xác nhận ngày làm việc từ nhật ký của nhóm; không suy ra ngày thực hành từ ngày commit.

