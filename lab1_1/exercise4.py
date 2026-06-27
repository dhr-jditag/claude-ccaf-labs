"""
Exercise 4: Programmatic Step Enforcement (Gates)
"""

from lab1_1.coordinator_v3 import coordinator_v3
from lab1_1.coordinator_v3_sabotage import coordinator_v3_sabotage

ticket_id = "TCK-1003"
customer_email = "sarah.chen@globalcorp.com"
raw_ticket = """
Subject: Cannot access SSO login — entire team locked out

Our team of 40 has been unable to log in via SSO since 09:00 this morning.
We have a client demo in 3 hours.
This is completely blocking us.
"""

if __name__ == "__main__":
    print("=== RUNNING V3 COORDINATOR (NORMAL) ===")
    ctx_normal = coordinator_v3(
        ticket_id=ticket_id,
        raw_ticket=raw_ticket,
        customer_email=customer_email,
    )
    
    print("\n" + "=" * 60)
    print("=== RUNNING V3 COORDINATOR (SABOTAGED) ===")
    ctx_sabotage = coordinator_v3_sabotage(
        ticket_id=ticket_id,
        raw_ticket=raw_ticket,
        customer_email=customer_email,
    )