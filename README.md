# Claude CCA-F Labs

Implementation of the **Anthropic Claude Certified Associate – Foundations (CCA-F)** hands-on labs using **Python** and **Amazon Bedrock**.

## Overview

This repository contains my implementations of the official CCA-F labs while learning core concepts of Agentic AI, Claude tool use, workflow orchestration, and enterprise AI application development.

The implementations use the **Anthropic Python SDK** with **Amazon Bedrock** as the inference provider.

---

## Technologies

* Python 3.11+
* Anthropic Python SDK
* Amazon Bedrock
* Claude Sonnet
* Git & GitHub

---

## Repository Structure

```text
.
├── lab1_1/
│   ├── tools.py
│   ├── loop.py
│   ├── subagents.py
│   ├── context.py
│   ├── gates.py
│   ├── coordinator.py
│   ├── coordinator_v2.py
│   ├── coordinator_v3.py
│   └── ...
│
├── lab1_2/
│   ├── tool_hooks.py
│   ├── agent_with_hooks.py
│   ├── decompose.py
│   ├── session_manager.py
│   └── ...
│
├── config.py
├── requirements.txt
└── README.md
```

---

# Completed Labs

## ✅ Lab 1.1 – Tool Use & Multi-Agent Workflows

Concepts covered:

* Claude Tool Use
* Tool Schemas
* Agentic Loop
* Multi-Agent Coordination
* Shared Context
* Workflow Gates
* Coordinator Pattern

---

## ✅ Lab 1.2 – Hooks, Planning & Sessions

Concepts covered:

* Tool Hooks
* Validation Hooks
* Policy Enforcement
* Audit Logging
* Fixed Task Decomposition
* Adaptive Task Decomposition
* Session Persistence
* Session Forking
* Conversation Summarization

---

## Skills Demonstrated

* Claude Tool Calling
* Agentic AI Workflows
* Multi-Agent Orchestration
* Workflow State Management
* Guardrails & Policy Enforcement
* Session Management
* Amazon Bedrock Integration
* Python Application Design

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/dhr-jditag/claude-ccaf-labs.git
cd claude-ccaf-labs
```

### Create a virtual environment

```bash
conda create -n ccaf python=3.11
conda activate ccaf
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file (or export environment variables)


---

## Running the Labs

### Lab 1.1

```bash
python -m lab1_1.loop
python -m lab1_1.exercise2
python -m lab1_1.exercise3
python -m lab1_1.exercise4
```

### Lab 1.2

```bash
python -m lab1_2.test_hooks
python -m lab1_2.agent_with_hooks
python -m lab1_2.decompose
python -m lab1_2.test_session
```

---

## Learning Journey

This repository documents my hands-on implementation of the Anthropic CCA-F labs while learning modern Agentic AI patterns, including:

* Tool Calling
* Multi-Agent Systems
* Workflow Orchestration
* Context Management
* Deterministic Guardrails
* Task Decomposition
* Session Persistence

Additional labs will be added as I progress through the certification.

---

## Disclaimer

This repository contains **my own implementations** created while completing the Anthropic CCA-F learning labs.

It does **not** include proprietary course materials or official lab documentation.

---

## Author

**Dheeraj R**

* GitHub: https://github.com/dhr-jditag
* LinkedIn: https://www.linkedin.com/in/dheerajr12
