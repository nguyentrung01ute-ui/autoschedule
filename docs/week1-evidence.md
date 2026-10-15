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

Các liên kết mở trực tiếp từng tệp trong repository:

1. **Kế hoạch dự án:** [PROJECT_PLAN.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/PROJECT_PLAN.md)
2. **Thiết kế kiến trúc:** [architecture.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/docs/architecture.md)
3. **Runbook Tuần 1:** [week1-runbook.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/docs/week1-runbook.md)
4. **Worklog Tuần 1:** [week1.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/worklog/week1.md)
5. **Mã nguồn scheduler:** [scheduler.py](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/src/scheduler.py)
6. **Template CloudFormation:** [template.yaml](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/infra/template.yaml)
7. **Ảnh sơ đồ hạ tầng:** [autoschedule-infrastructure.png](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/docs/screenshots/autoschedule-infrastructure.png)
8. **Khai báo sử dụng AI Tuần 1:** [ai-disclosure-week1.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/docs/ai-disclosure-week1.md)

**Commit khai báo AI:** [efe013161d455354457311cb809a8034b3e1bc84](https://github.com/nguyentrung01ute-ui/autoschedule/commit/efe013161d455354457311cb809a8034b3e1bc84)

**Commit cập nhật liên kết sản phẩm/minh chứng:** [ac620878a5f9121d2dbe88eebdc7a601a3fd023b](https://github.com/nguyentrung01ute-ui/autoschedule/commit/ac620878a5f9121d2dbe88eebdc7a601a3fd023b)

> Lưu ý: việc có mã nguồn hoặc template trong repository không tự chứng minh rằng mã đã được triển khai hay kiểm thử thành công trên AWS. Kết quả triển khai phải được đối chiếu với ảnh/log thực tế.
