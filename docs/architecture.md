# Kiến trúc Hệ thống AutoSchedule

Dự án **AutoSchedule** xây dựng giải pháp Serverless tự động bật/tắt tài nguyên AWS theo thời khóa biểu học tập nhằm tối ưu chi phí trong môi trường **AWS Learner Lab**.

---

## 1. Sơ đồ Kiến trúc Tổng thể

```text
               +-------------------------------------------------------------+
               |                     AWS Learner Lab                         |
               |                                                             |
               |   [EventBridge Rule #1]                                     |
               |   rate(15 minutes)                                          |
               |          |                                                  |
               |          v                                                  |
               |   +-------------------+    (boto3)     +------------------+ |
               |   |  AWS Lambda       |--------------->| EC2 Instances    | |
               |   |  autoschedule     |                | (t3.nano)        | |
               |   |  (Python 3.12,    |--------------->+------------------+ |
               |   |   LabRole)        |                | RDS MySQL        | |
               |   +-------------------+                | (db.t3.micro)    | |
               |     |        |        |--------------->+------------------+ |
               |     |        |                         | SageMaker NB     | |
               |     |        |                         | (ml.t3.medium)   | |
               |     |        |                         +------------------+ |
               |     |        +--------> [CloudWatch Logs]                   |
               |     |                         |                             |
               |     |                         v (Metric Alarm: Errors >= 1) |
               |     |                   [SNS Topic]                         |
               |     v                         |                             |
               |   [EventBridge Rule #2]       |                             |
               |   cron(0 1 * * ? *)           v                             |
               |   (08:00 VN - Báo cáo) -> [Email Thông báo / Báo cáo]       |
               +-------------------------------------------------------------+
```

---

## 2. Thiết kế Hai Luồng Xử Lý Chính

### 2.1 Luồng Tự Động Thực Thi Lịch (Enforce Flow)
- **Chu kỳ kích hoạt:** Mỗi 15 phút thông qua EventBridge Rule `rate(15 minutes)`.
- **Cơ chế hoạt động:**
  1. EventBridge gửi sự kiện kích hoạt Lambda Function `autoschedule`.
  2. Lambda sử dụng `boto3` quét toàn bộ tài nguyên EC2, RDS và SageMaker Notebook có gắn tag `Project=AutoSchedule` và `Schedule`.
  3. Hàm `desired_running()` so sánh thời gian thực tế theo múi giờ Việt Nam (`Asia/Ho_Chi_Minh` = UTC+7) với khung giờ quy định trong tag `Schedule` và ngày trong tuần trong tag `ScheduleDays`.
  4. Nếu trạng thái mong muốn khác trạng thái hiện tại:
     - Nếu cần tắt mà tài nguyên đang chạy (`running` / `available` / `InService`) -> Gọi API Stop (`stop_instances`, `stop_db_instance`, `stop_notebook_instance`).
     - Nếu cần bật mà tài nguyên đang dừng (`stopped`) -> Gọi API Start (`start_instances`, `start_db_instance`, `start_notebook_instance`).
  5. Các tài nguyên đang trong trạng thái chuyển tiếp (`pending`, `stopping`, `starting`, `modifying`, `Deleting`) sẽ tự động được bỏ qua và xử lý ở chu kỳ tiếp theo để tránh xung đột trạng thái.

### 2.2 Luồng Báo Cáo Hằng Ngày (Report Flow)
- **Thời gian kích hoạt:** 01:00 UTC hằng ngày (tương ứng 08:00 sáng giờ Việt Nam) qua EventBridge Rule `cron(0 1 * * ? *)`.
- **Cơ chế hoạt động:**
  1. EventBridge kích hoạt Lambda với payload `{"action": "report"}`.
  2. Lambda thu thập danh sách tất cả các tài nguyên đang ở trạng thái chạy (`running`, `available`, `InService`).
  3. Tổng hợp nội dung báo cáo chi tiết kèm mức ước tính thời gian hoạt động.
  4. Publish thông điệp đến **Amazon SNS Topic** (`autoschedule-report`).
  5. SNS tự động gửi email thông báo trạng thái tài nguyên tới danh sách email quản trị viên đã đăng ký.

---

