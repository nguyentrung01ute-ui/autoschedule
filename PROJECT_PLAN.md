# AutoSchedule: Tự động bật/tắt tài nguyên AWS theo giờ học để tiết kiệm ngân sách

**Nhóm:** DevOps & IaC
**Môi trường:** AWS Learner Lab (Region `us-east-1`, dùng `LabRole`)
**Thời gian:** 4 tuần, nhóm tối đa 2 sinh viên, mỗi SV tối thiểu 8 giờ/tuần

---

## 1. Tổng quan

### 1.1 Bài toán
Trong Learner Lab, ngân sách có hạn nhưng tài nguyên (EC2, RDS, SageMaker Notebook) thường bị để chạy cả ngày đêm, kể cả ngoài giờ học. Việc nhớ tắt thủ công dễ sót, gây lãng phí.

### 1.2 Giải pháp
Một hệ thống serverless tự động:
1. **Quét** các tài nguyên có tag `Schedule`.
2. **So sánh** với giờ hiện tại (múi giờ `Asia/Ho_Chi_Minh`) và **bật/tắt** cho đúng lịch.
3. **Gửi báo cáo hằng ngày** qua email (SNS) liệt kê các tài nguyên đang chạy.
4. Toàn bộ được **đóng gói bằng CloudFormation** để dựng lại bằng một lệnh.

### 1.3 Mục tiêu
- Lambda (boto3) xử lý ít nhất **3 loại tài nguyên**: EC2, RDS, SageMaker Notebook.
- EventBridge kích hoạt theo lịch định kỳ.
- Báo cáo SNS hằng ngày.
- Template CloudFormation triển khai toàn bộ giải pháp.
- Có giám sát (CloudWatch Logs, Alarm) và báo cáo chi phí tiết kiệm được.

### 1.4 Ngoài phạm vi
- Auto Scaling Group, ngày nghỉ lễ, SageMaker Studio/Endpoint (có thể làm phần mở rộng).
- Tạo IAM user/role mới (Learner Lab không cho phép).

---

## 2. Kiến trúc

```
EventBridge rule (rate 15 phút) ──► Lambda (LabRole) ──► EC2 / RDS / SageMaker Notebook
EventBridge rule (cron 01:00 UTC = 08:00 VN) ─┘   │
                                                   ├──► SNS topic ──► Email (báo cáo hằng ngày)
                                                   └──► CloudWatch Logs ──► Alarm (Errors) ──► SNS
CloudFormation: đóng gói Lambda, 2 Rule, SNS, Log Group, Alarm, Permission
S3: lưu file scheduler.zip
```

### 2.1 Thành phần

| Thành phần | Vai trò |
|---|---|
| **EventBridge Rule #1** `rate(15 minutes)` | Gọi Lambda kiểm tra lịch và bật/tắt tài nguyên |
| **EventBridge Rule #2** `cron(0 1 * * ? *)` | Gọi Lambda với input `{"action":"report"}` để gửi báo cáo |
| **Lambda `autoschedule`** (Python 3.12, LabRole) | Logic chính: thu thập, so lịch, bật/tắt, báo cáo |
| **SNS topic** `autoschedule-report` | Gửi email báo cáo và cảnh báo lỗi |
| **CloudWatch Logs / Alarm** | Lưu log (7 ngày), cảnh báo khi Lambda lỗi |
| **S3 bucket** `autoschedule-<ACCOUNT_ID>` | Chứa mã Lambda đóng gói |
| **CloudFormation** | Triển khai lặp lại toàn bộ hệ thống |

### 2.2 Quy ước tag

| Tag | Ví dụ | Ý nghĩa |
|---|---|---|
| `Schedule` | `08:00-17:00`, `22:00-06:00`, `off` | Khung giờ được chạy; `off` là luôn tắt. **Không có tag này thì bị bỏ qua** |
| `ScheduleDays` | `Mon-Fri`, `Mon` (mặc định `Mon-Sun`) | Các ngày được chạy |
| `Project` | `AutoSchedule` | Bắt buộc theo đề |
| `Owner` | `sv01` | Bắt buộc theo đề |

### 2.3 Logic quyết định

```
Không có tag Schedule        → bỏ qua
Schedule = off               → phải tắt
Ngày hợp lệ VÀ trong khung giờ → phải chạy
Ngược lại                    → phải tắt

Nếu trạng thái thực tế ≠ trạng thái mong muốn → gọi start/stop
Tài nguyên đang starting/stopping/pending → bỏ qua, chu kỳ sau xử lý
```

