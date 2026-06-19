"""Example script for generating a security report from sample logs."""

from event_parser import load_events
from mitre_mapper import MITRE_MAPPING
from report_generator import save_report


def main():
    events = load_events("sample_logs.csv")
    results = []

    for _, row in events.iterrows():
        event_id = int(row["EventID"])
        if event_id not in MITRE_MAPPING:
            continue

        results.append(
            {
                "time": row["TimeCreated"],
                "event_id": event_id,
                "user": row["User"],
                "technique": MITRE_MAPPING[event_id]["technique"],
                "tactic": MITRE_MAPPING[event_id]["tactic"],
                "description": MITRE_MAPPING[event_id]["description"],
            }
        )

    save_report(results, "reports/security_report.json")
    print("Security report generated successfully.")


if __name__ == "__main__":
    main()