># AutoSchedule

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
<img width="1682" height="1051" alt="autoschedule-infrastructure (1)" src="https://github.com/user-attachments/assets/f8694fa8-2dcd-4fb6-9f6a-a4ade1fecf15" />



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

Đọc docs/week1-runbook.md trước khi tạo tài nguyên. Ảnh minh chứng và chú thích được quản lý tại [docs/week1-evidence.md](docs/week1-evidence.md); đặt các file PNG trong `docs/screenshots/` theo đúng tên trong bảng.

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

Ảnh minh chứng đã được lưu trong `docs/screenshots/`. Danh mục Tuần 1 ở [docs/week1-evidence.md](docs/week1-evidence.md), danh mục 34 ảnh Tuần 2 ở [docs/week2-evidence.md](docs/week2-evidence.md), danh mục 34 ảnh Tuần 3 ở [docs/week3-evidence.md](docs/week3-evidence.md). Trước khi nộp, cần mở và đối chiếu ảnh thực tế với nội dung báo cáo, đặc biệt các cấu hình IAM/LabRole; không tự tạo ngày hoặc minh chứng.

## Test local

    pip install -r requirements-dev.txt
    python -m pytest -q

CI chạy unit test và kiểm tra CloudFormation template.

## Deploy

Sau khi Tuần 2 đã test Lambda và SNS:

    export ALERT_EMAIL=your-email@example.com
    ./scripts/07_deploy.sh

Script tạo artifact Lambda có tên riêng theo thời gian, upload lên S3 rồi truyền CodeKey mới cho CloudFormation. Sau deploy phải xác nhận email SNS.

## Tuần 4

Kiểm thử tổng thể toàn hệ thống (end-to-end), đánh giá chi phí & mức tiết kiệm, quay video demo, hoàn thiện báo cáo cuối kỳ và dọn dẹp toàn bộ tài nguyên để không phát sinh chi phí ngoài ý muốn:

1. **Dựng lại hệ thống từ đầu bằng một lệnh (`INT-15`):**
   Xóa stack `autoschedule` cũ rồi chạy lại lệnh triển khai tự động:

       aws cloudformation delete-stack --stack-name autoschedule
       aws cloudformation wait stack-delete-complete --stack-name autoschedule
       export ALERT_EMAIL=your-email@example.com
       ./scripts/07_deploy.sh

   Sau khi stack đạt `CREATE_COMPLETE`, xác nhận lại subscription trong email SNS và chạy test event `{"action":"report"}` để kiểm tra nhận email báo cáo tài nguyên đang chạy.

2. **Kiểm thử end-to-end với lịch ngắn cho cả 3 loại tài nguyên (`INT-16a`, `INT-16b`):**
   Khi cả 3 tài nguyên (EC2, RDS, SageMaker Notebook) đang ở trạng thái `Stopped`, đặt khung giờ ngắn bao trùm giờ hiện tại và chờ chu kỳ EventBridge (`rate(15 minutes)`) tự kích hoạt:

       ./scripts/06_set_schedule.sh all "08:00-23:59" Mon-Sun
       ./scripts/05_status.sh

   - **Chu kỳ tự bật (`INT-16a`):** Không gọi Lambda thủ công; chờ EventBridge tự gọi Lambda `START` cả 3 tài nguyên và theo dõi đến khi đạt trạng thái ổn định (`EC2 Running`, `RDS Available`, `SageMaker InService`).
   - **Chu kỳ tự tắt (`INT-16b`):** Đổi lịch sang khung giờ ngoài giờ hiện tại, chờ chu kỳ EventBridge tiếp theo tự gọi `STOP` cả 3 tài nguyên và kiểm tra lại bằng `./scripts/05_status.sh`:

       ./scripts/06_set_schedule.sh all "08:00-09:00" Mon-Sun
       ./scripts/05_status.sh

