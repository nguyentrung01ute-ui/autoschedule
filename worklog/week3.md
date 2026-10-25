# Worklog tuần 3 — AutoSchedule

## 1. Thông tin chung

- **Nhóm:** DevOps & IaC
- **Dự án:** AutoSchedule — tự động bật/tắt tài nguyên AWS theo lịch học
- **Môi trường:** AWS Learner Lab, Region `us-east-1` (dùng IAM role có sẵn `LabRole`)
- **Thời gian thực hiện:** Tuần 3 (20/10/2026 – 26/10/2026)
- **Thành viên:** 
  - Nguyễn Văn Trung (MSSV: 24110365) — Nhóm trưởng
  - Nguyễn Văn Thi (MSSV: 24110334) — Thành viên
- **Tổng thời lượng đã ghi nhận:** 17 giờ 05 phút
  - **Nguyễn Văn Trung:** 8 giờ 28 phút
  - **Nguyễn Văn Thi:** 8 giờ 37 phút
- **Trạng thái minh chứng:** Đã cập nhật đủ 34 ảnh minh chứng Tuần 3 trong `docs/screenshots/`; danh mục và mô tả từng ảnh được liên kết chi tiết tại [docs/week3-evidence.md](../docs/week3-evidence.md).
- **Báo cáo chính thức:** [reports/Bao_cao_tuan3_Nhom_DevOps_IaC.docx](../reports/Bao_cao_tuan3_Nhom_DevOps_IaC.docx)

---

## 2. Liên kết Mã Nguồn, Mẫu Triển Khai IaC và Script Tuần 3 (Tiêu chí 3)