Khung giờ: `start <= giờ_hiện_tại < end` (đầu vào bao gồm, đầu ra không bao gồm). Nếu `start > end` thì hiểu là khung qua đêm.

### 2.4 API boto3 sử dụng

| Dịch vụ | Liệt kê | Đọc tag | Bật | Tắt |
|---|---|---|---|---|
| EC2 | `describe_instances` (paginator, lọc tag-key `Schedule`) | có sẵn trong kết quả | `start_instances` | `stop_instances` |
| RDS | `describe_db_instances` | `list_tags_for_resource` | `start_db_instance` | `stop_db_instance` |
| SageMaker | `list_notebook_instances` | `list_tags` | `start_notebook_instance` | `stop_notebook_instance` |

---

## 3. Ràng buộc của Learner Lab cần tuân thủ

- Chỉ dùng Region `us-east-1` hoặc `us-west-2`.
- Dùng `LabRole`/`LabInstanceProfile`, **không tạo IAM user/role**.
- EC2 loại nano → large, ≤ 9 instance và ≤ 32 vCPU chạy đồng thời mỗi Region.
- EBS ≤ 100 GB (gp2/gp3).
- Gắn tag `Project`/`Owner` cho mọi tài nguyên.
- Dừng/xóa tài nguyên sau mỗi buổi làm việc.
- Không tạo NAT Gateway (tốn phí).

---

## 4. Cấu trúc repo Git

```
autoschedule/
├── src/
│   └── scheduler.py          # Mã Lambda
├── infra/
│   └── template.yaml         # Template CloudFormation
├── tests/
│   └── test_schedule.py      # Unit test cho logic lịch
├── docs/
│   ├── architecture.drawio   # Sơ đồ kiến trúc
│   ├── screenshots/          # Minh chứng theo tuần
│   └── report.md             # Báo cáo cuối kỳ
├── worklog/
│   ├── week1.md ... week4.md
└── PROJECT_PLAN.md
```

---

## 5. Kế hoạch 4 tuần

### Phân công đề xuất

| | SV A | SV B |
|---|---|---|
| Chính | EC2, mã Lambda core, CloudFormation | RDS, SageMaker, SNS, CloudWatch, báo cáo |
| Chéo | Review mã và test phần của B | Review mã và template của A |

Cả hai phải giải thích được **mọi** phần khi vấn đáp.

### Quy tắc mỗi buổi làm việc
1. Bắt đầu: *Start Lab*, mở CloudShell ở `us-east-1`.
2. Chụp minh chứng có **Account ID, Region, thời gian** (chạy `aws sts get-caller-identity`).
3. Kết thúc: dừng/xóa tài nguyên không cần, ghi worklog.

---

### Tuần 1: Thiết kế và dựng nền tảng

**Mục tiêu:** có sơ đồ, bucket S3, 3 tài nguyên mẫu đã gắn tag, repo Git.

| # | Công việc | Giờ | Phụ trách |
|---|---|---|---|
| 1 | Tìm hiểu EventBridge (cron/rate), boto3 EC2/RDS/SageMaker, giới hạn Learner Lab | 2 | A + B |
| 2 | Tạo repo Git, cấu trúc thư mục | 1 | A |
| 3 | Vẽ sơ đồ kiến trúc (draw.io), chốt quy ước tag, múi giờ, tên tài nguyên | 2 | B |
| 4 | Tạo S3 bucket có tag, bật Block Public Access | 1 | A |
| 5 | Tạo EC2 `t3.nano` có tag | 1.5 | A |
| 6 | Tạo RDS MySQL `db.t3.micro` 20 GB (không public, không Multi-AZ) | 2 | B |
| 7 | Tạo SageMaker Notebook `ml.t3.medium` (role LabRole) | 1.5 | B |
| 8 | Ghi worklog, chụp minh chứng | 1 | A + B |

**Lệnh tham khảo:**
```bash
aws sts get-caller-identity
aws iam get-role --role-name LabRole --query Role.Arn --output text
ACC=$(aws sts get-caller-identity --query Account --output text)
aws s3 mb s3://autoschedule-$ACC --region us-east-1
```

**Minh chứng:** sơ đồ kiến trúc; ảnh console EC2/RDS/SageMaker có cột tag; ảnh bucket; link repo; worklog.
**Hoàn thành khi:** 3 tài nguyên chạy được, đủ tag, sơ đồ được cả nhóm đồng ý.

