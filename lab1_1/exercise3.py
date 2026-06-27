"""
Exercise 3: Explicit Context Passing
"""

from lab1_1.coordinator_v2 import coordinator_v2

ticket_id = "TCK-1002"
customer_email = "sarah.chen@globalcorp.com"
raw_ticket = """
Subject: Cannot access SSO login — entire team locked out

Our team of 40 has been unable to log in via SSO since 09:00 this morning.
We have a client demo in 3 hours.
This is completely blocking us.
"""

if __name__ == "__main__":
    context = coordinator_v2(
        ticket_id=ticket_id,
        raw_ticket=raw_ticket,
        customer_email=customer_email,
    )