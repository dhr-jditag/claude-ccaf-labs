"""
Exercise 2: Basic Multi-Agent Pipeline
"""

from lab1_1.coordinator import coordinator

ticket = """
From: sarah.chen@globalcorp.com
Subject: Cannot access SSO login — entire team locked out

Our team of 40 has been unable to log in via SSO since 09:00 this morning.
We have a client demo in 3 hours.
This is completely blocking us.
"""

if __name__ == "__main__":
    coordinator(ticket)