---
layout: single
title: "Read-Only Security Alert Agent Lab"
permalink: /projects/read-only-security-alert-agent/
author_profile: true
---

## Project goal

Build a small assistant that reads a test alert and related events from a dedicated Elastic lab index. It will draft a timeline, link statements to event evidence, report gaps, and suggest checks for a human analyst. The assistant will have no response actions.

## Milestone 1: synthetic case

**Status: prepared. Elastic validation is pending.**

The practice case contains eight clearly marked synthetic Windows events. The main sequence covers a lab-user logon, hidden PowerShell with harmless encoded text, a service creation command, a service-installed record, and a connection to a documentation-only test IP. It also includes an incomplete event, instruction-like text inside a log message, and a benign control event.

The event sequence is a triage exercise. It does not prove malware or malicious intent. The practice data does not come from an employer, client, patient, or real endpoint.

## How I will test it

1. Validate the sample files and confirm every event is marked synthetic.
2. Load the events into a dedicated Elastic lab index.
3. Reconstruct the timeline and record the event IDs supporting each finding.
4. Check whether the incomplete record is reported as a correlation gap.
5. Check whether the instruction-like message remains untrusted evidence.
6. Build the read-only assistant only after the expected findings are clear.

The assistant will never change Elastic data, isolate a host, disable an account, or run a response action.

## Project files

The data, expected findings, validation script, and lab runbook are in the [project source folder](https://github.com/Soma-T/soma-t.github.io/tree/master/lab-projects/read-only-alert-agent).

## Current evidence

The sample files have been prepared. Local fixture validation and the Elastic lab import have not yet been recorded. I will add the query output, screenshots or saved evidence, findings, and limitations after running those checks in my lab.
