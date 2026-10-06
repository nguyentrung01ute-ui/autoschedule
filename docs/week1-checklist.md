# Checklist Tuần 1

Chạy trong CloudShell, region us-east-1. Mở đầu mỗi buổi: `aws sts get-caller-identity` rồi chụp màn hình.

```bash
git clone https://github.com/nguyentrung01ute-ui/autoschedule.git && cd autoschedule/scripts
chmod +x *.sh
./01_setup_s3.sh
./02_create_ec2.sh
./03_create_rds.sh
./04_create_sagemaker.sh
./05_status.sh
```

- [ ] Sửa `OWNER` trong `scripts/config.sh`
- [ ] S3 bucket có tag, Block Public Access, mã hóa
- [ ] EC2 chạy, có tag Project/Owner/Schedule/ScheduleDays
- [ ] RDS `available`, có tag
- [ ] SageMaker Notebook `InService`, có tag
- [ ] Sơ đồ kiến trúc (docs/architecture.md) đã chụp ảnh
- [ ] Ảnh console có Account ID, Region, thời gian
- [ ] `worklog/week1.md` đã điền
- [ ] Cuối buổi: `./99_cleanup.sh` hoặc dừng tài nguyên
