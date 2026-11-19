import psutil
from config import DISK_PATH


def get_metrics():
    return {
        "cpu": psutil.cpu_percent(interval=0.1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage(DISK_PATH).percent,
    }
