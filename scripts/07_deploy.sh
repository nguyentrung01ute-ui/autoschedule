#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
source "$ROOT/scripts/config.sh" > /dev/null
: "${ALERT_EMAIL:?Set ALERT_EMAIL before deploy, e.g. export ALERT_EMAIL=you@example.com}"

cd "$ROOT"
rm -f scheduler.zip
(cd src && zip -q "../scheduler.zip" scheduler.py)

CODE_KEY="artifacts/scheduler-$(date -u '+%Y%m%d-%H%M%S').zip"
aws s3 cp scheduler.zip "s3://$BUCKET/$CODE_KEY" --region "$AWS_DEFAULT_REGION"

aws cloudformation deploy   --stack-name autoschedule   --template-file infra/template.yaml   --parameter-overrides     LabRoleArn="$LAB_ROLE_ARN"     CodeBucket="$BUCKET"     CodeKey="$CODE_KEY"     AlertEmail="$ALERT_EMAIL"     ProjectTag="$PROJECT"     OwnerTag="$OWNER"   --region "$AWS_DEFAULT_REGION"

echo "Deploy complete. Confirm the SNS email subscription."
aws cloudformation describe-stacks   --stack-name autoschedule   --query 'Stacks[0].Outputs'   --output table
