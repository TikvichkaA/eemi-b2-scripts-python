"""Bilan de tous les exercices : python3 bilan.py"""
import subprocess
import sys
from pathlib import Path

ici = Path(__file__).resolve().parent
reussis = 0
fichiers = sorted(ici.glob("ex0*.py"))
for f in fichiers:
    r = subprocess.run([sys.executable, f.name], cwd=ici, capture_output=True, text=True, timeout=20)
    ok = r.returncode == 0
    reussis += ok
    print(f"  {'✓' if ok else '✗'} {f.name}")
print(f"\n{reussis}/{len(fichiers)} exercices réussis")
