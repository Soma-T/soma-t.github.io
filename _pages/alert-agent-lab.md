---
layout: single
title: "Read-Only Security Alert Agent Lab"
permalink: /projects/read-only-security-alert-agent/
author_profile: true
---

## Project goal

Build a small assistant that reads a test alert and related events from a dedicated Elastic lab index. It will draft a timeline, link statements to event evidence, report gaps, and suggest checks for a human analyst. The assistant will have no response actions.

## Milestone 1: synthetic case

**Status: project index created and verified. Event import is next.**

The practice case contains eight clearly marked synthetic Windows events. The main sequence covers a lab-user logon, hidden PowerShell with harmless encoded text, a service creation command, a service-installed record, and a connection to a documentation-only test IP. It also includes an incomplete event, instruction-like text inside a log message, and a benign control event.

The event sequence is a triage exercise. It does not prove malware or malicious intent. The practice data does not come from an employer, client, patient, or real endpoint.

## Elastic checkpoint

On 5 October 2026, I created the dedicated `synthetic-alert-lab` index in my Elastic 9.5.3 home lab. Kibana returned HTTP 200 and confirmed the index was created. A follow-up index check showed green health, one primary shard, zero replicas and zero documents.

This verifies the empty index only. The synthetic events have not yet been imported or queried.

## How I will test it

1. Load the eight synthetic events into `synthetic-alert-lab`.
2. Confirm the document count and inspect the event fields.
3. Reconstruct the timeline and record the event IDs supporting each finding.
4. Check whether the incomplete record is reported as a correlation gap.
5. Check whether the instruction-like message remains untrusted evidence.
6. Build the read-only assistant only after the expected findings are clear.

The assistant will never change Elastic data, isolate a host, disable an account, or run a response action.

## Project files

The data, expected findings, validation script, and lab runbook are in the [project source folder](https://github.com/Soma-T/soma-t.github.io/tree/master/lab-projects/read-only-alert-agent).

## Current evidence

The fixture passes local validation. The Elastic index creation and empty-index check passed. The next evidence will cover event import, count, query results, findings and limitations. The uploaded screenshot includes an index UUID, so I will crop or obscure it before sharing the image publicly.
