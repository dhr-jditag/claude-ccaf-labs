import os

from dotenv import load_dotenv
from anthropic import AnthropicBedrock

load_dotenv()

client = AnthropicBedrock(
    aws_region=os.getenv("AWS_REGION")
)

MODEL = os.getenv("ANTHROPIC_MODEL")


def main():

    print("=" * 60)
    print("Testing Bedrock Connection")
    print("=" * 60)

    response = client.messages.create(
        model=MODEL,
        max_tokens=100,
        messages=[
            {
                "role": "user",
                "content": "Say hello from Claude."
            }
        ]
    )

    print("\nFULL RESPONSE OBJECT\n")
    print(response)

    print("\n--------------------------------")

    print("\nSTOP REASON")
    print(response.stop_reason)

    print("\n--------------------------------")

    print("\nCONTENT BLOCKS")

    for block in response.content:
        print(block)

if __name__ == "__main__":
    main()