---

### Tuần 2: Chức năng lõi và kiểm thử từng thành phần

**Mục tiêu:** Lambda bật/tắt đúng cho từng loại tài nguyên khi chạy thủ công.

| # | Công việc | Giờ | Phụ trách |
|---|---|---|---|
| 1 | Viết `tests/test_schedule.py`, chạy `pytest` (không cần AWS) | 2 | A |
| 2 | Viết `scheduler.py` hoàn chỉnh | 2 | A |
| 3 | Tạo SNS topic, đăng ký và xác nhận email | 1 | B |
| 4 | Tạo Lambda thủ công trên console (LabRole, timeout 120s, biến môi trường `TOPIC_ARN`, `TZ_NAME`) | 1.5 | B |
| 5 | Test từng loại tài nguyên bằng cách đổi tag `Schedule` sát giờ hiện tại | 3 | A (EC2), B (RDS, SageMaker) |
| 6 | Test báo cáo SNS với event `{"action":"report"}` | 0.5 | B |
| 7 | Worklog, minh chứng | 1 | A + B |

**Bảng kiểm thử bắt buộc:**

| Test | Thao tác | Kết quả mong đợi |
|---|---|---|
| EC2 tắt | `Schedule` là khung giờ đã qua, EC2 đang chạy | Log `STOP EC2 i-...` |
| EC2 bật | `Schedule` bao quanh giờ hiện tại, EC2 đang tắt | Log `START EC2 ...` |
| RDS bật/tắt | Tương tự (mất vài phút đổi trạng thái) | `START/STOP RDS ...` |
| SageMaker bật/tắt | Tương tự | `START/STOP SageMaker ...` |
| Không có tag | Xóa tag `Schedule` | Không có hành động |
| Tag `off` | `Schedule=off` | Luôn bị tắt |
| Tag sai định dạng | `Schedule=abc` | Bỏ qua, có log cảnh báo |
| Báo cáo | Event `{"action":"report"}` | Nhận email SNS |

**Minh chứng:** kết quả pytest; ảnh Test event thành công; ảnh CloudWatch Logs có dòng `Actions: [...]`; ảnh email báo cáo; ảnh trạng thái trước/sau.
**Hoàn thành khi:** bảng kiểm thử đều đạt và có kết quả ghi lại.

---

### Tuần 3: Tích hợp, bảo mật, giám sát, IaC

**Mục tiêu:** chạy tự động bằng EventBridge, triển khai được bằng một lệnh CloudFormation.

| # | Công việc | Giờ | Phụ trách |
|---|---|---|---|
| 1 | Tạo 2 EventBridge rule thủ công, quan sát kích hoạt | 2 | B |
| 2 | Xóa tài nguyên thủ công (function, rule, topic) để tránh trùng tên | 0.5 | A |
| 3 | Hoàn thiện `template.yaml` (Lambda, 2 rule, permission, SNS, Log Group, Alarm) | 3 | A |
| 4 | Deploy bằng `aws cloudformation deploy`; sửa lỗi theo tab Events | 1.5 | A |
| 5 | Thử xóa stack rồi tạo lại để kiểm chứng tính lặp lại | 0.5 | A + B |
| 6 | Rà soát bảo mật (xem 6) | 1.5 | B |
| 7 | CloudWatch Dashboard (Invocations, Errors, Duration); thử gây lỗi để Alarm kích hoạt | 1.5 | B |
| 8 | Worklog, minh chứng | 1 | A + B |

**Lệnh triển khai:**
```bash
cd src && zip ../scheduler.zip scheduler.py && cd ..
aws s3 cp scheduler.zip s3://autoschedule-$ACC/ --region us-east-1
aws cloudformation deploy --stack-name autoschedule \
  --template-file infra/template.yaml \
  --parameter-overrides LabRoleArn=arn:aws:iam::$ACC:role/LabRole \
    CodeBucket=autoschedule-$ACC AlertEmail=<email> OwnerTag=sv01 \
  --region us-east-1
```

**Lưu ý:** sau deploy phải bấm **Confirm subscription** trong email. Khi sửa mã Lambda mà `CodeKey` không đổi, dùng `aws lambda update-function-code` hoặc đổi tên key.

**Minh chứng:** ảnh 2 rule EventBridge; stack `CREATE_COMPLETE` và tab Resources; ảnh Alarm/Dashboard; template trên Git.
**Hoàn thành khi:** không can thiệp tay mà tài nguyên vẫn tự bật/tắt đúng giờ và có email báo cáo.

