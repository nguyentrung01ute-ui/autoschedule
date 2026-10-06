#!/usr/bin/env bash
# Cấu hình chung. Sửa OWNER cho đúng tên/mã SV của bạn.
export AWS_DEFAULT_REGION=us-east-1
export PROJECT=AutoSchedule
export OWNER=sv01
export SCHEDULE="08:00-17:00"
export SCHEDULE_DAYS="Mon-Fri"

export ACC=$(aws sts get-caller-identity --query Account --output text)
export LAB_ROLE_ARN=$(aws iam get-role --role-name LabRole --query Role.Arn --output text)
export BUCKET="autoschedule-$ACC"

echo "Account : $ACC"
echo "Region  : $AWS_DEFAULT_REGION"
echo "LabRole : $LAB_ROLE_ARN"
echo "Bucket  : $BUCKET"
echo "Time    : $(date '+%Y-%m-%d %H:%M:%S %Z')"
