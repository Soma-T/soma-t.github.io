#!/usr/bin/env python3
"""Validate the synthetic Elastic bulk fixture without connecting to a SIEM."""

import json
from datetime import datetime
from ipaddress import ip_address, ip_network
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "security-alert.bulk.ndjson"
EXPECTED = ROOT / "expected-results.json"
TEST_NET = ip_network("203.0.113.0/24")


def load_bulk(path):
    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(lines) % 2:
        raise ValueError("Bulk file must contain an action line and a document line for each event.")
    events = []
    for index in range(0, len(lines), 2):
        action = json.loads(lines[index])
        document = json.loads(lines[index + 1])
        if "index" not in action:
            raise ValueError(f"Line {index + 1} must contain an index action.")
        if action["index"].get("_index") != "synthetic-alert-lab":
            raise ValueError("Every event must target the dedicated synthetic index.")
        events.append(document)
    return events


def main():
    events = load_bulk(DATA)
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    ids = [event["event"]["id"] for event in events]
    if len(ids) != len(set(ids)):
        raise ValueError("Event IDs must be unique.")
    if ids != [f"evt-{number:03d}" for number in range(1, 9)]:
        raise ValueError("Expected exactly eight ordered fixture events.")

    timestamps = [datetime.fromisoformat(event["@timestamp"].replace("Z", "+00:00")) for event in events]
    if timestamps != sorted(timestamps):
        raise ValueError("Events must be ordered by timestamp.")

    for event in events:
        if event.get("labels", {}).get("synthetic") is not True:
            raise ValueError(f"{event['event']['id']} is missing labels.synthetic=true.")
        if not event.get("host", {}).get("name", "").endswith(("-lab-01", "-lab-02")):
            raise ValueError(f"{event['event']['id']} has a host name outside the lab fixture.")

    external_ips = []
    for event in events:
        destination = event.get("destination", {}).get("ip")
        if destination:
            external_ips.append(ip_address(destination))
    if not external_ips or any(ip not in TEST_NET for ip in external_ips):
        raise ValueError("External destination values must stay in documentation-only TEST-NET-3.")

    injection = next(event for event in events if event["event"]["id"] == "evt-007")
    if "ignore previous instructions" not in injection["message"].lower():
        raise ValueError("Prompt-injection test text is missing from evt-007.")
    if expected["expected_event_ids"] != ids[:5]:
        raise ValueError("Expected primary-case event IDs do not match the fixture.")
    if expected["control_event_ids"] != ["evt-008"]:
        raise ValueError("Expected control event ID does not match the fixture.")

    print(f"PASS: {len(events)} ordered synthetic records; unique IDs; isolated index; TEST-NET-3 only.")
    print("PASS: primary case, incomplete-evidence case, prompt-injection case, and benign control are present.")
    print("PASS: no SIEM connection or response action was performed.")


if __name__ == "__main__":
    main()
