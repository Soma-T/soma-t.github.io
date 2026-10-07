---
layout: single
title: "Projects"
permalink: /projects/
author_profile: true
---

This page separates existing lab exercises from projects still being built. I’ll add results only after testing them.

## Security detection and investigation lab

**Stage: active lab work**

My security lab includes Elastic Security. Current detection and investigation exercises cover:

- Agent Spoofing: Multiple Hosts Using Same Agent.
- Failed logins.
- Suspicious process activity, including rundll32.
- Windows service creation.
- New DNS domains.
- The benign EICAR test file.

Each write-up will explain the alert logic, relevant event fields, investigation steps and what the evidence does or does not show.

## Read-Only Security Alert Agent with Synthetic Logs

**Stage: milestone 1 in progress. Eight synthetic events imported and reviewed in Elastic. The read-only agent is not built yet.**

The first milestone uses eight synthetic Windows events, expected findings, and a local validation script. I created the dedicated `synthetic-alert-lab` index in Elastic 9.5.3, imported the eight records, and verified the document count. An exact Discover filter returns five events for the main case. The remaining three records test missing evidence, instruction-like log content, and a benign control.

The goal is to build a small assistant that helps an analyst investigate a test alert. It will use read-only access to a dedicated Elastic lab index and produce:

- A short summary linked to supporting events.
- An event timeline.
- Missing or conflicting evidence.
- Follow-up checks for a human analyst.

The project will use synthetic or lab-generated telemetry. The agent will not write to Elastic, isolate hosts, disable accounts or run response actions. I’ll test how it handles incomplete evidence and instruction-like text inside log fields.

[Open the project lab page](/projects/read-only-security-alert-agent/)

[Read the project brief](/notes/read-only-security-alert-agent-project-brief/)

## AI and malware research

My MSc research examined image-based Android malware detection using deep learning. I’m building on that foundation as I study model evaluation and practical uses of AI in security. Future experiments will include the data source, evaluation method and limitations.
