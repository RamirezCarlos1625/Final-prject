import json
from pathlib import Path


def save_report(data, filename):
    output_path = Path(filename)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as report:
        json.dump(data, report, indent=4)
        report.write("\n")