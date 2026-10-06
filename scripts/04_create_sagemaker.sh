#!/usr/bin/env bash
# Tạo SageMaker Notebook Instance (role LabRole).
set -euo pipefail
source "$(dirname "$0")/config.sh"

aws sagemaker create-notebook-instance \
  --notebook-instance-name autoschedule-nb \
  --instance-type ml.t3.medium \
  --role-arn "$LAB_ROLE_ARN" \
  --volume-size-in-gb 5 \
  --tags Key=Project,Value=$PROJECT Key=Owner,Value=$OWNER Key=Schedule,Value=$SCHEDULE Key=ScheduleDays,Value=$SCHEDULE_DAYS

echo "Notebook đang tạo (khoảng 3-5 phút). Theo dõi:"
echo "aws sagemaker describe-notebook-instance --notebook-instance-name autoschedule-nb --query NotebookInstanceStatus"
