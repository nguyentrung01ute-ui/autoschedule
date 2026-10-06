# AutoSchedule

Tự động bật/tắt EC2, RDS, SageMaker Notebook theo tag `Schedule` để tiết kiệm ngân sách AWS Learner Lab.
Lambda (boto3) + EventBridge + SNS + CloudWatch, đóng gói bằng CloudFormation.

Mô tả chi tiết và kế hoạch 4 tuần: [PROJECT_PLAN.md](PROJECT_PLAN.md)

## Cấu trúc
- `src/scheduler.py`: mã Lambda
- `infra/template.yaml`: template CloudFormation
- `tests/test_schedule.py`: unit test logic lịch
- `docs/`: sơ đồ kiến trúc, ảnh minh chứng, báo cáo
- `worklog/`: nhật ký công việc hằng tuần

## Chạy test
```bash
pip install pytest boto3
python -m pytest
```

## Triển khai (us-east-1)
```bash
ACC=$(aws sts get-caller-identity --query Account --output text)
aws s3 mb s3://autoschedule-$ACC --region us-east-1
cd src && zip ../scheduler.zip scheduler.py && cd ..
aws s3 cp scheduler.zip s3://autoschedule-$ACC/ --region us-east-1
aws cloudformation deploy --stack-name autoschedule \
  --template-file infra/template.yaml \
  --parameter-overrides LabRoleArn=arn:aws:iam::$ACC:role/LabRole \
    CodeBucket=autoschedule-$ACC AlertEmail=<email> OwnerTag=<ten> \
  --region us-east-1
```
Sau khi deploy, mở email và bấm **Confirm subscription**.

## Quy ước tag
| Tag | Ví dụ | Ý nghĩa |
|---|---|---|
| `Schedule` | `08:00-17:00`, `off` | Khung giờ chạy |
| `ScheduleDays` | `Mon-Fri` | Ngày chạy (mặc định cả tuần) |
| `Project`, `Owner` | `AutoSchedule`, `sv01` | Bắt buộc |
