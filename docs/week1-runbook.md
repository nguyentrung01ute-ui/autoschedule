# Runbook Tuần 1

## Mục tiêu
Đến cuối tuần 1 phải có Region hợp lệ, S3 bucket, EC2/RDS/SageMaker mẫu, tag Project/Owner/Schedule/ScheduleDays, sơ đồ, minh chứng và worklog.

## Bắt đầu buổi học
    aws sts get-caller-identity
    aws configure get region
    date -u

Chụp ảnh kết quả để chứng minh Account ID, Region và thời gian.

## Chuẩn bị repo
    git clone https://github.com/nguyentrung01ute-ui/autoschedule.git
    cd autoschedule
    chmod +x scripts/*.sh

Sửa OWNER trong scripts/config.sh thành mã SV thật.

## Dựng nền tảng
    ./scripts/01_setup_s3.sh
    ./scripts/02_create_ec2.sh
    ./scripts/03_create_rds.sh
    ./scripts/04_create_sagemaker.sh
    ./scripts/05_status.sh

Chờ RDS available và SageMaker InService trước khi chụp minh chứng.

## Minh chứng
Chụp Account ID, Region, thời gian, trạng thái và tag của 3 loại tài nguyên. Lưu ảnh vào docs/screenshots với tên rõ ràng.

## Dọn cuối buổi
Nếu không cần giữ cho buổi sau, dừng tài nguyên. Khi kết thúc hẳn tuần 1:
    ./scripts/99_cleanup.sh --bucket

Sau đó kiểm tra EBS, snapshot, Elastic IP và tài nguyên còn sót.

## Quy tắc worklog
Chỉ ghi số giờ thực tế. Không đánh dấu PASS nếu chưa có ảnh/log/trạng thái thực tế.
