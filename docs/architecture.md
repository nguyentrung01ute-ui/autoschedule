# Kiến trúc AutoSchedule

Đề tài sử dụng EventBridge scheduled rules vì yêu cầu môn học chỉ định EventBridge rule. AWS hiện khuyến nghị EventBridge Scheduler cho các thiết kế mới, nhưng scheduled rule vẫn phù hợp với phạm vi bài lab này. 

## Sơ đồ

    EventBridge Rule: rate(15 minutes)
                 |
                 v
          Lambda autoschedule
             |    |    |
             v    v    v
            EC2  RDS  SageMaker
             ^    ^    ^
             |    |    |
       Project=AutoSchedule
       + Schedule + ScheduleDays

    EventBridge Rule: cron(0 1 * * ? *)
                 |
                 v
          Lambda report
                 |
                 v
               SNS
                 |
               Email

    Lambda --> CloudWatch Logs --> Error Alarm --> SNS
    S3 --> Lambda deployment package
    CloudFormation --> Lambda/EventBridge/SNS/Logs/Alarm

## Luồng enforce

1. EventBridge gọi Lambda mỗi 15 phút.
2. Lambda lấy EC2/RDS/SageMaker có Project=AutoSchedule và có Schedule.
3. Lambda đọc Schedule và ScheduleDays theo giờ Asia/Ho_Chi_Minh.
4. Nếu trạng thái thực tế khác trạng thái mong muốn thì gọi start/stop.
5. Tài nguyên đang ở trạng thái chuyển tiếp được bỏ qua và xử lý ở chu kỳ sau.

## Luồng report

1. Rule report chạy lúc 01:00 UTC, tương đương 08:00 Việt Nam.
2. Lambda thu thập các tài nguyên được quản lý đang chạy.
3. Lambda publish nội dung lên SNS.
4. SNS gửi email tới subscription đã xác nhận.

## Quy ước tag

| Tag | Ví dụ | Ý nghĩa |
|---|---|---|
| Project | AutoSchedule | Bắt buộc để Lambda xác định phạm vi |
| Owner | sv01 | Bắt buộc theo đề |
| Schedule | 08:00-17:00 | Khung giờ chạy |
| ScheduleDays | Mon-Fri | Ngày chạy |

Schedule=off nghĩa là tài nguyên phải dừng.

Lịch qua đêm, ví dụ 22:00-06:00, được tính tiếp sang ngày kế tiếp nhưng ngày đó phải xuất phát từ ngày bắt đầu của lịch. Ví dụ Mon-Fri 22:00-06:00 hoạt động tới 06:00 sáng thứ Bảy.

## Thành phần

| Thành phần | Vai trò |
|---|---|
| EventBridge | Kích hoạt Lambda theo chu kỳ và báo cáo |
| Lambda | Logic đọc tag, tính lịch, start/stop, report |
| EC2 | Loại tài nguyên 1 |
| RDS | Loại tài nguyên 2 |
| SageMaker Notebook | Loại tài nguyên 3 |
| SNS | Email báo cáo/cảnh báo |
| CloudWatch | Logs và Error Alarm |
| S3 | Lưu artifact scheduler.zip |
| CloudFormation | IaC triển khai lặp lại |

## Ghi chú IAM

Lambda dùng LabRole có sẵn. Không tạo role mới trong template. Role phải có quyền CloudWatch Logs và các API của EC2/RDS/SageMaker/SNS mà mã thực tế sử dụng.
