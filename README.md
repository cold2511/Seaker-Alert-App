# Seaker Alert App

A system monitoring and alerting application that tracks CPU, RAM, Disk usage and uptime, displays them on a web-based dashboard, and sends alerts when predefined thresholds are breached.

---

## Objective

This project is built as part of the **Seaker Monitoring & Alert Application Assignment**.  
It monitors system usage metrics with minimal overhead, stores historical data, visualizes it in real time, and triggers alerts when limits are crossed.

---

## Metrics Monitored

- CPU Usage (%)
- RAM Usage (Used & Total in GB)
- Disk Usage (Used & Total in GB)
- System Uptime (hours)

---

## Architecture

System Metrics (OS)
↓
Python Agent (psutil)
↓ /metrics
Prometheus (scraping + storage + alert rules)
↓
Grafana (web dashboard)
↓
Alertmanager → Telegram / Email



---

## Technology Stack

- Python (psutil, prometheus-client)
- Prometheus
- Grafana
- Alertmanager
- Docker & Docker Compose
- Telegram API (for alerts)

All tools used are open-source and permitted by the assignment.

---

## How to Run (Docker)

### Prerequisites
- Docker
- Docker Compose

### Steps
```bash
git clone <YOUR_GITHUB_REPO_LINK>
cd Seaker-Alert-App
docker-compose up --build



| Service       | URL                                                            |
| ------------- | -------------------------------------------------------------- |
| Agent Metrics | [http://localhost:8000/metrics]                                |
| Prometheus    | [http://localhost:9090]                                        |
| Grafana       | [http://localhost:3000]                                        |
| Alertmanager  | [http://localhost:9093]                                        |



Username: admin
Password: admin





Thank you
email:hrishinarain@gmail.com
