# Ảnh minh chứng AWS — AutoSchedule

Thư mục này lưu ảnh minh chứng thực tế cho các tuần thực hành.

## Tuần 1

- Ảnh minh chứng theo danh mục: [docs/week1-evidence.md](../week1-evidence.md)
- Các ảnh có tiền tố `week1-evidence-` và sơ đồ `autoschedule-infrastructure.png`.

## Tuần 2

- Danh mục đầy đủ 34 ảnh và mô tả: [docs/week2-evidence.md](../week2-evidence.md)
- Worklog và nhiệm vụ từng thành viên: [worklog/week2.md](../../worklog/week2.md)
- Ảnh được đánh số từ `week2-evidence-01-pytest-11-passed.png` đến `week2-evidence-34-report-email.png`.
- Bộ ảnh bao gồm pytest, xác nhận SNS, cấu hình Lambda, kiểm thử START/STOP EC2, kiểm thử tag hợp lệ/không hợp lệ/`off`/thiếu tag, log enforce và email báo cáo SNS; ngoài ra có minh chứng RDS và SageMaker.

## Tuần 3

- Danh mục đầy đủ 34 ảnh và mô tả: [docs/week3-evidence.md](../week3-evidence.md)
- Worklog và nhiệm vụ từng thành viên: [worklog/week3.md](../../worklog/week3.md)
- Ảnh được đánh số từ `week3-evidence-01.png` đến `week3-evidence-35.png` (trong đó có `week3-evidence-12a.png` và `week3-evidence-12b.png`).
- Bộ ảnh bao gồm: tạo lịch EventBridge Scheduler thủ công, kiểm thử tự động kích hoạt START/STOP EC2 và gửi email báo cáo SNS, xóa tài nguyên thủ công, triển khai CloudFormation template và xác nhận subscription, rà soát 10 hạng mục bảo mật (mã nguồn, RDS, S3, Security Group, Lambda, CloudWatch retention), thiết lập CloudWatch Dashboard và kiểm thử gây lỗi CloudWatch Error Alarm kích hoạt cảnh báo SNS.

## Tuần 4

- Danh mục ảnh và mô tả: [docs/week4-evidence.md](../week4-evidence.md)
- Worklog và nhiệm vụ từng thành viên: [worklog/week4.md](../../worklog/week4.md)
- Hình 10–16 (Nguyễn Văn Thi): `week4-evidence-10.png`, `-11.png`, `-12.jpg`, `-13.jpg`, `-14.jpg`, `-15.png`, `-16.png` — test tag sai (INT-17), tài nguyên đang chuyển trạng thái (INT-18), Alarm `In alarm` → email → `OK` (INT-19), ngân sách Learner Lab và AWS Pricing Calculator.
- Hình 10–14 dùng lại từ Tuần 2 (Hình 25, 19) và Tuần 3 (Hình 33–35), đã ghi nguồn.
- Hình 01–09 (dựng lại stack, test end-to-end) do Nguyễn Văn Trung bổ sung.

## Kiểm tra trước khi nộp

- Mở từng ảnh và xác nhận trạng thái, tag, log và nội dung hiển thị đọc được.
- Đối chiếu số hình trong báo cáo Word với bảng tại [docs/week2-evidence.md](../week2-evidence.md), [docs/week3-evidence.md](../week3-evidence.md) và [docs/week4-evidence.md](../week4-evidence.md).
- Không commit access key, secret key, session token hoặc thông tin nhạy cảm.
- Chỉ dùng ảnh chụp/log thực tế; không tạo ảnh minh họa thay cho kết quả AWS.