## 3. Quy Ước Tag Chuẩn (Tagging Strategy)

| Tên Tag | Giá trị ví dụ | Tính bắt buộc | Ý nghĩa và tác dụng |
|---|---|---|---|
| `Project` | `AutoSchedule` | Bắt buộc | Nhận diện tài nguyên thuộc phạm vi quản lý của dự án, tránh ảnh hưởng tài nguyên khác trong lab. |
| `Owner` | `24110365`, `24110334` | Bắt buộc | Định danh sinh viên phụ trách quản lý tài nguyên để phân bổ chi phí. |
| `Schedule` | `08:00-17:00`, `22:00-06:00`, `off` | Bắt buộc | Khung giờ cho phép tài nguyên chạy. `off` nghĩa là luôn dừng tài nguyên. |
| `ScheduleDays` | `Mon-Fri`, `Mon,Wed,Fri` | Tùy chọn (Mặc định `Mon-Sun`) | Các ngày trong tuần được phép chạy. |

- **Xử lý khung giờ qua đêm (Overnight Schedule):** Nếu `start_time > end_time` (ví dụ: `22:00-06:00`), hệ thống xác định khung giờ chạy bắt đầu từ ngày hiện tại và kết thúc vào rạng sáng ngày tiếp theo.

---

## 4. Danh Mục Dịch Vụ và Bảng API boto3

| Dịch vụ AWS | Mục đích trong dự án | API boto3 Liệt kê & Đọc Tag | API Bật tài nguyên | API Tắt tài nguyên |
|---|---|---|---|---|
| **EC2** | Máy chủ ứng dụng mẫu (`t3.nano`) | `describe_instances` (dùng Paginator) | `start_instances` | `stop_instances` |
| **RDS MySQL** | Cơ sở dữ liệu mẫu (`db.t3.micro`, gp3 20GB) | `describe_db_instances`, `list_tags_for_resource` | `start_db_instance` | `stop_db_instance` |
| **SageMaker** | Notebook phân tích dữ liệu (`ml.t3.medium`) | `list_notebook_instances`, `list_tags` | `start_notebook_instance` | `stop_notebook_instance` |
| **EventBridge** | Bộ lập lịch tự động gọi Lambda | Scheduled Rules (`rate`, `cron`) | — | — |
| **SNS** | Kênh gửi email báo cáo & cảnh báo lỗi | `sns.publish` | — | — |
| **CloudWatch** | Lưu trữ Log và giám sát cảnh báo lỗi | Metric Alarm (`Errors >= 1`) | — | — |
| **S3** | Lưu trữ mã nguồn đóng gói `scheduler.zip` | `s3.put_object`, `s3.get_object` | — | — |
| **CloudFormation** | Đóng gói toàn bộ hạ tầng dưới dạng mã (IaC) | `infra/template.yaml` | — | — |

---

## 5. Ràng Buộc Kỹ Thuật và Bảo Mật AWS Learner Lab

1. **Phân quyền IAM:**
   - Tuân thủ quy định môi trường Learner Lab: Tuyệt đối không tạo IAM User hoặc IAM Role mới.
   - Toàn bộ Lambda Function và SageMaker Notebook sử dụng Role có sẵn là `LabRole` (`arn:aws:iam::<ACCOUNT_ID>:role/LabRole`).
   - EC2 sử dụng Instance Profile `LabInstanceProfile`.
2. **Bảo mật cơ sở dữ liệu:**
   - RDS MySQL cấu hình `PubliclyAccessible = False`, chỉ cho phép truy cập nội bộ trong VPC.
   - Quản lý mật khẩu thông qua AWS Secrets Manager hoặc tham số truyền vào lúc thực thi, không hardcode mật khẩu trong git commit.
3. **Bảo mật S3:**
   - Bật tính năng `Block Public Access` toàn diện và kích hoạt mã hóa mặc định SSE-S3.
4. **Giới hạn thời gian của RDS:**
   - Lưu ý hành vi của AWS: RDS sau khi stop sẽ tự động được AWS bật lại sau tối đa 7 ngày. Do đó, luồng Enforce quét định kỳ 15 phút sẽ tự động stop lại nếu nằm ngoài lịch học.
