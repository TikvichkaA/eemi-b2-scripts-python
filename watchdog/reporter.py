import datetime
from config import LOG_FILE


def report(alerts, log_file=LOG_FILE):
    with open(log_file, "w") as f:
        for alert in alerts:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line = f"[{timestamp}] ALERTE : {alert}\n"
            print(line, end="")
            f.write(line)
