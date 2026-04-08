from google.adk.agents import LlmAgent
from . import prompt

MODEL = "gemini-1.5-flash"

polisher_agent = LlmAgent(
    name="polisher",
    model=MODEL,
    description="Fine-tunes text for grammar, style, flow, and professional impact.",
    instruction=prompt.POLISHER_AGENT_PROMPT,
    output_key="polisher_output",
)
