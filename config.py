import os

from dotenv import load_dotenv
from anthropic import AnthropicBedrock

load_dotenv()

MODEL = os.getenv("ANTHROPIC_MODEL")

client = AnthropicBedrock(
    aws_region=os.getenv("AWS_REGION")
)