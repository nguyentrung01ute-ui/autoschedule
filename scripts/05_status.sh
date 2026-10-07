#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/config.sh" > /dev/null

echo "=== CONTEXT ==="
aws sts get-caller-identity
echo "Region : $AWS_DEFAULT_REGION"
date -u '+UTC time: %Y-%m-%d %H:%M:%S UTC'
echo

echo "=== EC2 (managed) ==="
aws ec2 describe-instances   --filters "Name=tag:Project,Values=$PROJECT" "Name=tag-key,Values=Schedule"   --query "Reservations[].Instances[].[InstanceId,InstanceType,State.Name,Tags[?Key=='Schedule']|[0].Value,Tags[?Key=='ScheduleDays']|[0].Value]"   --output table

echo "=== RDS ==="
aws rds describe-db-instances   --query "DBInstances[].[DBInstanceIdentifier,DBInstanceClass,DBInstanceStatus,PubliclyAccessible]"   --output table

echo "=== SageMaker Notebook ==="
aws sagemaker list-notebook-instances   --query "NotebookInstances[].[NotebookInstanceName,InstanceType,NotebookInstanceStatus]"   --output table
