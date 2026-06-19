from event_parser import load_events
from mitre_mapper import MITRE_MAPPING
from report_generator import save_report


def main():
    events = load_events("sample_logs.csv")
    results = []

    for _, row in events.iterrows():
        event_id = int(row["EventID"])

        if event_id in MITRE_MAPPING:
            finding = {
                "time": row["TimeCreated"],
                "event_id": event_id,
                "user": row["User"],
                "technique": MITRE_MAPPING[event_id]["technique"],
                "tactic": MITRE_MAPPING[event_id]["tactic"],
                "description": MITRE_MAPPING[event_id]["description"],
            }
            results.append(finding)

    save_report(results, "reports/security_report.json")

    print("\nSecurity Report Generated\n")
    for item in results:
        print(item)


if __name__ == "__main__":
    main()