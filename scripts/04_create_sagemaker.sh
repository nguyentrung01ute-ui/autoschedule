#!/usr/bin/env bash
# Tạo SageMaker Notebook Instance mẫu (ml.t3.medium, 5GB, LabRole) phục vụ dự án AutoSchedule.
set -euo pipefail
source "$(dirname "$0")/config.sh"

NB_NAME="autoschedule-nb"

echo "=== Khởi tạo SageMaker Notebook Instance mẫu: $NB_NAME ==="

# Kiểm tra nếu Notebook instance đã tồn tại
EXISTING_STATUS=$(aws sagemaker describe-notebook-instance --notebook-instance-name "$NB_NAME" --query 'NotebookInstanceStatus' --output text 2>/dev/null || true)

if [ -n "$EXISTING_STATUS" ] && [ "$EXISTING_STATUS" != "None" ]; then
  echo "SageMaker Notebook '$NB_NAME' đã tồn tại với trạng thái: $EXISTING_STATUS"
else
  echo "Sử dụng IAM Role ARN: $LAB_ROLE_ARN"
  echo "Đang gửi yêu cầu tạo SageMaker Notebook '$NB_NAME'..."

  aws sagemaker create-notebook-instance \
    --notebook-instance-name "$NB_NAME" \
    --instance-type ml.t3.medium \
    --role-arn "$LAB_ROLE_ARN" \
    --volume-size-in-gb 5 \
    --tags Key=Project,Value="$PROJECT" Key=Owner,Value="$OWNER" Key=Schedule,Value="$SCHEDULE" Key=ScheduleDays,Value="$SCHEDULE_DAYS"

  echo "Yêu cầu tạo SageMaker Notebook đã được gửi thành công."
fi

echo ""
echo "Để theo dõi trạng thái tạo Notebook (mất khoảng 3-5 phút để đạt InService):"
echo "aws sagemaker describe-notebook-instance --notebook-instance-name $NB_NAME --query '[NotebookInstanceName,NotebookInstanceStatus,InstanceType,DefaultCodeRepository]' --output table"
