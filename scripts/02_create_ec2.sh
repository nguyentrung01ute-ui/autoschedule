#!/usr/bin/env bash
# Tạo 1 EC2 t3.nano (VPC mặc định) có tag Schedule.
set -euo pipefail
source "$(dirname "$0")/config.sh"

ID=$(aws ec2 run-instances \
  --instance-type t3.nano --count 1 \
  --image-id resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64 \
  --block-device-mappings 'DeviceName=/dev/xvda,Ebs={VolumeSize=8,VolumeType=gp3}' \
  --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=autoschedule-ec2},{Key=Project,Value=$PROJECT},{Key=Owner,Value=$OWNER},{Key=Schedule,Value=$SCHEDULE},{Key=ScheduleDays,Value=$SCHEDULE_DAYS}]" \
            "ResourceType=volume,Tags=[{Key=Project,Value=$PROJECT},{Key=Owner,Value=$OWNER}]" \
  --query 'Instances[0].InstanceId' --output text)

echo "EC2 đã tạo: $ID"