---

### Tuần 4: Kiểm thử tổng thể, tối ưu chi phí, dọn dẹp, báo cáo, demo

| # | Công việc | Giờ | Phụ trách |
|---|---|---|---|
| 1 | Dựng lại toàn bộ từ đầu bằng một lệnh deploy | 1 | A |
| 2 | Test end-to-end: đặt lịch ngắn (bật 10 phút), quan sát chu kỳ bật rồi tắt qua EventBridge, ghi bảng thời điểm | 2 | A + B |
| 3 | Test lỗi: tag sai, tài nguyên đang `starting`, Lambda lỗi → Alarm gửi email | 1 | B |
| 4 | Tính chi phí và mức tiết kiệm (xem 7) | 2 | B |
| 5 | Dọn dẹp tài nguyên (sau khi chụp đủ minh chứng) | 1 | A |
| 6 | Viết báo cáo | 3 | A + B |
| 7 | Quay video demo ≤ 10 phút | 1.5 | A + B |
| 8 | Ôn vấn đáp, worklog | 1 | A + B |

**Dọn dẹp:**
```bash
aws cloudformation delete-stack --stack-name autoschedule
aws ec2 terminate-instances --instance-ids <id>
aws rds delete-db-instance --db-instance-identifier autoschedule-db --skip-final-snapshot
aws sagemaker stop-notebook-instance --notebook-instance-name autoschedule-nb
# đợi Stopped rồi mới xóa:
aws sagemaker delete-notebook-instance --notebook-instance-name autoschedule-nb
aws s3 rb s3://autoschedule-$ACC --force
```
Sau đó kiểm tra EBS volume, snapshot, Elastic IP còn sót.

**Kịch bản video demo (≤ 10 phút):**

| Thời gian | Nội dung |
|---|---|
| 0:00–1:30 | Bài toán, sơ đồ kiến trúc |
| 1:30–3:00 | Mã Lambda và template |
| 3:00–4:30 | Deploy stack bằng CloudFormation |
| 4:30–8:00 | Đổi tag, quan sát bật/tắt EC2/RDS/SageMaker và log |
| 8:00–9:30 | Email báo cáo SNS, Alarm, bảng chi phí |
| 9:30–10:00 | Kết luận |

---

## 6. Bảo mật

Learner Lab không cho tạo IAM nên bảo mật thể hiện qua:
- Lambda chỉ tác động tài nguyên có tag `Schedule`.
- Không ghi mật khẩu/khóa trong mã hay template (RDS dùng `--manage-master-user-password`).
- RDS không public; Security Group không mở cổng DB cho `0.0.0.0/0`.
- S3 bật Block Public Access và mã hóa mặc định.
- Giới hạn Timeout/Memory Lambda; log giữ 7 ngày.
- Mỗi tài nguyên đều có tag `Project`/`Owner` để truy vết.

## 7. Chi phí và mức tiết kiệm

- Ví dụ lịch `08:00-17:00`, `Mon-Fri`: 9 giờ × 5 ngày = **45 giờ/tuần** so với **168 giờ/tuần** chạy 24/7 → giảm khoảng **73%** giờ chạy.
- Lập bảng cho từng loại tài nguyên: đơn giá/giờ × giờ chạy (có lịch) so với 24/7.
- Chi phí chạy chính hệ thống (Lambda 15 phút/lần ≈ 2.880 lần/tháng, SNS, CloudWatch) rất nhỏ, nằm trong mức miễn phí hoặc không đáng kể.
- Nếu Cost Explorer bị hạn chế quyền, dùng AWS Pricing Calculator và ghi rõ là **ước tính**.
- Đánh đổi: chu kỳ 15 phút → độ trễ tối đa 15 phút; chu kỳ 30 phút giảm số lần gọi nhưng tăng độ trễ.

## 8. Rủi ro và hạn chế đã biết

