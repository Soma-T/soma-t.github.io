---
layout: single
title: "Project Brief: Read-Only Security Alert Agent with Synthetic Logs"
date: 2026-10-05
permalink: /notes/read-only-security-alert-agent-project-brief/
categories: [security, ai, home-lab]
tags: [elastic-security, alert-triage, synthetic-logs, responsible-ai]
excerpt: "The goal, boundaries and test plan for a read-only alert triage assistant in an Elastic home lab."
read_time: true
---

**Project stage: planning. The assistant is not built or tested yet.**

I want to learn whether an AI assistant can help an analyst understand a security alert while keeping the evidence visible and response decisions with the human.

I already use an Elastic Security home lab for detection and investigation exercises. This project will add a separate, read-only workflow using synthetic or lab-generated events.

## The question

Given a test alert, can an assistant retrieve the related events and draft a short summary that an analyst can verify?

## Planned workflow

1. Start with one alert and a defined time window.
2. Retrieve related events from a dedicated test index with read-only access.
3. Draft a timeline and link each finding to the supporting events.
4. List missing or conflicting evidence.
5. Suggest follow-up checks for the analyst to consider.

## Safety boundaries

The project will use synthetic or lab-generated telemetry. It will not use employer, client or patient data. The assistant will not write to Elastic, isolate hosts, disable accounts or run response actions.

Text inside event fields is untrusted data. I’ll test whether instruction-like text inside a log changes the output. It must remain evidence to analyse, not instructions for the assistant.

## How I’ll evaluate it

I’ll test normal events, incomplete records, conflicting events and misleading text inside a log field. I’ll check whether every claim has evidence, whether gaps are called out and whether the assistant avoids conclusions the logs cannot support.

## Next step

I’ll create a small synthetic event set and define the expected timeline and findings before writing the retrieval code. The next post will report what I build and what the tests show.
