# 🦞 OpenClaw-Lineage: Cryptographic Intent Attribution

**A Zero-Trust Framework for Autonomous Agent Attribution.**

[![Award](https://img.shields.io/badge/2026_Cybersecurity_Excellence-Nominee-gold.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## ⚠️ The "Attribution Gap" Problem
Current autonomous agents follow the ReAct (Reason + Act) pattern. However, if an agent is hijacked via Indirect Prompt Injection, there is no cryptographically signed link between the original human prompt and the final shell command. Static analysis (like VirusTotal skill scanning) cannot prevent runtime manipulation. 

## 🛡️ The Solution: A "Black Box Recorder"
OpenClaw-Lineage introduces a **Lineage-Aware Gateway**. It cryptographically signs the "Intent Chain" using Ed25519 signatures, ensuring every terminal command is traced back to a verified human initiator. 

If a hijacked sub-agent attempts to execute an unauthorized payload, the execution layer instantly blocks it due to a mathematically orphaned intent.

## 🚀 Quick Start & Simulation

1. **Install Dependencies:**
   `pip install cryptography`

2. **Run the Simulation:**
   `python simulate_attack.py`

### Proof of Concept Output
The framework successfully differentiates between legitimate human intent and a hijacked rogue agent:

```text
=== 🟢 PHASE 1: LEGITIMATE HUMAN INTENT ===
User Request: Check my current directory
[*] Intent Signed. Lineage UUID: f5a931b0-dfcb-41c7-aa32-683af60323c8
Agent executing: ls -la
[+] Lineage mathematically verified. Executing command...

=== 🔴 PHASE 2: INDIRECT PROMPT INJECTION (HIJACK) ===
Rogue Agent attempting to execute: echo 'Pretending to read /etc/shadow...'
Attempting to bypass enforcer with orphaned signature...
Terminal Output: [-] CRITICAL ERROR: Lineage verification failed. Orphaned intent detected. Execution blocked.
