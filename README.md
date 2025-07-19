# 🌩️ CloudMonitorApp

A simple Flask-based dashboard to monitor your AWS services like **EC2**, **ECS**, **Lambda**, and **S3**.

---

## 🔍 What It Does

- Shows running EC2 instances
- Displays ECS clusters and tasks
- Lists Lambda functions
- Shows available S3 buckets

---

## 🛠️ Tech Stack

- **Flask** (Python)
- **Boto3** (AWS SDK)
- **Docker**
- **GitHub Actions** for CI/CD
- **AWS ECS Fargate** for deployment

---

## 🚀 How to Run Locally

```bash
docker build -t cloud-monitor-app .
docker run -p 5000:5000 cloud-monitor-app
