# Kịch bản demo tối đa 10 phút

## 0:00-1:00 — Bài toán
Nêu vấn đề: tài nguyên Learner Lab có thể chạy ngoài giờ học và làm tiêu hao ngân sách.

## 1:00-2:00 — Kiến trúc
Giải thích EventBridge -> Lambda -> EC2/RDS/SageMaker; SNS báo cáo; CloudWatch log/alarm; CloudFormation IaC.

## 2:00-3:00 — Tag
Mở một tài nguyên và chỉ ra Project, Owner, Schedule, ScheduleDays.

## 3:00-4:00 — Lambda
Mở scheduler.py và giải thích desired_running, collect, enforce, report.

## 4:00-5:30 — CloudFormation
Mở template và chỉ ra Lambda dùng LabRole ARN có sẵn, 2 EventBridge rule, SNS, LogGroup, Alarm.

## 5:30-7:30 — Chạy thật
Đổi Schedule sát giờ hiện tại, invoke Lambda hoặc chờ EventBridge, quan sát trạng thái tài nguyên và CloudWatch Logs.

## 7:30-8:30 — Báo cáo
Cho xem email SNS liệt kê tài nguyên đang chạy.

## 8:30-9:15 — Chi phí
Trình bày số giờ chạy theo lịch so với 24/7 và cách tính.

## 9:15-10:00 — Giới hạn
Nêu RDS tự start sau tối đa 7 ngày, LabRole có thể bị AccessDenied và độ trễ tối đa của chu kỳ 15 phút.
