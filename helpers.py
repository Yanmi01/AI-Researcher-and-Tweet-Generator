import os
from datetime import datetime
from typing import Dict, Any, List


def sanity_checks(report: str, tweets: str) -> List[str]:
    errors: List[str] = []
    if len(report.split()) < 50:
        errors.append("Report seems too short (<50 words).")
    for idx, t in enumerate(tweets.splitlines(), 1):
        if len(t) > 280:
            errors.append(f"Tweet #{idx} too long ({len(t)} chars).")
    return errors


def append_to_review_log(query: str, entry: Dict[str, Any]) -> None:
    log_dir = os.getenv("REVIEW_LOG_DIR", ".")
    os.makedirs(log_dir, exist_ok=True)
    path = os.path.join(log_dir, "review_log.csv")
    header = not os.path.exists(path)
    with open(path, "a", encoding="utf-8") as f:
        if header:
            f.write("query,timestamp,decision,comments\n")
        line = f"{query},{entry['timestamp']},{entry['decision']},{entry['comments'].replace(',', ';')}\n"
        f.write(line)