3. **Kiểm thử lỗi & Alarm, phân tích chi phí và hoàn thiện hồ sơ:**
   - Kiểm thử các tình huống biên/lỗi: tag `Schedule=abc` sai định dạng (`INT-17`), bỏ qua tài nguyên đang chuyển trạng thái `Starting` (`INT-18`), và gây lỗi `TOPIC_ARN` sai để kích hoạt CloudWatch Alarm `autoschedule-errors` gửi email cảnh báo rồi tự phục hồi về `OK` (`INT-19`).
   - Đối chiếu ngân sách AWS Learner Lab và ước tính chi phí trên AWS Pricing Calculator (giảm ~73% giờ chạy so với chạy 24/7).
   - Tổng hợp báo cáo tại [reports/Bao_cao_tuan4_Nhom_DevOps_IaC.docx](reports/Bao_cao_tuan4_Nhom_DevOps_IaC.docx), cập nhật [worklog/week4.md](worklog/week4.md) và quay video demo (≤ 10 phút).

## Dọn dẹp

Thực hiện dọn dẹp sau khi đã chụp đủ ảnh minh chứng, quay xong video demo và commit toàn bộ mã nguồn, tài liệu lên Git:

1. **Xóa stack CloudFormation `autoschedule`:**
   Xóa kèm Lambda `autoschedule`, SNS topic & subscription, 2 EventBridge rule, CloudWatch Log Group và Alarm `autoschedule-errors`:

       aws cloudformation delete-stack --stack-name autoschedule
       aws cloudformation wait stack-delete-complete --stack-name autoschedule

2. **Xóa các tài nguyên mẫu và S3 bucket chứa artifact:**
   Chạy script dọn dẹp để terminate EC2 `autoschedule-ec2` (cùng EBS volume), xóa RDS `autoschedule-db` (`--skip-final-snapshot`), dừng và xóa SageMaker Notebook `autoschedule-nb`, đồng thời xóa S3 bucket:

       ./scripts/99_cleanup.sh --bucket

3. **Xóa tài nguyên tạo thủ công ngoài stack (nếu còn):**
   - Xóa CloudWatch Dashboard `autoschedule-dashboard` (CloudWatch → Dashboards → Delete).
   - Kiểm tra EventBridge Scheduler (`autoschedule-enforce-manual`, `autoschedule-report-manual`), nếu còn thì xóa.

4. **Kiểm tra tay trên AWS Console (`us-east-1`) để tránh sót tài nguyên tính phí:**
   - **CloudFormation:** Không còn stack `autoschedule`.
   - **EC2:** Instances, Volumes, Snapshots, Elastic IPs đều trống.
   - **RDS:** Databases và Manual/Automated Snapshots đều trống.
   - **SageMaker:** Notebook instances trống.
   - **S3:** Không còn bucket `autoschedule-<ACCOUNT_ID>-us-east-1`.
   - **CloudWatch / SNS / EventBridge:** Không còn dashboard, log group, alarm, topic hay rule/schedule của dự án.
   - Kiểm tra mục ngân sách Learner Lab (`Used ... of $50`) rồi chọn **End Lab** khi kết thúc phiên làm việc.

## Tài liệu dự án

- PROJECT_PLAN.md: kế hoạch 4 tuần và Definition of Done.
- docs/ROADMAP.md: tiến độ và mốc kiểm soát.
- docs/week1-runbook.md: hướng dẫn thực hành Tuần 1.
- docs/week1-evidence.md, docs/week2-evidence.md và docs/week3-evidence.md: danh mục ảnh minh chứng.
- worklog/week1.md, worklog/week2.md, worklog/week3.md và worklog/week4.md: nhiệm vụ, thời lượng và liên kết minh chứng 4 tuần.
- docs/test-plan.md: unit/integration test.
- docs/iam-requirements.md: quyền LabRole.
- docs/cost-analysis.md: cách tính chi phí.
- docs/demo-script.md: kịch bản video <= 10 phút.
- docs/report.md: khung báo cáo cuối kỳ.

## Lưu ý AWS

RDS stop chỉ là tạm thời: AWS tự khởi động DB sau tối đa 7 ngày. Đây là giới hạn thiết kế cần nêu trong báo cáo.

Chu kỳ EventBridge 15 phút giúp giảm số lần gọi nhưng tạo độ trễ tối đa theo chu kỳ. Khi cần demo nhanh, có thể truyền EnforceSchedule khác vào CloudFormation, nhưng phải ghi rõ cấu hình thực tế.

## AI

Đề cho phép dùng LLM. Báo cáo có sử dụng Claude mô hình 5.5 và Chat GPT hổ trợ tham khảo và fix các lỗi.
