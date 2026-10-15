#!/usr/bin/env bash
# Tạo RDS MySQL mẫu (db.t3.micro, 20 GB gp3, Single-AZ, non-public) phục vụ dự án AutoSchedule.
set -euo pipefail
source "$(dirname "$0")/config.sh"

DB_ID="autoschedule-db"

echo "=== Khởi tạo RDS MySQL mẫu: $DB_ID ==="

# Kiểm tra nếu DB instance đã tồn tại
EXISTING_STATUS=$(aws rds describe-db-instances --db-instance-identifier "$DB_ID" --query 'DBInstances[0].DBInstanceStatus' --output text 2>/dev/null || true)

if [ -n "$EXISTING_STATUS" ] && [ "$EXISTING_STATUS" != "None" ]; then
  echo "RDS instance '$DB_ID' đã tồn tại với trạng thái: $EXISTING_STATUS"
else
  if [ -n "${DB_PASSWORD:-}" ]; then
    PASS_ARGS=(--master-user-password "$DB_PASSWORD")
  else
    PASS_ARGS=(--manage-master-user-password)
  fi

  echo "Đang gửi yêu cầu tạo RDS instance '$DB_ID'..."
  aws rds create-db-instance \
    --db-instance-identifier "$DB_ID" \
    --db-instance-class db.t3.micro \
    --engine mysql \
    --allocated-storage 20 \
    --storage-type gp3 \
    --master-username admin "${PASS_ARGS[@]}" \
    --no-publicly-accessible \
    --no-multi-az \
    --backup-retention-period 0 \
    --tags Key=Project,Value="$PROJECT" Key=Owner,Value="$OWNER" Key=Schedule,Value="$SCHEDULE" Key=ScheduleDays,Value="$SCHEDULE_DAYS" \
    --query 'DBInstance.DBInstanceStatus' \
    --output text

  echo "Yêu cầu tạo RDS đã được gửi thành công."
fi

echo ""
echo "Để theo dõi trạng thái tạo RDS (mất khoảng 5-10 phút để đạt Available):"
echo "aws rds describe-db-instances --db-instance-identifier $DB_ID --query 'DBInstances[0].[DBInstanceIdentifier,DBInstanceStatus,DBInstanceClass,PubliclyAccessible]' --output table"
