# pyrefly: ignore [missing-import]
from anthropic.types import ToolUseBlock

from config import client, MODEL

from lab1_2.tool_hooks import run_tool

TOOLS = [
    {
        "name": "quarantine_host",
        "description": "Quarantine a compromised host.",
        "input_schema": {
            "type": "object",
            "properties": {
                "hostname": {
                    "type": "string"
                }
            },
            "required": ["hostname"]
        }
    },
    {
        "name": "block_ip",
        "description": "Block a malicious IP.",
        "input_schema": {
            "type": "object",
            "properties": {
                "ip": {
                    "type": "string"
                }
            },
            "required": ["ip"]
        }
    }
]


messages = [
    {
        "role": "user",
        "content":
        """
A ransomware attack has been detected.

Quarantine host "dev-server".

Then block IP "8.8.8.8".
"""
    }
]

iteration = 1

while True:

    print(f"\n========== ITERATION {iteration} ==========\n")

    response = client.messages.create(

        model=MODEL,

        max_tokens=500,

        tools=TOOLS,

        messages=messages
    )

    print("Stop Reason:", response.stop_reason)

    messages.append(
        {
            "role": "assistant",
            "content": response.content
        }
    )

    if response.stop_reason != "tool_use":

        print("\nFINAL ANSWER\n")

        print(response.content[0].text)

        break

    tool_results = []

    for block in response.content:

        if isinstance(block, ToolUseBlock):

            print(f"\nTool Requested: {block.name}")

            print(block.input)

            result = run_tool(
                block.name,
                block.input
            )

            print("Tool Result:", result)

            tool_results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result
                }
            )

    messages.append(
        {
            "role": "user",
            "content": tool_results
        }
    )

    iteration += 1