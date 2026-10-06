#!/usr/bin/env bash
# Xem trạng thái + tag của cả 3 tài nguyên (chụp làm minh chứng).
source "$(dirname "$0")/config.sh" > /dev/null
echo "=== EC2 ==="
aws ec2 describe-instances --filters Name=tag-key,Values=Schedule Name=instance-state-name,Values=pending,running,stopping,stopped \
  --query 'Reservations[].Instances[].[InstanceId,InstanceType,State.Name,Tags[?Key==`Schedule`]|[0].Value]' --output table
echo "=== RDS ==="
aws rds describe-db-instances --query 'DBInstances[].[DBInstanceIdentifier,DBInstanceClass,DBInstanceStatus]' --output table
echo "=== SageMaker ==="
aws sagemaker list-notebook-instances --query 'NotebookInstances[].[NotebookInstanceName,InstanceType,NotebookInstanceStatus]' --output table
