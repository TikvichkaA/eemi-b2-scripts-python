from config import CPU_THRESHOLD, RAM_THRESHOLD, DISK_THRESHOLD


def check(metrics):
    alerts = []
    if metrics["cpu"] > CPU_THRESHOLD:
        alerts.append(f"CPU élevé : {metrics['cpu']:.1f}% (seuil {CPU_THRESHOLD}%)")
    if metrics["ram"] > RAM_THRESHOLD:
        alerts.append(f"RAM élevée : {metrics['ram']:.1f}% (seuil {RAM_THRESHOLD}%)")
    if metrics["disk"] > DISK_THRESHOLD:
        alerts.append(f"Disque plein : {metrics['disk']:.1f}% (seuil {DISK_THRESHOLD}%)")
    return alerts
