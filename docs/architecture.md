# Kiến trúc AutoSchedule

> Sơ đồ dùng Mermaid, GitHub tự hiển thị. Khi cần nộp báo cáo, chụp ảnh sơ đồ này hoặc vẽ lại bằng draw.io.

```mermaid
flowchart LR
    subgraph EB[EventBridge]
        R1["Rule 1: rate(15 phút)<br/>kiểm tra lịch"]
        R2["Rule 2: cron(0 1 * * ? *)<br/>08:00 giờ VN, báo cáo"]
    end

    L["Lambda: autoschedule<br/>Python 3.12 - LabRole"]

    subgraph RES["Tài nguyên có tag Schedule"]
        EC2["EC2 t3.nano"]
        RDS["RDS db.t3.micro"]
        SM["SageMaker Notebook<br/>ml.t3.medium"]
    end

    SNS["SNS topic<br/>autoschedule-report"]
    MAIL["Email"]
    CW["CloudWatch Logs + Alarm Errors"]
    S3["S3: scheduler.zip"]
    CFN["CloudFormation stack"]

    R1 --> L
    R2 -->|"action=report"| L
    L -->|"start / stop"| EC2
    L -->|"start / stop"| RDS
    L -->|"start / stop"| SM
    L -->|"báo cáo hằng ngày"| SNS --> MAIL
    L -->|"log"| CW
    CW -->|"cảnh báo lỗi"| SNS
    S3 -.->|"mã nguồn"| L
    CFN -.->|"dựng toàn bộ"| L
```

## Luồng xử lý của Lambda

```mermaid
flowchart TD
    A[Lambda được gọi] --> B{event.action = report?}
    B -- Có --> C[Thu thập tài nguyên đang chạy]
    C --> D[Gửi email qua SNS]
    B -- Không --> E[Thu thập EC2, RDS, SageMaker có tag Schedule]
    E --> F{Có tag Schedule hợp lệ?}
    F -- Không --> G[Bỏ qua]
    F -- Có --> H{Trạng thái thực tế = mong muốn?}
    H -- Có --> G
    H -- Không --> I[Gọi start hoặc stop]
    I --> J[Ghi log Actions]
```

## Quy ước tag

| Tag | Ví dụ | Ý nghĩa |
|---|---|---|
| `Schedule` | `08:00-17:00`, `22:00-06:00`, `off` | Khung giờ chạy |
| `ScheduleDays` | `Mon-Fri` | Ngày chạy (mặc định cả tuần) |
| `Project` | `AutoSchedule` | Bắt buộc theo đề |
| `Owner` | `sv01` | Bắt buộc theo đề |
