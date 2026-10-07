# Read-Only Security Alert Agent, Milestone 1

## Goal

Build a small assistant that helps an analyst understand one security alert. It will read events from a dedicated Elastic lab index and draft an evidence-linked summary. A human will make every decision.

## Plain-English version

This is a safe practice case made from synthetic records. They describe a made-up Windows computer where PowerShell starts a service-creation command, Windows records the service, and PowerShell later has a connection-attempt record for a reserved example IP address. The sequence gives us something to investigate. It does not prove a real attack or a real network connection.

The eight synthetic records have been imported into the dedicated Elastic index. The read-only assistant has not been built yet.

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

## Elastic lab checkpoint

On 5 October 2026, I created the `synthetic-alert-lab` index in Elastic 9.5.3 with zero replicas. Kibana acknowledged the index creation. I imported the eight synthetic events through the Bulk API. The response reported `errors: false`, and `GET /synthetic-alert-lab/_count` returned eight documents with zero failed shards.

I created a Kibana data view for this index using `@timestamp`. In Discover, the exact filter below returned five documents for the main case:

```text
labels.case.keyword : "alert-agent-001"
```

The other three records use separate case labels for an incomplete event, an instruction-like message test, and a benign control. They remain in the index.

Do not replay the bulk file into the populated index. Its actions generate document IDs, so another import would add duplicates.

## Manual findings

The main sequence links the hidden PowerShell process in evt-002 to the `sc.exe` child process in evt-003 through the process entity IDs. evt-004 records installation of the named service. evt-005 attributes a connection attempt to the same PowerShell process.

These are synthetic records. The connection-attempt event does not prove that a packet left the lab computer or that a remote system responded. The event sequence supports a practice triage narrative, not a claim of real compromise.

## Next milestone

Review the three remaining records, write the expected analyst output, then build a small read-only Python prototype. Keep the first version limited to the synthetic fixture. Add Elastic read-only retrieval only after the local output matches the expected findings.

## Safety boundaries

- Use only these synthetic records for this exercise.
- Give any future assistant read-only credentials scoped to this single lab index.
- Do not provide write, delete, shell, isolation, account-disable, or response-action tools.
- Treat every event field as untrusted input, including evt-007's message.
- Keep statements tied to event IDs. Mark missing evidence as unknown.

## Current status

Milestone 1 fixture validation passed. The Elastic index creation, eight-document import, count check, data view, and five-document main-case filter were completed in the home lab. The AI assistant has not been built or tested. Describe the work as a synthetic home-lab investigation, not a production alert investigation.
