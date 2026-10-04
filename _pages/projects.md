---
layout: single
title: "Projects"
permalink: /projects/
author_profile: true
---

This page separates existing lab exercises from projects still being built. I’ll add results only after testing them.

## Elastic Security detection and investigation lab

**Stage: active lab work**

My Elastic Security home lab includes detection and investigation exercises covering:

- Agent identity conflicts, including an ES|QL alert for multiple hosts using the same agent.
- Failed logins.
- Suspicious process activity, including rundll32.
- Windows service creation.
- New DNS domains.
- Test malware indicators such as EICAR.

Each write-up will explain the alert logic, relevant event fields, investigation steps and what the evidence does or does not show.

## Read-Only Security Alert Agent with Synthetic Logs

**Stage: planned**

The goal is to build a small assistant that helps an analyst investigate a test alert. It will use read-only access to a dedicated Elastic lab index and produce:

- A short summary linked to supporting events.
- An event timeline.
- Missing or conflicting evidence.
- Follow-up checks for a human analyst.

The project will use synthetic or lab-generated telemetry. The agent will not write to Elastic, isolate hosts, disable accounts or run response actions. I’ll test how it handles incomplete evidence and instruction-like text inside log fields.

[Read the project brief](/notes/read-only-security-alert-agent-project-brief/)

## AI and malware research

My MSc research examined image-based Android malware detection using deep learning. I’m building on that foundation as I study model evaluation and practical uses of AI in security. Future experiments will include the data source, evaluation method and limitations.
