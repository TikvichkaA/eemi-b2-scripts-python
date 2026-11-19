import time
import argparse

from config import CHECK_INTERVAL, LOG_FILE
from metrics import get_metrics
from checker import check
from reporter import report


def main():
    parser = argparse.ArgumentParser(description="Agent de supervision système")
    parser.add_argument("--log", default=LOG_FILE, help="Chemin du fichier de log")
    parser.add_argument("--interval", type=int, default=CHECK_INTERVAL,
                        help="Intervalle entre deux vérifications (secondes)")
    args = parser.parse_args()

    print(f"Watchdog démarré — vérification toutes les {args.interval} s")
    while True:
        metrics = get_metrics()
        alerts = check(metrics)
        if alerts:
            report(alerts, args.log)
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
