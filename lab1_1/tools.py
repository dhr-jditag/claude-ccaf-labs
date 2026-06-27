"""
Lab 1.1
Exercise 1
Tool definitions.
"""

from typing import List
import random


PRODUCT_AREAS = [
    "Billing",
    "Platform",
    "Integrations",
    "Security",
    "Onboarding"
]

SEVERITIES = [
    "P1-Critical",
    "P2-High",
    "P3-Medium",
    "P4-Low"
]

INTENTS = [
    "Bug",
    "Question",
    "Feature Request",
    "Billing Dispute"
]


def classify_ticket(ticket_text: str, fields_needed: List[str]) -> dict:
    """
    Simulated classifier.
    """

    values = {
        "product_area": random.choice(PRODUCT_AREAS),
        "severity": random.choice(SEVERITIES),
        "intent": random.choice(INTENTS)
    }

    return {
        field: values[field]
        for field in fields_needed
        if field in values
    }