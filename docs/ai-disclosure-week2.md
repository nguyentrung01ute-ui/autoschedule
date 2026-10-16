# Khai báo sử dụng AI — Tuần 2

## 1. Công cụ được sử dụng
- **Công cụ:** Claude (Anthropic).
- **Phạm vi sử dụng trong Tuần 2:**
  - Hỗ trợ tham khảo cú pháp và hoàn thiện 11 unit test case cho hàm `desired_running()` trong `tests/test_schedule.py` (bao quát các trường hợp kiểm thử biên, ngày cuối tuần, lịch qua đêm).
  - Tham khảo kịch bản kiểm thử tích hợp bật/tắt (START/STOP) cho RDS MySQL và SageMaker Notebook khi gọi Lambda thủ công bằng event enforce.
  - Hỗ trợ dàn ý cấu trúc bảng tổng hợp kết quả kiểm thử (INT-01 đến INT-09) và ghi chú kỹ thuật về thời gian chuyển trạng thái tài nguyên.

## 2. Cách nhóm sử dụng và kiểm tra
Nhóm sinh viên chịu trách nhiệm hoàn toàn về toàn bộ mã nguồn và kết quả thực tế trên hệ thống AWS:
- Mã kiểm thử pytest do sinh viên Nguyễn Văn Thi tự đọc hiểu, tự chạy trên môi trường thực tế đạt 11/11 tests passed.
- Các thao tác cấu hình tài nguyên (gắn tag `Schedule`, `ScheduleDays`, tạo SNS topic, đăng ký email subscription) đều do sinh viên tự thực hiện trên AWS Learner Lab Console.
- Kết quả kiểm thử START/STOP, bỏ qua khi đang chuyển trạng thái được sinh viên tự kích hoạt và kiểm chứng bằng ảnh chụp màn hình thực tế có hiển thị thời gian, log CloudWatch và email SNS nhận về.
- Mọi nội dung do AI gợi ý đều được đối chiếu trực tiếp với tài liệu AWS boto3 và giới hạn của AWS Learner Lab (`LabRole`, Region `us-east-1`).

## 3. Minh chứng Git
- **Commit pytest 11 passed:** [Commit c90a945](https://github.com/nguyentrung01ute-ui/autoschedule/commit/c90a9459bcdbbfb20c0471f9081164f22fec1a43)
- **Commit minh chứng kiểm thử RDS, SageMaker, SNS:** [Commit 9f54fe9](https://github.com/nguyentrung01ute-ui/autoschedule/commit/9f54fe9d21a7c0304917d16fc189fd7e26522d5e)
