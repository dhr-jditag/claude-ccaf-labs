from lab1_1.context import TicketContext
from lab1_1.subagents import (
    run_classifier,
    run_crm_enricher,
    run_drafter,
    run_validator,
)


def coordinator_v2(ticket_id: str, raw_ticket: str, customer_email: str) -> TicketContext:
    print("=" * 60)
    print("Coordinator V2 (Exercise 3) Started")
    print("=" * 60)

    # Construct the TicketContext
    ctx = TicketContext(
        ticket_id=ticket_id,
        raw_ticket=raw_ticket,
        customer_email=customer_email,
    )

    # 1. Classifier
    print("\n--- Running Classifier ---")
    classification = run_classifier(ctx.raw_ticket)
    ctx.product_area = classification.get("product_area")
    ctx.severity = classification.get("severity")
    ctx.intent = classification.get("intent")
    print(f"Classification saved: product_area={ctx.product_area}, severity={ctx.severity}, intent={ctx.intent}")

    # 2. CRM Enricher
    print("\n--- Running CRM Enricher ---")
    # Pass only the specific fields each subagent needs
    class_dict = {
        "product_area": ctx.product_area,
        "severity": ctx.severity,
        "intent": ctx.intent
    }
    crm_data = run_crm_enricher(ctx.customer_email, class_dict)
    ctx.account_tier = crm_data.get("account_tier")
    ctx.sla_tier = crm_data.get("sla_tier")
    ctx.account_manager = crm_data.get("account_manager")
    print(f"CRM saved: account_tier={ctx.account_tier}, sla_tier={ctx.sla_tier}, account_manager={ctx.account_manager}")

    # 3. Drafter
    print("\n--- Running Drafter ---")
    # Pass only the specific fields each subagent needs
    crm_dict = {
        "account_tier": ctx.account_tier,
        "sla_tier": ctx.sla_tier,
        "account_manager": ctx.account_manager
    }
    draft = run_drafter(ctx.raw_ticket, class_dict, crm_dict)
    ctx.draft_response = draft
    print("Draft response saved.")

    # 4. Validator
    print("\n--- Running Validator ---")
    # Pass only the specific fields each subagent needs
    validation = run_validator(ctx.draft_response, class_dict, crm_dict)
    ctx.validation_result = validation
    print("Validation result saved.")

    # At the end, print the full ctx object to confirm all fields are populated
    print("\n" + "=" * 60)
    print("FINAL CONTEXT OBJECT")
    print("=" * 60)
    print(ctx)

    return ctx


if __name__ == "__main__":
    ticket_id = "TCK-2002"
    customer_email = "sarah.chen@globalcorp.com"
    raw_ticket = """
From: sarah.chen@globalcorp.com
Subject: Cannot access SSO login — entire team locked out

Our team of 40 has been unable to log in via SSO since 09:00 this morning.
We have a client demo in 3 hours.
This is completely blocking us.
"""
    coordinator_v2(ticket_id, raw_ticket, customer_email)