| Vấn đề | Tác động | Cách xử lý |
|---|---|---|
| RDS tự bật lại sau 7 ngày khi bị stop | Tốn phí ngoài lịch | Lambda chu kỳ 15 phút sẽ tắt lại; ghi vào báo cáo |
| Lab session hết hạn sẽ tắt/làm ngừng EventBridge, Lambda | Hệ thống không chạy | Kiểm tra lại sau mỗi lần mở lab |
| LabRole có thể bị từ chối một số API | Lỗi `AccessDenied` | Bọc `try/except`, ghi log, ghi vào báo cáo |
| Khung giờ qua đêm gắn với ngày hiện tại | Ví dụ `22:00-06:00` + `Mon-Fri`: sáng thứ Bảy 03:00 bị coi ngoài lịch | Ghi vào mục Hạn chế; có thể mở rộng |
| Tài nguyên đang `starting/stopping` bị bỏ qua | Trễ một chu kỳ | Hành vi chủ đích, chu kỳ sau xử lý |
| Loại instance bị từ chối ở một Region | Không tạo được | Đổi loại nhỏ hơn hoặc Region còn lại, ghi lại lỗi |
| Quên dọn dẹp | Hết ngân sách | Checklist dọn dẹp cuối buổi |

## 9. Hướng mở rộng
- Tag `ScheduleSkipDates` cho ngày nghỉ lễ.
- Hỗ trợ Auto Scaling Group (đổi min/desired).
- Dashboard CloudWatch tổng hợp, metric tùy chỉnh số tài nguyên bị tắt.
- Báo cáo kèm ước tính tiền tiết kiệm.

---

## 10. Sản phẩm bàn giao

| Sản phẩm | Yêu cầu |
|---|---|
| Mã nguồn + template trên Git | `src/`, `infra/`, `tests/` |
| Sơ đồ kiến trúc | Tệp draw.io và ảnh xuất ra |
| Báo cáo | Có phần chi phí và phần AI hỗ trợ |
| Video demo | ≤ 10 phút |
| Worklog 4 tuần | Phân công và số giờ từng SV |
| Minh chứng | Ảnh console/CLI có Account ID, Region, thời gian |

### Cấu trúc báo cáo
1. Giới thiệu bài toán và mục tiêu
2. Kiến trúc và sơ đồ
3. Triển khai từng thành phần (kèm ảnh)
4. Kết quả kiểm thử
5. Bảo mật và giám sát
6. Chi phí và mức tiết kiệm
7. Hạn chế và hướng mở rộng
8. Phần AI hỗ trợ
9. Phụ lục: worklog, link Git

### Mẫu worklog

| Ngày | SV | Công việc | Số giờ | Có dùng AI? | Minh chứng |
|---|---|---|---|---|---|
| dd/mm | A | ... | 2.5 | Có (hỏi lệnh CLI) | anh-01.png |
| dd/mm | B | ... | 3 | Không | anh-02.png |

---

## 11. Khai báo sử dụng AI

Ghi rõ trong báo cáo, ví dụ:

| Phần | AI hỗ trợ | SV đã làm gì |
|---|---|---|
| Mã `scheduler.py` | Sinh bản nháp | Đọc, test, sửa, tự giải thích được từng hàm |
| Template CloudFormation | Sinh bản nháp | Deploy thật, sửa lỗi theo Events |
| Lệnh CLI | Tham khảo | Chạy thật trên Learner Lab |

Mọi tài nguyên phải được triển khai và chạy thật trên AWS Learner Lab.

## 12. Chuẩn bị vấn đáp

Mỗi SV tự giải thích được:
- Hàm `desired_running()`: các nhánh, giờ biên, khung qua đêm.
- Vì sao dùng paginator cho EC2.
- Vì sao lambda dùng tham số mặc định `i=i` (tránh closure bắt biến vòng lặp).
- Vì sao cron EventBridge dùng UTC còn logic lịch dùng `Asia/Ho_Chi_Minh`.
- Vì sao Lambda dùng LabRole, cần những quyền nào.
- Luồng CloudFormation: tham số, `DependsOn`, `Lambda::Permission`, Alarm.
- Cách tính tiết kiệm chi phí và các hạn chế của giải pháp.

## 13. Tiêu chí hoàn thành (Definition of Done)

- [ ] Lambda xử lý đúng ≥ 3 loại tài nguyên (EC2, RDS, SageMaker).
- [ ] EventBridge tự kích hoạt; email báo cáo đến hằng ngày.
- [ ] Stack CloudFormation dựng lại được từ đầu bằng một lệnh.
- [ ] Alarm lỗi Lambda hoạt động.
- [ ] Mọi tài nguyên có tag `Project`/`Owner`.
- [ ] Có bảng kiểm thử và kết quả.
- [ ] Có báo cáo chi phí và mức tiết kiệm.
- [ ] Đã dọn dẹp tài nguyên.
- [ ] Đủ báo cáo, sơ đồ, Git, video, worklog 4 tuần.
