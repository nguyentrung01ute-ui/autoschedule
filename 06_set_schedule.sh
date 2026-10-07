#!/usr/bin/env bash
# Đổi nhanh tag Schedule để test bật/tắt.
# Dùng: ./06_set_schedule.sh <ec2|rds|sagemaker|all> "<HH:MM-HH:MM|off>" [Mon-Fri]
# Ví dụ: ./06_set_schedule.sh ec2 "08:00-09:00"      (đặt khung giờ cho EC2)
#        ./06_set_schedule.sh all off                (cả 3 loại luôn tắt)
set -euo pipefail
source "$(dirname "$0")/config.sh" > /dev/null

TARGET="${1:?Thiếu loại tài nguyên: ec2|rds|sagemaker|all}"
SCHED="${2:?Thiếu giá trị Schedule, ví dụ 08:00-17:00 hoặc off}"
DAYS="${3:-$SCHEDULE_DAYS}"

set_ec2() {
  IDS=$(aws ec2 describe-instances \
    --filters Name=tag:Project,Values=$PROJECT Name=instance-state-name,Values=running,stopped \
    --query 'Reservations[].Instances[].InstanceId' --output text)
  [ -z "$IDS" ] && { echo "Không có EC2 nào của project."; return; }
  aws ec2 create-tags --resources $IDS --tags Key=Schedule,Value="$SCHED" Key=ScheduleDays,Value="$DAYS"
  echo "EC2 $IDS -> Schedule=$SCHED ScheduleDays=$DAYS"
}

set_rds() {
  ARN=$(aws rds describe-db-instances --db-instance-identifier autoschedule-db \
    --query 'DBInstances[0].DBInstanceArn' --output text)
  aws rds add-tags-to-resource --resource-name "$ARN" \
    --tags Key=Schedule,Value="$SCHED" Key=ScheduleDays,Value="$DAYS"
  echo "RDS autoschedule-db -> Schedule=$SCHED ScheduleDays=$DAYS"
}

set_sagemaker() {
  ARN=$(aws sagemaker describe-notebook-instance --notebook-instance-name autoschedule-nb \
    --query NotebookInstanceArn --output text)
  aws sagemaker add-tags --resource-arn "$ARN" \
    --tags Key=Schedule,Value="$SCHED" Key=ScheduleDays,Value="$DAYS"
  echo "SageMaker autoschedule-nb -> Schedule=$SCHED ScheduleDays=$DAYS"
}

case "$TARGET" in
  ec2) set_ec2 ;;
  rds) set_rds ;;
  sagemaker) set_sagemaker ;;
  all) set_ec2; set_rds; set_sagemaker ;;
  *) echo "Loại không hợp lệ: $TARGET"; exit 1 ;;
esac
