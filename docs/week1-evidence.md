# Minh chứng Tuần 1 — AutoSchedule

Các ảnh trong thư mục này được trích nguyên dạng từ báo cáo DOCX Tuần 1 do nhóm cung cấp. Tên file được giữ theo thứ tự trong báo cáo để dễ đối chiếu. Ngày thực hiện cần được xác nhận riêng; ngày chụp không được suy đoán.

> **Lưu ý:** Bản chỉ mục này đã được thêm vào repository. Các ảnh PNG cần được tải lên `docs/screenshots/` bằng đúng tên bên dưới trước khi coi bộ minh chứng là đầy đủ.

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
| [week1-evidence-14.png](screenshots/week1-evidence-14.png) | EC2/EBS và kiểm tra tài nguyên còn sót | Đối chiếu dọn dẹp |

## Checklist trước khi nộp

- [ ] Tải đủ 14 ảnh PNG vào `docs/screenshots/` theo tên ở bảng.
- [ ] Xác nhận ngày thực hiện và cập nhật `worklog/week1.md`; không dùng ngày commit làm ngày thực hành.
- [ ] Kiểm tra ảnh không để lộ access key, secret, session token, email riêng hoặc dữ liệu nhạy cảm.
- [ ] Bổ sung minh chứng IAM/LabRole rõ ràng nếu giảng viên yêu cầu.
- [ ] Kiểm tra các ảnh thể hiện rõ Account/Region/thời gian nếu dùng để xác minh môi trường.
