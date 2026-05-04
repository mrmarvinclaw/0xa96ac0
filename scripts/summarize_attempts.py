#!/usr/bin/env python3
import json
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
records = json.loads((repo / "docs" / "attempts.json").read_text())
completed = [r for r in records if r.get("status") == "ok"]
print(f"attempts={len(records)}")
print(f"completed={len(completed)}")
print(f"failed={len(records) - len(completed)}")
print(f"completed_demonstrated={sum(r.get('resolution') == 'demonstrated' for r in completed)}")
print(f"completed_not_demonstrated={sum(r.get('resolution') == 'not_demonstrated' for r in completed)}")
print(f"votes_demonstrated={sum(r.get('votes_for', 0) for r in completed)}")
print(f"votes_not_demonstrated={sum(r.get('votes_against', 0) for r in completed)}")
