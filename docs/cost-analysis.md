# Phân tích chi phí

## Công thức

Nếu một tài nguyên chạy H giờ/tuần thay vì 168 giờ/tuần:

    Tiết kiệm giờ = 168 - H
    Tỷ lệ giảm giờ chạy = (168 - H) / 168 * 100%

Ví dụ lịch 08:00-17:00, Mon-Fri:

- 9 giờ/ngày x 5 ngày = 45 giờ/tuần.
- So với 168 giờ/tuần, giảm 123 giờ.
- Tỷ lệ giảm giờ chạy khoảng 73.2%.

Đây là tỷ lệ giờ chạy, không phải số tiền tiết kiệm thực tế. Báo cáo cuối kỳ phải dùng đơn giá thực tế/ước tính phù hợp với tài nguyên và ghi rõ nguồn.

## RDS

Khi RDS stopped, vẫn phát sinh chi phí lưu trữ; AWS cũng tự khởi động DB sau tối đa 7 ngày. Vì vậy không được tuyên bố RDS tiết kiệm 100% chi phí khi stopped.

## Lambda/EventBridge/SNS/CloudWatch

Ghi nhận số invocation, log và cảnh báo thực tế nếu có thể. Nếu quyền Learner Lab không cho xem Cost Explorer, dùng AWS Pricing Calculator và ghi rõ đó là ước tính.

## Bảng cuối kỳ

| Tài nguyên | Chạy 24/7 | Chạy theo lịch | Giờ giảm | Chi phí ước tính 24/7 | Chi phí theo lịch | Tiết kiệm |
|---|---:|---:|---:|---:|---:|---:|
| EC2 | | | | | | |
| RDS compute | | | | | | |
| SageMaker compute | | | | | | |
| Lambda/Events/SNS/Logs | | | | | | |
| Tổng | | | | | | |
