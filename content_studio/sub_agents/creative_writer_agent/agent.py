from google.adk.agents import LlmAgent
from . import prompt

MODEL = "gemini-1.5-pro"

creative_writer_agent = LlmAgent(
    name="creative_writer",
    model=MODEL,
    description="Drafts high-quality content based on research and user requirements.",
    instruction=prompt.CREATIVE_WRITER_PROMPT,
    output_key="writer_output",
)
