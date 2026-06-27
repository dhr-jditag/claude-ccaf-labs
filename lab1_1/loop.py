from config import client, MODEL
from lab1_1.tools import classify_ticket


TEST_TICKET = """
From: sarah.chen@globalcorp.com
Subject: Cannot access SSO login — entire team locked out

Our team of 40 has been unable to log in via SSO since 09:00 this morning.
We have a client demo in 3 hours.
This is completely blocking us.
"""


TOOLS = [
    {
        "name": "classify_ticket",
        "description": "Classify a support ticket.",
        "input_schema": {
            "type": "object",
            "properties": {
                "ticket_text": {
                    "type": "string"
                },
                "fields_needed": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            },
            "required": [
                "ticket_text",
                "fields_needed"
            ]
        }
    }
]


messages = [
    {
        "role": "user",
        "content": f"""
Classify this support ticket.

Use the classify_ticket tool until
product_area,
severity,
intent
are all identified.

Ticket:

{TEST_TICKET}
"""
    }
]


iteration = 1

while True:

    print(f"\nIteration {iteration}")

    response = client.messages.create(
        model=MODEL,
        max_tokens=500,
        tools=TOOLS,
        messages=messages,
    )

    print("Stop Reason:", response.stop_reason)

    # VERY IMPORTANT
    messages.append(
        {
            "role": "assistant",
            "content": response.content,
        }
    )

    if response.stop_reason == "end_turn":

        print("\nFINAL ANSWER\n")

        for block in response.content:
            if block.type == "text":
                print(block.text)

        break

    if response.stop_reason == "tool_use":

        tool_results = []

        for block in response.content:

            if block.type != "tool_use":
                continue

            print("\nCalling Tool:", block.name)

            result = classify_ticket(
                **block.input
            )

            print(result)

            tool_results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result),
                }
            )

        messages.append(
            {
                "role": "user",
                "content": tool_results,
            }
        )

    iteration += 1