| Hạng mục mã nguồn / cấu hình | File trong repo | Link trực tiếp trên GitHub | Mô tả tóm tắt |
|---|---|---|---|
| **CloudFormation Template** | `infra/template.yaml` | [infra/template.yaml](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/infra/template.yaml) | Bản thiết kế IaC chuẩn hóa toàn bộ hạ tầng: SNS Topic, Email Subscription, LogGroup (retention 7 ngày), Lambda Function (Python 3.12, 128MB, 120s, LabRole), 2 EventBridge Rules (`rate(15 minutes)` và `cron(0 1 * * ? *)`), 2 Lambda Permissions, và CloudWatch Error Alarm. Không tạo IAM mới. |
| **Script triển khai tự động** | `scripts/07_deploy.sh` | [scripts/07_deploy.sh](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/scripts/07_deploy.sh) | Tự động đóng gói mã nguồn `src/scheduler.py` thành zip, upload lên S3 bucket với tiền tố định danh theo thời gian (`artifacts/scheduler-YYYYMMDD-HHMMSS.zip`) và thực thi lệnh `aws cloudformation deploy` với đầy đủ tham số và tag. |
| **Danh mục minh chứng Tuần 3** | `docs/week3-evidence.md` | [docs/week3-evidence.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/docs/week3-evidence.md) | Bảng tra cứu toàn bộ 34 ảnh minh chứng kết quả triển khai, kiểm thử tự kích hoạt, rà soát bảo mật và giám sát CloudWatch. |
| **Khai báo sử dụng AI Tuần 3** | `docs/ai-disclosure-week3.md` | [docs/ai-disclosure-week3.md](https://github.com/nguyentrung01ute-ui/autoschedule/blob/main/docs/ai-disclosure-week3.md) | Bản giải trình chi tiết về việc ứng dụng Claude Sonnet 5.5, phạm vi trợ giúp kỹ thuật và công việc sinh viên tự kiểm chứng trên AWS. |

---

## 3. Phân công, Kết quả và Commit Minh Chứng Phát Triển (Tiêu chí 6)

| Thành viên | Nhiệm vụ cụ thể | Thời lượng | Link file mã nguồn / tài liệu liên quan | Link Commit minh chứng công việc phát triển |
|---|---|---:|---|---|
| **Nguyễn Văn Trung (24110365)** | - **Tạo lịch tự kích hoạt EventBridge**: Do giao diện AWS Console thay đổi, cấu hình thủ công qua EventBridge Scheduler với 2 lịch: `autoschedule-enforce-manual` (rate 15 phút) và `autoschedule-report-manual` (cron 08:00 VN) gắn role `LabRole`.<br>- **Kiểm thử tự kích hoạt (INT-10a, INT-10b, INT-11)**: Kiểm chứng EC2 tự động bật khi trong khung giờ (`START EC2`) và tự động tắt khi đổi sang ngoài giờ (`STOP EC2`) mà không cần thao tác tay; kiểm chứng email báo cáo tài nguyên nhận tự động.<br>- **Rà soát bảo mật hạ tầng**: Thực hiện đối chiếu 10 tiêu chuẩn an toàn trên AWS Learner Lab: quét mã nguồn không có secret/password/access key, kiểm tra RDS private & mã hóa, kiểm tra Security Group không mở `0.0.0.0/0`, S3 Block All Public Access & SSE-S3 encryption, giới hạn tài nguyên Lambda và retention của Log group.<br>- **Xây dựng Dashboard & kiểm thử Alarm (INT-14)**: Thiết lập CloudWatch Dashboard giám sát Invocations, Errors, Duration. Gây lỗi có chủ đích bằng cách sửa biến môi trường `TOPIC_ARN` sai để kích hoạt Alarm chuyển `In alarm`, xác nhận email cảnh báo gửi về và theo dõi Alarm tự phục hồi về `OK` sau 15 phút sửa lại đúng. | **8 giờ 28 phút** | • [infra/template.yaml](../infra/template.yaml)<br>• [worklog/week3.md](week3.md)<br>• [docs/week3-evidence.md](../docs/week3-evidence.md) | • [Commit add1c60](https://github.com/nguyentrung01ute-ui/autoschedule/commit/add1c60fc977a4a98dd9cbaee5f333fb1f692257): Cập nhật bộ ảnh minh chứng Tuần 3 đợt 1 (01-11, 21-35).<br>• [Commit 8a0adff](https://github.com/nguyentrung01ute-ui/autoschedule/commit/8a0adffbbc45e5c13281edb54f8ab820ec096090): Thêm báo cáo Word chính thức Tuần 3. |
| **Nguyễn Văn Thi (24110334)** | - **Dọn dẹp tài nguyên thủ công**: Xóa sạch các tài nguyên tạo thủ công ở tuần trước (2 lịch Scheduler, Lambda `autoschedule`, SNS topic `autoschedule-report`, log group) để tránh lỗi trùng tên tài nguyên khi triển khai CloudFormation.<br>- **Viết và hoàn thiện script triển khai IaC**: Chuẩn hóa `scripts/07_deploy.sh` tự động nén mã nguồn Lambda, upload S3 artifact và thực thi `aws cloudformation deploy` với các tham số role, email, bucket, tag.<br>- **Triển khai CloudFormation stack lần 1 (INT-12)**: Deploy stack `autoschedule` thành công trên AWS CloudShell, đạt trạng thái `CREATE_COMPLETE` và xác nhận email subscription SNS.<br>- **Kiểm thử tính tái lập của IaC (INT-13)**: Xóa stack bằng lệnh `aws cloudformation delete-stack`, chờ `DELETE_COMPLETE`, sau đó chạy lại script deploy để chứng minh hệ thống có thể dựng lại nguyên vẹn và độc lập.<br>- **Quản lý Git & tổng hợp minh chứng**: Đặt tên, phân loại và upload bộ 34 ảnh minh chứng thực tế; rà soát và biên tập báo cáo Tuần 3. | **8 giờ 37 phút** | • [scripts/07_deploy.sh](../scripts/07_deploy.sh)<br>• [reports/Bao_cao_tuan3_Nhom_DevOps_IaC.docx](../reports/Bao_cao_tuan3_Nhom_DevOps_IaC.docx)<br>• [docs/screenshots/](../docs/screenshots/) | • [Commit 9a5f5ef](https://github.com/nguyentrung01ute-ui/autoschedule/commit/9a5f5ef4545d5ca3587053eef631525c34538d58): Bổ sung ảnh minh chứng xóa tài nguyên thủ công và deploy CloudFormation (12-18).<br>• [Commit 8a0adff](https://github.com/nguyentrung01ute-ui/autoschedule/commit/8a0adffbbc45e5c13281edb54f8ab820ec096090): Báo cáo Word Tuần 3. |
| **Cả hai thành viên** | Cùng thảo luận phương án giải quyết giới hạn giao diện EventBridge mới, thống nhất cấu hình template CloudFormation, đối chiếu các yêu cầu bảo mật trên AWS Learner Lab, theo dõi log CloudWatch và hoàn thiện hồ sơ báo cáo. | Đã tính trong tổng giờ | [Kế hoạch](../PROJECT_PLAN.md) · [Roadmap](../docs/ROADMAP.md) · [Báo cáo Tuần 3](week3.md) | Phối hợp đồng bộ kết quả trên nhánh chính `main`. |

---

## 4. Nhật ký công việc và liên kết kiểm chứng thực tế

Mục này chi tiết hóa từng công việc cụ thể của hai thành viên nhằm đối chiếu minh bạch giữa **nhiệm vụ – sản phẩm – minh chứng thực tế**.

| Hạng mục công việc | Người phụ trách | File kiểm tra / mã kiểm thử / sản phẩm | Trạng thái & liên kết kiểm chứng |
|---|---|---|---|
| Cấu hình 2 lịch tự kích hoạt thủ công trên EventBridge Scheduler (`rate(15 minutes)` và `cron(0 8 * * ? *)`) | Nguyễn Văn Trung | EventBridge Console | [Ảnh danh sách lịch](../docs/screenshots/week3-evidence-01.png) · [Ảnh lịch enforce](../docs/screenshots/week3-evidence-02.png) · [Ảnh lịch report](../docs/screenshots/week3-evidence-03.png) |
| Kiểm thử tự kích hoạt START EC2 trong khung giờ (INT-10a) | Nguyễn Văn Trung | EC2 Console / CloudWatch Logs | [Tag EC2 trước khi chạy](../docs/screenshots/week3-evidence-04.png) · [EC2 tự chuyển Running](../docs/screenshots/week3-evidence-05.png) · [Log START EC2](../docs/screenshots/week3-evidence-06.png) |
| Kiểm thử tự kích hoạt STOP EC2 ngoài khung giờ (INT-10b) | Nguyễn Văn Trung | EC2 Console / CloudWatch Logs | [Đổi tag ngoài giờ](../docs/screenshots/week3-evidence-07.png) · [EC2 tự chuyển Stopped & Log STOP](../docs/screenshots/week3-evidence-08.png) · [Biểu đồ Lambda Invocations](../docs/screenshots/week3-evidence-09.png) |
| Kiểm thử nhận email báo cáo tài nguyên hàng ngày qua SNS theo lịch tự động (INT-11) | Nguyễn Văn Trung | Email / CloudWatch Logs | [Email nhận từ SNS](../docs/screenshots/week3-evidence-10.png) · [Log stream report](../docs/screenshots/week3-evidence-11.png) |
| Xóa các tài nguyên đã tạo thủ công (Lambda, SNS topic, Log group, Scheduler) để chuẩn bị deploy IaC | Nguyễn Văn Thi | AWS Console / CloudShell | [Lambda sau khi xóa](../docs/screenshots/week3-evidence-12a.png) · [SNS sau khi xóa](../docs/screenshots/week3-evidence-12b.png) |
| Xây dựng và hoàn thiện script đóng gói và triển khai tự động `07_deploy.sh` | Nguyễn Văn Thi | [scripts/07_deploy.sh](../scripts/07_deploy.sh) | Script nén zip Lambda, upload S3 key theo thời gian và chạy `aws cloudformation deploy` |
| Triển khai stack CloudFormation `autoschedule` lần 1 đạt `CREATE_COMPLETE` (INT-12) | Nguyễn Văn Thi | CloudFormation Console | [Stack CREATE_COMPLETE](../docs/screenshots/week3-evidence-13.png) · [Resources](../docs/screenshots/week3-evidence-14.png) · [Events](../docs/screenshots/week3-evidence-15.png) · [Outputs](../docs/screenshots/week3-evidence-16.png) · [EventBridge Rules](../docs/screenshots/week3-evidence-17.png) · [Email confirmed](../docs/screenshots/week3-evidence-18.png) |
| Kiểm thử tính tái lập: xóa stack (`delete-stack`) và deploy lại lần 2 đạt `CREATE_COMPLETE` (INT-13) | Nguyễn Văn Thi | CloudFormation Console / CloudShell | Thực hiện `aws cloudformation delete-stack` và deploy lại thành công bằng `./scripts/07_deploy.sh` |
| Rà soát bảo mật mã nguồn (quét credential/mật khẩu trong code) | Nguyễn Văn Trung | Terminal / Git repo | [Kết quả grep không có password/secret](../docs/screenshots/week3-evidence-28.png) |
| Rà soát bảo mật dịch vụ lưu trữ và cơ sở dữ liệu (RDS, S3) | Nguyễn Văn Trung | RDS Console / S3 Console | [RDS không public](../docs/screenshots/week3-evidence-21.png) · [Mật khẩu RDS ẩn & mã hóa](../docs/screenshots/week3-evidence-22.png) · [S3 Block Public Access](../docs/screenshots/week3-evidence-24.png) · [S3 SSE-S3 Encryption](../docs/screenshots/week3-evidence-25.png) |
| Rà soát bảo mật mạng, tài nguyên Lambda và cấu hình lưu vết log | Nguyễn Văn Trung | VPC Console / Lambda / CloudWatch | [Security Group không mở 0.0.0.0/0](../docs/screenshots/week3-evidence-23.png) · [Lambda 128MB & 120s](../docs/screenshots/week3-evidence-26.png) · [Log group retention 7 ngày](../docs/screenshots/week3-evidence-27.png) |
| Thiết lập CloudWatch Dashboard `autoschedule-dashboard` giám sát Lambda | Nguyễn Văn Trung | CloudWatch Dashboard Console | [Dashboard với Invocations, Errors, Duration](../docs/screenshots/week3-evidence-29.png) |
| Kiểm thử CloudWatch Alarm `autoschedule-errors`: gây lỗi, kích hoạt cảnh báo SNS và tự hồi phục (INT-14) | Nguyễn Văn Trung | CloudWatch Alarms / Lambda / SNS | [Alarm ban đầu OK](../docs/screenshots/week3-evidence-30.png) · [Đặt TOPIC_ARN sai](../docs/screenshots/week3-evidence-31.png) · [Test event lỗi InvalidClientTokenId](../docs/screenshots/week3-evidence-32.png) · [Alarm In alarm](../docs/screenshots/week3-evidence-33.png) · [Email cảnh báo](../docs/screenshots/week3-evidence-34.png) · [Alarm tự về OK](../docs/screenshots/week3-evidence-35.png) |
| Soạn thảo, chuẩn hóa định dạng báo cáo Word Tuần 3 và đồng bộ dữ liệu | Nguyễn Văn Thi | [reports/Bao_cao_tuan3_Nhom_DevOps_IaC.docx](../reports/Bao_cao_tuan3_Nhom_DevOps_IaC.docx) | [Danh mục minh chứng Tuần 3](../docs/week3-evidence.md) · [Khai báo AI](../docs/ai-disclosure-week3.md) |
| Phối hợp rà soát toàn bộ kết quả kiểm thử và đồng bộ git | Cả hai | Git repo / GitHub | Kiểm tra 34 ảnh minh chứng, xác nhận bảng kết quả kiểm thử và đẩy toàn bộ sản phẩm lên GitHub |

---

## 5. Khai báo sử dụng AI (Tiêu chí 7)

Trong Tuần 3, nhóm sử dụng **Claude (Anthropic)** (phiên bản Claude Sonnet 5.5) với mục đích hỗ trợ tra cứu kỹ thuật và chuẩn hóa phương án kiểm thử:

| Tên công cụ AI & Mô hình | Mục đích sử dụng | Công việc sinh viên tự thực hiện (kiểm chứng & sửa đổi) | Link commit minh chứng |
|---|---|---|---|
| **Claude (Sonnet 5.5)** | Hướng dẫn tạo lịch EventBridge Scheduler thay thế cho giao diện Rule truyền thống và cấu hình role execution `LabRole`. | Sinh viên tự thao tác cấu hình trực tiếp trên AWS Learner Lab Console, thiết lập tham số múi giờ `Asia/Saigon` và payload JSON chính xác. | [Commit add1c60](https://github.com/nguyentrung01ute-ui/autoschedule/commit/add1c60fc977a4a98dd9cbaee5f333fb1f692257) |
| **Claude (Sonnet 5.5)** | Gợi ý cú pháp lệnh deploy CloudFormation linh hoạt với S3 key động và cấu trúc tham số override trong bash script. | Sinh viên Nguyễn Văn Thi tự viết file `scripts/07_deploy.sh`, kiểm tra xử lý lỗi `set -euo pipefail` và chạy trực tiếp trên AWS CloudShell. | [Commit 9a5f5ef](https://github.com/nguyentrung01ute-ui/autoschedule/commit/9a5f5ef4545d5ca3587053eef631525c34538d58) |
| **Claude (Sonnet 5.5)** | Tham khảo danh mục các tiêu chí rà soát bảo mật chuẩn theo mô hình Well-Architected Framework cho bài thực hành sinh viên. | Sinh viên Nguyễn Văn Trung tự chạy lệnh grep quét code, kiểm tra từng cấu hình dịch vụ AWS thực tế và chụp minh chứng đối chiếu đạt 10/10 tiêu chí. | [Commit add1c60](https://github.com/nguyentrung01ute-ui/autoschedule/commit/add1c60fc977a4a98dd9cbaee5f333fb1f692257) |
| **Claude (Sonnet 5.5)** | Tư vấn kịch bản thử nghiệm CloudWatch Alarm bằng cách gây lỗi an toàn không làm hỏng dữ liệu hệ thống. | Sinh viên tự thay đổi cấu hình `TOPIC_ARN`, kích hoạt test event, quan sát chu kỳ 15 phút của metric CloudWatch và khôi phục hệ thống về trạng thái ổn định. | [Commit add1c60](https://github.com/nguyentrung01ute-ui/autoschedule/commit/add1c60fc977a4a98dd9cbaee5f333fb1f692257) |

---

## 6. Tổng hợp thời lượng Tuần 3

| Thành viên | MSSV | Vai trò | Tổng thời gian |
|---|---|---|---:|
| **Nguyễn Văn Trung** | 24110365 | Nhóm trưởng (DevOps & IaC) | **8 giờ 28 phút** |
| **Nguyễn Văn Thi** | 24110334 | Thành viên (DevOps & IaC) | **8 giờ 37 phút** |
| **Tổng cộng cả nhóm** | | | **17 giờ 05 phút** |

*Cả hai thành viên đều đáp ứng và vượt mức thời lượng tối thiểu 8 giờ/tuần theo quy định của môn học.*

---

## 7. Tài liệu và Sản phẩm Tuần 3 liên quan

- [Kế hoạch dự án tổng thể](../PROJECT_PLAN.md)
- [Bản đồ tiến độ chi tiết (Roadmap)](../docs/ROADMAP.md)
- [Mẫu thiết kế hạ tầng CloudFormation](../infra/template.yaml)
- [Script triển khai tự động](../scripts/07_deploy.sh)
- [Danh mục minh chứng và kết quả kiểm thử Tuần 3](../docs/week3-evidence.md)
- [Bản khai báo sử dụng AI Tuần 3](../docs/ai-disclosure-week3.md)
- [Báo cáo Word Tuần 3 (.docx)](../reports/Bao_cao_tuan3_Nhom_DevOps_IaC.docx)
- [Thư mục ảnh minh chứng thực tế](../docs/screenshots/)
- [Worklog Tuần 2](week2.md)
