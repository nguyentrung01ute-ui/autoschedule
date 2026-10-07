#!/usr/bin/env bash
set -euo pipefail

export AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION:-us-east-1}"
case "$AWS_DEFAULT_REGION" in
  us-east-1|us-west-2) ;;
  *) echo "ERROR: only us-east-1/us-west-2 is allowed."; exit 1 ;;
esac

export PROJECT="${PROJECT:-AutoSchedule}"
export OWNER="${OWNER:-sv01}"
export SCHEDULE="${SCHEDULE:-08:00-17:00}"
export SCHEDULE_DAYS="${SCHEDULE_DAYS:-Mon-Fri}"

export ACC="$(aws sts get-caller-identity --query Account --output text)"
export LAB_ROLE_ARN="$(aws iam get-role --role-name LabRole --query Role.Arn --output text)"
export BUCKET="autoschedule-$ACC-${AWS_DEFAULT_REGION}"

echo "Account : $ACC"
echo "Region  : $AWS_DEFAULT_REGION"
echo "LabRole : $LAB_ROLE_ARN"
echo "Project : $PROJECT"
echo "Owner   : $OWNER"
echo "Schedule: $SCHEDULE ($SCHEDULE_DAYS)"
echo "Time    : $(date '+%Y-%m-%d %H:%M:%S %Z')"
