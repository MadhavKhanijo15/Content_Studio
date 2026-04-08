import os
# Force ADK to look for the API Key instead of Vertex AI
os.environ["GOOGLE_API_BACKEND"] = "generativeai"
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
# Importing sub-agents 
from .sub_agents.research_agent import research_agent
from .sub_agents.creative_writer_agent import creative_writer_agent
from .sub_agents.polisher_agent import polisher_agent

MODEL = "gemini-1.5-pro" 

content_coordinator = LlmAgent(
    name="content_studio_coordinator",
    model=MODEL,
    description=(
        "Orchestrates a multi-agent workflow to research, write, "
        "and polish high-quality text content."
    ),
    instruction=prompt.CONTENT_COORDINATOR_PROMPT,
    output_key="coordinator_output",
    tools=[
        AgentTool(agent=research_agent),
        AgentTool(agent=creative_writer_agent),
        AgentTool(agent=polisher_agent),
    ],
)

root_agent = content_coordinator
