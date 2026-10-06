#!/usr/bin/env bash
# Dọn tài nguyên mẫu. Dùng: ./99_cleanup.sh          (xóa EC2, RDS, SageMaker)
#                          ./99_cleanup.sh --bucket  (xóa luôn S3 bucket)
set -uo pipefail
source "$(dirname "$0")/config.sh" > /dev/null

IDS=$(aws ec2 describe-instances \
  --filters Name=tag:Project,Values=$PROJECT Name=instance-state-name,Values=pending,running,stopping,stopped \
  --query 'Reservations[].Instances[].InstanceId' --output text)
[ -n "$IDS" ] && aws ec2 terminate-instances --instance-ids $IDS --query 'TerminatingInstances[].InstanceId' --output text

aws rds delete-db-instance --db-instance-identifier autoschedule-db --skip-final-snapshot --delete-automated-backups \
  --query 'DBInstance.DBInstanceStatus' --output text 2>&1 | tail -1

STATUS=$(aws sagemaker describe-notebook-instance --notebook-instance-name autoschedule-nb --query NotebookInstanceStatus --output text 2>/dev/null)
if [ -n "$STATUS" ]; then
  [ "$STATUS" = "InService" ] && aws sagemaker stop-notebook-instance --notebook-instance-name autoschedule-nb
  echo "Đợi notebook dừng hẳn..."
  aws sagemaker wait notebook-instance-stopped --notebook-instance-name autoschedule-nb
  aws sagemaker delete-notebook-instance --notebook-instance-name autoschedule-nb
fi

if [ "${1:-}" = "--bucket" ]; then
  aws s3 rb "s3://$BUCKET" --force
fi
echo "Xong. Kiểm tra lại EBS volume, snapshot, Elastic IP còn sót trong console."
