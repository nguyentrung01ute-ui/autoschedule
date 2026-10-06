#!/usr/bin/env bash
# Tạo RDS MySQL db.t3.micro 20 GB (không public, không Multi-AZ).
# Mặc định để RDS tự quản lý mật khẩu (Secrets Manager).
# Nếu Learner Lab chặn Secrets Manager: export DB_PASSWORD='MatKhau12345' rồi chạy lại.
set -euo pipefail
source "$(dirname "$0")/config.sh"

if [ -n "${DB_PASSWORD:-}" ]; then
  PASS_ARGS=(--master-user-password "$DB_PASSWORD")
else
  PASS_ARGS=(--manage-master-user-password)
fi

aws rds create-db-instance \
  --db-instance-identifier autoschedule-db \
  --db-instance-class db.t3.micro \
  --engine mysql \
  --allocated-storage 20 --storage-type gp3 \
  --master-username admin "${PASS_ARGS[@]}" \
  --no-publicly-accessible --no-multi-az \
  --backup-retention-period 0 \
  --tags Key=Project,Value=$PROJECT Key=Owner,Value=$OWNER Key=Schedule,Value=$SCHEDULE Key=ScheduleDays,Value=$SCHEDULE_DAYS \
  --query 'DBInstance.DBInstanceStatus' --output text

echo "RDS đang tạo (mất khoảng 5-10 phút). Theo dõi:"
echo "aws rds describe-db-instances --db-instance-identifier autoschedule-db --query 'DBInstances[0].DBInstanceStatus'"
