# Runbook Vận Hành và Kiểm Thử Tuần 1 — AutoSchedule

Tài liệu hướng dẫn chi tiết quy trình thiết lập, kiểm tra trạng thái và thu thập minh chứng cho hạ tầng nền tảng trong Tuần 1 trên môi trường **AWS Learner Lab**.

---

## 1. Mục Tiêu Tuần 1

- Xác thực Region hoạt động hợp lệ (`us-east-1` hoặc `us-west-2`) và quyền thực thi thông qua `LabRole`.
- Dựng S3 bucket lưu trữ deployment package của Lambda.
- Dựng 3 loại tài nguyên mẫu phục vụ kiểm thử:
  1. EC2 Instance (`autoschedule-ec2`, loại `t3.nano`).
  2. RDS MySQL (`autoschedule-db`, loại `db.t3.micro`).
  3. SageMaker Notebook Instance (`autoschedule-nb`, loại `ml.t3.medium`).
- Gắn đầy đủ bộ 4 tag chuẩn: `Project=AutoSchedule`, `Owner=<MSSV>`, `Schedule=08:00-17:00`, `ScheduleDays=Mon-Fri`.
- Thu thập đủ 16 ảnh minh chứng thực tế trên AWS Console theo danh mục.

---

## 2. Bắt Đầu Buổi Thực Hành (Pre-flight Checks)

Mở AWS CloudShell hoặc terminal local đã cấu hình AWS CLI tương ứng với phiên AWS Learner Lab:

```bash
# 1. Kiểm tra Account ID và thông tin xác thực hiện tại
aws sts get-caller-identity

# 2. Kiểm tra Region hiện tại (phải là us-east-1 hoặc us-west-2)
aws configure get region

# 3. Đồng bộ thời gian thực hành theo chuẩn UTC
date -u '+UTC time: %Y-%m-%d %H:%M:%S UTC'

# 4. Kiểm tra sự tồn tại của IAM role LabRole bắt buộc
aws iam get-role --role-name LabRole --query 'Role.[RoleName,Arn]' --output table
```

> **Lưu ý minh chứng:** Chụp ảnh màn hình terminal hiển thị đầy đủ lệnh và kết quả (Account ID, Region, thời gian UTC) để làm minh chứng xác thực tài khoản.

---

## 3. Chuẩn Bị Kho Mã Nguồn (Repository Setup)

```bash
# Clone repository dự án
git clone https://github.com/nguyentrung01ute-ui/autoschedule.git
cd autoschedule

# Cấp quyền thực thi cho toàn bộ script
chmod +x scripts/*.sh

# Kiểm tra và cập nhật mã sinh viên trong file cấu hình
# Sửa OWNER trong scripts/config.sh thành mã SV của bạn (ví dụ: 24110365 hoặc 24110334)
nano scripts/config.sh
```

Kiểm tra nội dung file cấu hình chung `scripts/config.sh`:
- `PROJECT="AutoSchedule"`
- `SCHEDULE="08:00-17:00"`
- `SCHEDULE_DAYS="Mon-Fri"`
- `AWS_DEFAULT_REGION="us-east-1"`

---

## 4. Quy Trình Khởi Tạo Tài Nguyên Mẫu (Provisioning)

Chạy tuần tự các script theo đúng thứ tự thiết kế:

### Bước 4.1: Tạo S3 Bucket lưu trữ
```bash
./scripts/01_setup_s3.sh
```
*Mục tiêu kiểm tra:* S3 bucket được tạo với tên `autoschedule-<ACCOUNT_ID>-<REGION>`, kích hoạt `Block all public access` và bật mã hóa mặc định SSE-S3.

### Bước 4.2: Tạo EC2 Instance mẫu
```bash
./scripts/02_create_ec2.sh
```
*Mục tiêu kiểm tra:* Instance `autoschedule-ec2` chạy trên nền Amazon Linux 2023, phân vùng EBS 8 GiB gp3, gắn đủ 4 tag trên cả instance và volume.

### Bước 4.3: Tạo RDS MySQL Instance mẫu
```bash
./scripts/03_create_rds.sh
```
*Mục tiêu kiểm tra:* DB identifier `autoschedule-db`, MySQL 8.x, Single-AZ, `PubliclyAccessible=No`, dung lượng lưu trữ 20 GiB gp3, gắn đủ 4 tag. Quá trình tạo RDS mất khoảng 5–10 phút để đạt trạng thái `available`.

### Bước 4.4: Tạo SageMaker Notebook Instance mẫu
```bash
./scripts/04_create_sagemaker.sh
```
*Mục tiêu kiểm tra:* Notebook identifier `autoschedule-nb`, loại `ml.t3.medium`, ổ đĩa 5 GB, gán IAM Role `LabRole`, gắn đủ 4 tag. Quá trình tạo mất khoảng 3–5 phút để đạt trạng thái `InService`.

