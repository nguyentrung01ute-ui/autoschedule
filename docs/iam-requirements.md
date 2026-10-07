# Quyền cần có của LabRole

AutoSchedule không tạo IAM user/role mới. CloudFormation nhận ARN của role có sẵn trong Learner Lab và gán role đó cho Lambda.

Lambda cần quyền tương ứng với các API:
- CloudWatch Logs: tạo/ghi log.
- EC2: describe, start, stop instances.
- RDS: describe DB instances, list tags, start, stop.
- SageMaker: list notebook instances, list tags, start, stop.
- SNS: publish báo cáo.

Nếu LabRole thiếu quyền, ghi nhận lỗi thực tế vào worklog/báo cáo và báo GVHD. Không tự tạo IAM role mới.

AWS yêu cầu execution role của Lambda có trust policy cho lambda.amazonaws.com.
