import os
import psutil
import resend
from dotenv import load_dotenv

# Load .env only once
load_dotenv("/home/guderian/AMALITECH_GTP/LEARNING_RESOURCE/lab2_a/.env")

class SysAlert:
    def __init__(self): 
        # Thresholds from environment with defaults
        self.cpu_threshold = float(os.getenv("CPU_THRESHOLD", 2))
        self.ram_threshold = float(os.getenv("RAM_THRESHOLD", 10))
        self.disk_threshold = float(os.getenv("DISK_THRESHOLD", 50))  # disk free space %

        self.recipient_email = os.getenv("ALERT_RECIPIENT", "example@example.com")
        self.from_email = os.getenv("ALERT_FROM", "System Monitor <onboarding@resend.dev>")
        resend.api_key = os.getenv("RESEND_API_KEY")
    # method to send alert if threshold exceeded
    def send_alert(self, message):
        """Send alert email using Resend API"""
        print("Sending alert...\n", message)
        params: resend.Emails.SendParams = {
            "from": self.from_email,
            "to": [self.recipient_email],
            "subject": "🚨 System Alert: Threshold Exceeded",
            "html": message.replace("\n", "<br>"),
        }

        try:
            response = resend.Emails.send(params)
            print("Alert sent:", response)
        except Exception as e:
            print("Failed to send alert:", str(e))

    def check_metrics(self): #  check system metrics 
        """Check system metrics and send alert if thresholds are exceeded"""
        cpu = psutil.cpu_percent(interval=1) # get cpu usage in percentage
        ram = psutil.virtual_memory().percent # get ram usage in percentage
        disk = 100 - psutil.disk_usage('/').percent  # Free disk space

        alerts = []

        # if usage is greater that set threashold
        if cpu > self.cpu_threshold: 
            alerts.append(f"⚠️ CPU usage is high: {cpu}% (Threshold: {self.cpu_threshold}%)")
        if ram > self.ram_threshold:
            alerts.append(f"⚠️ RAM usage is high: {ram}% (Threshold: {self.ram_threshold}%)")
        if disk < self.disk_threshold:
            alerts.append(f"⚠️ Disk space is low: {disk}% free (Threshold: {self.disk_threshold}% free)")

        if alerts:
            self.send_alert("\n".join(alerts)) # if there are alerts then send them
        else:
            print("✅ All system metrics are within normal range.")

if __name__ == '__main__':
    monitor = SysAlert()
    monitor.check_metrics()
