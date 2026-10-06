#!/usr/bin/env bash
# Tạo S3 bucket chứa mã Lambda: có tag, chặn truy cập public, mã hóa mặc định.
set -euo pipefail
source "$(dirname "$0")/config.sh"

aws s3 mb "s3://$BUCKET" --region "$AWS_DEFAULT_REGION" || echo "Bucket đã tồn tại, tiếp tục."

aws s3api put-bucket-tagging --bucket "$BUCKET" \
  --tagging "TagSet=[{Key=Project,Value=$PROJECT},{Key=Owner,Value=$OWNER}]"

aws s3api put-public-access-block --bucket "$BUCKET" \
  --public-access-block-configuration \
  BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true

aws s3api put-bucket-encryption --bucket "$BUCKET" \
  --server-side-encryption-configuration \
  '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"}}]}'

echo "Xong. Chụp màn hình Bucket > Properties/Permissions làm minh chứng."
