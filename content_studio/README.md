AI Content Studio: Autonomous Multi-Agent Orchestrator
A sophisticated content generation engine built on the Google ADK (Agent Development Kit). This project demonstrates a Decentralized Multi-Agent Architecture where specialized AI entities collaborate to transform a raw user prompt into a polished, professional-grade long-form article.

-> Core Philosophy
The Content Studio moves away from the "Single-Prompt" paradigm. Instead, it utilizes Task Decomposition, where a complex objective is broken down into modular sub-tasks, handled by agents with distinct personas and tool-sets.

-> System Architecture
The studio follows a Hierarchical Orchestration pattern:

Orchestrator (Root Agent): Acts as the Controller. It parses the user query, determines the scope, and triggers the workflow.

Knowledge Engineer (Research Agent): Responsible for data retrieval and factual grounding.

Narrative Architect (Writer Agent): Transforms raw data into a structured, engaging narrative.

Quality Assurance (Polisher Agent): Conducts final syntax checks, tone adjustment, and platform-specific optimization (e.g., SEO/Hashtags).

-> Technical Specifications
Framework: Google ADK (Agent Development Kit)

Orchestration Logic: Asynchronous Agent Communication

Language: Python 3.12

Inference Engine: Google Gemini API (Flash/Pro)

-> Technical Features
State Management: Ensures context is passed seamlessly from Research to Writing to Polishing.

Persona Engineering: Each agent is hard-coded with specific system instructions to prevent "Hallucination" and "Tone Drift."

Modular Design: New agents (e.g., Image Generator, Fact Checker) can be plugged into the adk ecosystem with minimal configuration.

-> Setup & Execution
Environment Setup:
Bash
python3 -m venv .venv
source .venv/bin/activate
pip install google-adk

Authentication:
Bash
export GOOGLE_API_KEY='your_api_key'

Deployment:
Bash
adk run .
