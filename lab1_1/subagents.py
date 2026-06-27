import json
from typing import Dict, Any
from config import client, MODEL


def clean_json_string(text: str) -> str:
    """
    Cleans markdown code block fences and whitespace from a JSON response string.
    """
    text = text.strip()
    if text.startswith("```json"):
        text = text[len("```json"):]
    elif text.startswith("```"):
        text = text[len("```"):]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()


def run_classifier(ticket: str) -> Dict[str, Any]:
    """
    Classify the support ticket into product_area, severity, and intent.
    Responds only in JSON.
    """
    system_prompt = (
        "You are an expert support ticket classifier.\n\n"
        "Classify the ticket into exactly these fields:\n"
        "- product_area (one of: Billing, Platform, Integrations, Security, Onboarding)\n"
        "- severity (one of: P1-Critical, P2-High, P3-Medium, P4-Low)\n"
        "- intent (one of: Bug, Question, Feature Request, Billing Dispute)\n\n"
        "Respond ONLY with a valid JSON object matching these keys. Do not include any introductory or concluding text, explanation, or markdown formatting outside the JSON."
    )
    
    response = client.messages.create(
        model=MODEL,
        max_tokens=300,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": ticket
            }
        ]
    )
    
    response_text = response.content[0].text
    cleaned_text = clean_json_string(response_text)
    
    try:
        return json.loads(cleaned_text)
    except Exception as e:
        print(f"Warning: classifier JSON parsing failed: {e}. Raw response: {response_text}")
        return {}


def run_crm_enricher(customer_email: str, classification: Dict[str, Any]) -> Dict[str, Any]:
    """
    Simulate a CRM lookup for the customer.
    Returns account_tier, sla_tier, account_manager, contract_value.
    """
    system_prompt = (
        "You are a CRM assistant.\n\n"
        "Simulate a CRM lookup based on the customer email and classification data.\n"
        "Return a JSON object containing at least these fields:\n"
        "- account_tier\n"
        "- sla_tier\n"
        "- account_manager\n"
        "- contract_value\n\n"
        "Respond ONLY with the JSON object."
    )
    
    user_prompt = (
        f"Customer Email: {customer_email}\n"
        f"Classification: {json.dumps(classification)}"
    )
    
    response = client.messages.create(
        model=MODEL,
        max_tokens=300,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )
    
    response_text = response.content[0].text
    cleaned_text = clean_json_string(response_text)
    
    try:
        return json.loads(cleaned_text)
    except Exception as e:
        print(f"Warning: CRM JSON parsing failed: {e}. Raw response: {response_text}")
        # Hardcoded fallback as allowed by the lab instructions
        return {
            "account_tier": "Enterprise",
            "sla_tier": "Priority",
            "account_manager": "John Doe",
            "contract_value": "$100,000"
        }


def run_drafter(ticket: str, classification: Dict[str, Any], crm: Dict[str, Any]) -> str:
    """
    Draft a professional first-response email referencing the SLA tier.
    Composes a context string from all three arguments.
    """
    system_prompt = (
        "You draft professional first-response support emails for customers.\n"
        "You must explicitly reference their SLA tier in the response and keep the tone professional."
    )
    
    user_prompt = (
        f"Ticket Content:\n{ticket}\n\n"
        f"Ticket Classification:\n{json.dumps(classification)}\n\n"
        f"Customer CRM Data:\n{json.dumps(crm)}"
    )
    
    response = client.messages.create(
        model=MODEL,
        max_tokens=500,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )
    
    return response.content[0].text


def run_validator(draft: str, classification: Dict[str, Any], crm: Dict[str, Any]) -> str:
    """
    Check product area, SLA match, and tone.
    Reply APPROVED or list issues.
    """
    system_prompt = (
        "You validate drafted support responses before they are sent to customers.\n"
        "Check that the draft references the correct product area, matches the SLA tier, and has a professional tone.\n"
        "If acceptable, reply exactly with 'APPROVED'. Otherwise, list the issues."
    )
    
    sla_tier = crm.get("sla_tier", "Unknown")
    account_tier = crm.get("account_tier", "Unknown")
    
    user_prompt = (
        f"Contract & SLA Details:\n"
        f"- SLA Tier: {sla_tier}\n"
        f"- Account Tier: {account_tier}\n\n"
        f"Classification:\n{json.dumps(classification)}\n\n"
        f"Draft Response to Validate:\n{draft}"
    )
    
    response = client.messages.create(
        model=MODEL,
        max_tokens=300,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )
    
    return response.content[0].text