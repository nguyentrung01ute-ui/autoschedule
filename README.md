# AutoSchedule

Tự động bật/tắt EC2, RDS và SageMaker Notebook theo tag Schedule để tiết kiệm ngân sách AWS Learner Lab.

**Môn:** Cloud - Dot 1 - 2026-2027  
**Nhóm:** DevOps & IaC  
**GVHD:** Huỳnh Xuân Phụng  
**Region được phép:** us-east-1 / us-west-2  
**IAM:** dùng LabRole/LabInstanceProfile có sẵn, không tạo IAM user/role mới.

## Mục tiêu

- Lambda Python + boto3 quét tài nguyên được opt-in bằng tag.
- EventBridge kiểm tra lịch mỗi 15 phút.
- Lambda start/stop EC2, RDS và SageMaker Notebook.
- SNS gửi báo cáo tài nguyên đang chạy hằng ngày.
- CloudWatch Logs + Alarm theo dõi lỗi.
- CloudFormation đóng gói hệ thống.
- Có unit test, CI, runbook, worklog, test plan, cost analysis và kịch bản demo.

## Quy ước tag

| Tag | Ví dụ | Ý nghĩa |
|---|---|---|
| Project | AutoSchedule | Chỉ tài nguyên của project mới được quản lý |
| Owner | sv01 | Chủ sở hữu |
| Schedule | 08:00-17:00 / 22:00-06:00 / off | Khung giờ chạy |
| ScheduleDays | Mon-Fri | Ngày chạy |

**An toàn:** Lambda chỉ tác động tài nguyên có cả Project=AutoSchedule và Schedule.

## Cấu trúc

    src/scheduler.py
    infra/template.yaml
    scripts/
      config.sh
      01_setup_s3.sh
      02_create_ec2.sh
      03_create_rds.sh
      04_create_sagemaker.sh
      05_status.sh
      06_set_schedule.sh
      07_deploy.sh
      99_cleanup.sh
    tests/
      test_schedule.py
      events/
    docs/
    worklog/
    PROJECT_PLAN.md

## Tuần 1

Đọc docs/week1-runbook.md trước khi tạo tài nguyên.

Bắt đầu buổi:

    aws sts get-caller-identity
    aws configure get region
    date -u

Sau đó:

    chmod +x scripts/*.sh
    ./scripts/01_setup_s3.sh
    ./scripts/02_create_ec2.sh
    ./scripts/03_create_rds.sh
    ./scripts/04_create_sagemaker.sh
    ./scripts/05_status.sh

Không đánh dấu hoàn thành nếu chưa có ảnh/log minh chứng. Worklog phải ghi giờ thực tế.

## Test local

    pip install -r requirements-dev.txt
    python -m pytest -q

CI chạy unit test và kiểm tra CloudFormation template.

## Deploy

Sau khi Tuần 2 đã test Lambda và SNS:

    export ALERT_EMAIL=your-email@example.com
    ./scripts/07_deploy.sh

Script tạo artifact Lambda có tên riêng theo thời gian, upload lên S3 rồi truyền CodeKey mới cho CloudFormation. Sau deploy phải xác nhận email SNS.

## Dọn dẹp

    ./scripts/99_cleanup.sh --bucket

Kiểm tra thêm EBS, snapshot, Elastic IP và tài nguyên còn sót.

## Tài liệu dự án

- PROJECT_PLAN.md: kế hoạch 4 tuần và Definition of Done.
- docs/ROADMAP.md: tiến độ và mốc kiểm soát.
- docs/week1-runbook.md: hướng dẫn thực hành Tuần 1.
- docs/test-plan.md: unit/integration test.
- docs/iam-requirements.md: quyền LabRole.
- docs/cost-analysis.md: cách tính chi phí.
- docs/demo-script.md: kịch bản video <= 10 phút.
- docs/report.md: khung báo cáo cuối kỳ.

## Lưu ý AWS

RDS stop chỉ là tạm thời: AWS tự khởi động DB sau tối đa 7 ngày. Đây là giới hạn thiết kế cần nêu trong báo cáo.

Chu kỳ EventBridge 15 phút giúp giảm số lần gọi nhưng tạo độ trễ tối đa theo chu kỳ. Khi cần demo nhanh, có thể truyền EnforceSchedule khác vào CloudFormation, nhưng phải ghi rõ cấu hình thực tế.

## AI

Đề cho phép dùng LLM. Báo cáo phải ghi phần AI hỗ trợ và phần sinh viên đã đọc, triển khai, kiểm thử và giải thích được.