---

## 5. Kiểm Tra Trạng Thái Toàn Diện (Status Verification)

Sau khi khởi tạo xong, chạy script kiểm tra trạng thái tập trung:

```bash
./scripts/05_status.sh
```

Đảm bảo kết quả trả về hiển thị đầy đủ:
1. **EC2:** Trạng thái `running` (hoặc `stopped`), kèm giá trị tag `Schedule` và `ScheduleDays`.
2. **RDS:** Trạng thái `available`, không công khai Internet (`PubliclyAccessible=False`).
3. **SageMaker:** Trạng thái `InService`.

---

## 6. Hướng Dẫn Thu Thập Ảnh Minh Chứng (Evidence Collection)

Khi chụp ảnh màn hình trên AWS Console, phải tuân thủ nghiêm ngặt các quy tắc:
1. Luôn để lộ góc trên cùng bên phải màn hình (chứa Account ID và Region `us-east-1`).
2. Luôn để lộ thanh đồng hồ hệ thống (ngày giờ thực hiện bài lab).
3. Đặt tên file ảnh đúng định dạng quy định và lưu vào thư mục `docs/screenshots/`:
   - `week1-evidence-04.png`: S3 Block Public Access đang Bật.
   - `week1-evidence-05.png`: S3 Tags và Mã hóa mặc định SSE-S3.
   - `week1-evidence-06.png`: EC2 trạng thái Running 2/2 checks passed.
   - `week1-evidence-07.png`: Tab Tags của EC2 Instance.
   - `week1-evidence-08.png`: Tab Tags của EBS Volume.
   - `week1-evidence-09.png`: RDS MySQL trạng thái Available.
   - `week1-evidence-10.png`: Chi tiết cấu hình RDS (Single-AZ, Non-public).
   - `week1-evidence-11.png`: Tab Tags của RDS DB Instance.
   - `week1-evidence-12.png`: SageMaker Notebook trạng thái InService.
   - `week1-evidence-13.png`: Tab Tags của SageMaker Notebook.
   - `week1-evidence-14.png`: Kiểm tra tài nguyên và phân vùng EBS còn lại.
   - `week1-evidence-15-sagemaker-execution-role.png`: Minh chứng Notebook sử dụng role `LabRole`.
   - `week1-evidence-16-account-region.png`: Minh chứng hiển thị Account ID và Region `us-east-1`.

---

## 7. Quy Trình Dọn Dẹp và Bảo Vệ Ngân Sách (End of Session)

Để không làm cạn kiệt ngân sách $100 của AWS Learner Lab:

### Khi kết thúc buổi làm việc (Tạm dừng tài nguyên):
```bash
# Tạm dừng EC2
aws ec2 stop-instances --instance-ids $(aws ec2 describe-instances --filters "Name=tag:Project,Values=AutoSchedule" --query "Reservations[].Instances[].InstanceId" --output text)

# Tạm dừng RDS MySQL
aws rds stop-db-instance --db-instance-identifier autoschedule-db

# Tạm dừng SageMaker Notebook
aws sagemaker stop-notebook-instance --notebook-instance-name autoschedule-nb
```

### Khi dọn dẹp hoàn toàn tài nguyên mẫu:
```bash
./scripts/99_cleanup.sh --bucket
```
Sau khi xóa, kiểm tra lại trên Console:
- EC2 Instances: Đã chuyển sang trạng thái `terminated`.
- EBS Volumes: Không còn volume unattached/dư thừa.
- RDS Instances: Đã xóa hoàn toàn.
- SageMaker Notebook: Đã xóa hoàn toàn.

---

## 8. Xử Lý Sự Cố Thường Gặp (Troubleshooting)

| Lỗi gặp phải | Nguyên nhân | Cách khắc phục |
|---|---|---|
| `AccessDeniedException` khi gọi API | Phiên làm việc AWS Learner Lab bị hết hạn | Mở lại trang AWS Learner Lab, copy AWS Session Token mới vào `~/.aws/credentials`. |
| `Cannot create IAM Role` | Learner Lab giới hạn quyền quản trị IAM | Không tạo role mới; luôn sử dụng biến `$LAB_ROLE_ARN` trỏ tới `LabRole`. |
| `RDS tự động bật lại` | AWS tự động restart RDS sau tối đa 7 ngày | Đây là cơ chế mặc định của AWS RDS; kiểm tra lại giữa tuần hoặc dùng Lambda tự động stop. |
| `Tag Editor Explicit Deny` | Learner Lab áp dụng Service Control Policy chặn Resource Explorer | Kiểm tra tag trực tiếp tại trang quản trị từng dịch vụ (EC2, RDS, SageMaker). |
