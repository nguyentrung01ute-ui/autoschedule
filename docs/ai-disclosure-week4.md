# Khai báo sử dụng AI — Tuần 4

## 1. Công cụ được sử dụng
- **Công cụ:** Claude (Anthropic).
- **Phạm vi sử dụng trong Tuần 4:**
  - Tham khảo cách thiết kế bài kiểm thử tổng thể (end-to-end lịch ngắn, tag sai, tài nguyên đang chuyển trạng thái, gây lỗi Alarm).
  - Tham khảo cách tính chi phí và quy đổi giờ chạy theo tháng (730 giờ 24/7 so với 195 giờ theo lịch).
  - Gợi ý dàn ý kịch bản video demo và danh mục dọn dẹp tài nguyên.
  - Hỗ trợ trình bày tài liệu Markdown (bảng minh chứng, test plan, cost analysis, báo cáo cuối kỳ).

## 2. Cách nhóm sử dụng và kiểm tra
- Kết quả kiểm thử INT-17, INT-18, INT-19 dựa trên log/ảnh thực tế trên AWS Learner Lab (Hình 10–14); sinh viên tự đối chiếu `Actions: []`, log `Invalid schedule tag`, trạng thái Alarm và email cảnh báo.
- Chi phí 24/7 do sinh viên tự nhập cấu hình EC2 t3.nano, RDS db.t3.micro 20 GB, SageMaker ml.t3.medium vào AWS Pricing Calculator (Hình 16); sinh viên tự tính tỷ lệ 195/730 và kiểm tra lại từng số.
- Ngân sách Learner Lab ($3,5 / $50) được sinh viên tự chụp (Hình 15).
- Sinh viên tự chạy deploy, test end-to-end, dọn dẹp tài nguyên và giải thích được hoạt động của hệ thống; AI không truy cập tài khoản AWS.

## 3. Minh chứng Git
- **Commit báo cáo Tuần 4 (Nguyễn Văn Trung):** [Commit b3196b4](https://github.com/nguyentrung01ute-ui/autoschedule/commit/b3196b48759b6176f752eedc6d5c98c408847888)
- **Commit ảnh minh chứng Hình 10–16 và tài liệu Tuần 4 (Nguyễn Văn Thi):** [Commit 1c77812](https://github.com/nguyentrung01ute-ui/autoschedule/commit/1c77812d0444021e395db45397f9f7523325312f)
