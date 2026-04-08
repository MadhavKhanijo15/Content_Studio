from google.adk.agents import LlmAgent
from . import prompt

MODEL = "gemini-1.5-flash"

research_agent = LlmAgent(
    name="research_agent",
    model=MODEL,
    description="Researches topics, validates facts, and provides context for writing.",
    instruction=prompt.RESEARCH_AGENT_PROMPT,
    output_key="research_output",
)
