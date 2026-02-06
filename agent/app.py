import time
import psutil
from prometheus_client import Gauge, start_http_server

cpu_usage = Gauge("cpu_usage_percent", "CPU usage percent")
ram_used = Gauge("ram_used_gb", "RAM used in GB")
ram_total = Gauge("ram_total_gb", "Total RAM in GB")
disk_used = Gauge("disk_used_gb", "Disk used in GB")
disk_total = Gauge("disk_total_gb", "Total disk in GB")
uptime_hours = Gauge("uptime_hours", "System uptime in hours")

boot_time = psutil.boot_time()

def collect_metrics():
    while True:
        cpu_usage.set(psutil.cpu_percent(interval=1))

        mem = psutil.virtual_memory()
        ram_used.set(mem.used / (1024 ** 3))
        ram_total.set(mem.total / (1024 ** 3))

        disk = psutil.disk_usage("/")
        disk_used.set(disk.used / (1024 ** 3))
        disk_total.set(disk.total / (1024 ** 3))

        uptime_hours.set((time.time() - boot_time) / 3600)

        time.sleep(5)

if __name__ == "__main__":
    start_http_server(8000)
    collect_metrics()
