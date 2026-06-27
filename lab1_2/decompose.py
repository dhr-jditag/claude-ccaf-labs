from typing import List


# ==========================================
# Fixed Workflow
# ==========================================

def fixed_workflow():

    print("=" * 60)
    print("FIXED WORKFLOW")
    print("=" * 60)

    steps = [
        "Collect security alerts",
        "Summarize alerts",
        "Generate morning report",
        "Email report"
    ]

    for i, step in enumerate(steps, start=1):
        print(f"Step {i}: {step}")


# ==========================================
# Adaptive Workflow
# ==========================================

def adaptive_workflow(alert_type: str):

    print("\n" + "=" * 60)
    print("ADAPTIVE WORKFLOW")
    print("=" * 60)

    print(f"\nIncoming Alert: {alert_type}")

    if alert_type.lower() == "malware":

        workflow = [
            "Isolate endpoint",
            "Collect forensic artifacts",
            "Run malware scan",
            "Notify SOC"
        ]

    elif alert_type.lower() == "phishing":

        workflow = [
            "Block sender",
            "Remove malicious email",
            "Notify affected users",
            "Reset credentials"
        ]

    elif alert_type.lower() == "network":

        workflow = [
            "Block IP",
            "Capture network traffic",
            "Check firewall logs",
            "Notify Network Team"
        ]

    else:

        workflow = [
            "Create investigation ticket",
            "Assign analyst",
            "Manual triage"
        ]

    print("\nWorkflow:")

    for i, step in enumerate(workflow, start=1):
        print(f"Step {i}: {step}")


# ==========================================
# Demo
# ==========================================

if __name__ == "__main__":

    fixed_workflow()

    adaptive_workflow("malware")

    adaptive_workflow("phishing")

    adaptive_workflow("network")

    adaptive_workflow("unknown")