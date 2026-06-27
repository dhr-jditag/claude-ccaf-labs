from lab1_1.subagents import (
    run_classifier,
    run_crm_enricher,
    run_drafter,
    run_validator,
)


def coordinator(ticket: str) -> None:
    print("=" * 60)
    print("Coordinator (Exercise 2) Started")
    print("=" * 60)

    # 1. Classifier
    print("\n--- Running Classifier ---")
    classification = run_classifier(ticket)
    print("Classifier Output:", classification)

    # 2. CRM Enricher
    print("\n--- Running CRM Enricher ---")
    # Extract customer email dynamically from ticket if available, or default to sarah's email.
    customer_email = "sarah.chen@globalcorp.com"
    for line in ticket.splitlines():
        if "from:" in line.lower():
            parts = line.split(":", 1)
            if len(parts) > 1:
                customer_email = parts[1].strip()
                break

    crm_data = run_crm_enricher(customer_email, classification)
    print("CRM Enricher Output:", crm_data)

    # 3. Drafter
    print("\n--- Running Drafter ---")
    draft = run_drafter(ticket, classification, crm_data)
    print("Drafter Output:\n", draft)

    # 4. Validator
    print("\n--- Running Validator ---")
    validation = run_validator(draft, classification, crm_data)
    print("Validator Output:\n", validation)

    print("\nWorkflow Completed Successfully!")


if __name__ == "__main__":
    # Test ticket definition matching the lab
    test_ticket = """
From: sarah.chen@globalcorp.com
Subject: Cannot access SSO login — entire team locked out

Our team of 40 has been unable to log in via SSO since 09:00 this morning.
We have a client demo in 3 hours.
This is completely blocking us.
"""
    coordinator(test_ticket)