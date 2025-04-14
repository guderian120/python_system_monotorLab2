
# 🖥️ System Metrics Alert Script

This Python script monitors **CPU usage**, **RAM usage**, and **disk space**, and sends an **email alert** when any defined threshold is exceeded. It uses the [`psutil`](https://github.com/giampaolo/psutil) library for metric gathering and [Resend](https://resend.com) for sending email notifications.

---

## 🚀 Features

- ✅ Monitor CPU, RAM, and Disk usage
- 📩 Send alert emails using the Resend API
- ⚙️ Thresholds and email settings configurable via `.env`
- ⏱️ Ready to integrate with `cron`, `systemd`, or Docker

---

## 📁 Project Structure

```
.
├── monitor.py           # Main script
├── .env                 # Environment variables
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone  https://github.com/guderian120/python_system_monotorLab2
   cd system-metrics-alert
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---


## Demo
A live Demo video
![Demo Video](/media/sys_monitor.gif)

## 🛠️ Configuration

Create a `.env` file in the project root with the following content:

```env
RESEND_API_KEY=your_resend_api_key
ALERT_RECIPIENT=your_email@example.com
ALERT_FROM=System Monitor <onboarding@resend.dev>

CPU_THRESHOLD=75
RAM_THRESHOLD=80
DISK_THRESHOLD=15
```

> Threshold values are in percentages.

---

## ▶️ Usage

Run the script directly:

```bash
python monitor.py
```

You can also set it up as a cron job to run at intervals:

```bash
# Every 5 minutes
*/5 * * * * /path/to/venv/bin/python /path/to/system-metrics-alert/monitor.py
```

---



## ✅ Dependencies

- Python 3.7+
- [psutil](https://pypi.org/project/psutil/)
- [resend](https://resend.com)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

Install all with:
```bash
pip install -r requirements.txt
```

---

## 📬 Alert Preview

The email you receive will look like this:

> **Subject**: 🚨 System Alert: Threshold Exceeded  
> **Body**:  
> ⚠️ CPU usage is high: 2% (Threshold: 2%)  
> ⚠️ Disk space is low: 50% free (Threshold: 50% free)  

---





---

## 👨‍💻 Author

**Andy Amponsah** 
