# Minh chứng Tuần 1 — AutoSchedule

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
| [week1-evidence-15-sagemaker-execution-role.png](screenshots/week1-evidence-15-sagemaker-execution-role.png) | SageMaker Notebook execution role | Ảnh bổ sung cho thấy IAM role ARN chứa `LabRole` |
| [week1-evidence-16-account-region.png](screenshots/week1-evidence-16-account-region.png) | AWS Account ID và Region | Ảnh bổ sung hiển thị Account ID và `us-east-1`; kiểm tra ngày/giờ riêng nếu yêu cầu |


## Liên kết sản phẩm và khai báo AI

Các liên kết dưới đây mở trực tiếp từng tệp trong repository:

- [Kế hoạch dự án](../PROJECT_PLAN.md)
- [Thiết kế kiến trúc](architecture.md)
- [Runbook Tuần 1](week1-runbook.md)
- [Worklog Tuần 1](../worklog/week1.md)
- [Mã nguồn scheduler](../src/scheduler.py)
- [Template CloudFormation](../infra/template.yaml)
- [Khai báo sử dụng AI Tuần 1](ai-disclosure-week1.md)

Commit bổ sung khai báo AI: [efe013161d455354457311cb809a8034b3e1bc84](https://github.com/nguyentrung01ute-ui/autoschedule/commit/efe013161d455354457311cb809a8034b3e1bc84).

> Lưu ý: các tệp mã nguồn và template là sản phẩm trong repository; bản thân việc có tệp không chứng minh rằng mã đã được triển khai hoặc kiểm thử thành công trên AWS. Kết quả triển khai cần có minh chứng thực tế tương ứng.
