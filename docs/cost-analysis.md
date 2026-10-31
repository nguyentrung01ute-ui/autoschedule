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

## Quy đổi theo tháng

- 24/7: khoảng 730 giờ/tháng.
- Lịch 08:00-17:00, Mon-Fri: 45 giờ/tuần x 52 tuần / 12 tháng ≈ 195 giờ/tháng.
- Hệ số theo lịch = 195 / 730 ≈ 0,267.

## Nguồn số liệu

- Chi phí 24/7 lấy từ **AWS Pricing Calculator**, Region US East (N. Virginia): $96,00/tháng, $1.152,00/12 tháng ([Hình 16](screenshots/week4-evidence-16.png)).
- Chi phí theo lịch là **ước tính** = chi phí 24/7 x 195/730.
- Ngân sách Learner Lab đã dùng tại thời điểm báo cáo: **$3,5 / $50** ([Hình 15](screenshots/week4-evidence-15.png)).

## Bảng cuối kỳ (theo tháng)

| Tài nguyên | Chạy 24/7 | Chạy theo lịch | Giờ giảm | Chi phí ước tính 24/7 | Chi phí theo lịch | Tiết kiệm |
|---|---:|---:|---:|---:|---:|---:|
| EC2 (t3.nano, EBS 8 GB) | 730 h | 195 h | 535 h | ≈ $4,44 | ≈ $1,19 | ≈ $3,25 |
| RDS compute (MySQL db.t3.micro, 20 GB) | 730 h | 195 h | 535 h | ≈ $54,86 | ≈ $14,65 | ≈ $40,21 |
| SageMaker compute (ml.t3.medium, 5 GB) | 730 h | 195 h | 535 h | ≈ $36,70 | ≈ $9,80 | ≈ $26,90 |
| Lambda/Events/SNS/Logs | ≈ 2.880 lần gọi/tháng | ≈ 2.880 lần gọi/tháng | — | ≈ $0 (Free Tier) | ≈ $0 (Free Tier) | — |
| **Tổng** | | | | **≈ $96,00** | **≈ $25,64** | **≈ $70,36 (≈ 73%)** |

Ghi chú:

- Số lần gọi Lambda: `rate(15 minutes)` = 96 lần/ngày x 30 ngày ≈ 2.880 lần/tháng, cộng 30 lần report; nằm trong mức miễn phí hoặc không đáng kể.
- Phí lưu trữ (EBS 8 GB, RDS 20 GB, Notebook 5 GB) là cố định, không giảm theo lịch, nên mức tiết kiệm thực tế thấp hơn một chút so với 73%.
- RDS Stopped vẫn tính phí lưu trữ và AWS tự bật lại sau tối đa 7 ngày (Lambda tắt lại ở chu kỳ kế tiếp).
