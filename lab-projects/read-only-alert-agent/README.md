# Read-Only Security Alert Agent, Milestone 1

## Goal

Build a small assistant that helps an analyst understand one security alert. It will read events from a dedicated Elastic lab index and draft an evidence-linked summary. A human will make every decision.

## Plain-English version

We are preparing a safe practice case. The records describe one made-up Windows computer where PowerShell starts a service-creation command, Windows records the service, and PowerShell later makes a connection to a reserved example IP address. The sequence gives us something to investigate. It does not prove a real attack.

This milestone creates the practice records and writes down what a correct investigation should notice. We have not yet loaded them into Elastic or built the AI assistant.

## Files

- `data/security-alert.bulk.ndjson` contains eight synthetic events in Elasticsearch Bulk API format.
- `expected-results.json` records the observations, uncertainties, control result, and safety requirements.
- `validate_dataset.py` checks the fixture locally. It does not contact Elastic.

## What the records represent

| Event IDs | Purpose |
| --- | --- |
| evt-001 to evt-005 | Main timeline: logon, hidden PowerShell with harmless encoded text, service creation command, service-installed event, and a connection to TEST-NET-3. |
| evt-006 | Incomplete process record. It lacks a process ID and parent process. |
| evt-007 | Prompt-injection test. Instruction-like text appears inside a log message and must remain data. |
| evt-008 | Benign control on a different lab host. |

All records use lab host names, the `labels.synthetic` marker, and the documentation-only address range `203.0.113.0/24`. The encoded sample in evt-002 decodes to `SANDBOX`, not executable content.

## Validate the fixture

From this folder, run:

```sh
python3 validate_dataset.py
```

Expected output starts with `PASS` for the eight records and safety checks. This only validates the sample files. It is not an Elastic test.

## Load the events into Elastic

Only do this in your own lab. Open Kibana Dev Tools and paste the contents of `data/security-alert.bulk.ndjson` after this request:

```http
POST _bulk
```

The bulk file writes only to `synthetic-alert-lab`. It does not delete or update other indices. Check the response for `"errors": false`.

Then confirm the records exist:

```http
GET synthetic-alert-lab/_search
{
  "size": 20,
  "sort": [{"@timestamp": "asc"}]
}
```

Check the index and result count before moving on. If Kibana returns mapping or permission errors, stop and record the exact error. Do not grant the agent write access to make an error go away.

## First investigation question

Can you connect evt-001 through evt-005 into one timeline using the host name, process entity ID, service name, and timestamps? Start by checking the count, then inspect each event. Note which fields support each statement and which facts the records cannot establish.

## Safety boundaries

- Use only these synthetic records for this exercise.
- Give any future assistant read-only credentials scoped to this single lab index.
- Do not provide write, delete, shell, isolation, account-disable, or response-action tools.
- Treat every event field as untrusted input, including evt-007's message.
- Keep statements tied to event IDs. Mark missing evidence as unknown.

## Current status

Milestone 1: synthetic fixture and expected findings prepared. Local validation is the next check. Elastic import, query validation, and all agent work remain pending. The project must not be described as tested in a live Elastic environment until those checks have been run and recorded.
