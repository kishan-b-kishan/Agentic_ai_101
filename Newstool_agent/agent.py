#from google.adk.agents import LlmAgent
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from .newstool import get_news
from pydantic import BaseModel, Field
from typing import List

class NewsItem(BaseModel):
    title: str = Field(description="Headline of the news")
    source: str = Field(description="Source of the news")

class NewsResponse(BaseModel):
    summary: str = Field(description="Short summary of overall news")
    sentiment: str = Field(description="Overall sentiment: positive/negative/neutral")
    articles: List[NewsItem] = Field(description="List of relevant news articles")

model = LiteLlm(
    model="ollama/qwen2.5:7b-instruct",
    api_base="http://localhost:11434"
)

root_agent = Agent(
    name="news_agent",
    model=model,
    description="Agent with news access",
    instruction="""
You are a financial news assistant.

You have access to this tool:

- get_news → Fetches latest news based on a query

Use it whenever the user asks about recent events,
company updates,company financial data, company statistics or news.

Rules:

- Only call get_news when user asks about news or updates
- Never invent new tools
- If required /asked then analyse the extracted news and provide insights, do not just return the news output.
- After receiving tool results, always respond to user
- Always produce a final natural language answer after using the tool, do not just return the tool output.
CRITICAL RULE — TOOL USAGE
- ALWAYS return JSON matching schema
- Do NOT return plain text
- Do NOT explain anything outside JSON

You have access to EXACTLY ONE tool:

get_news → Fetches latest news based on a query

You MUST NEVER:

- Invent new tools
- Call any tool other than get_news
- Use tools like parse_news, filter_news,analysis etc.

If you need to analyze results, do it yourself.

After receiving get_news results,
you MUST ALWAYS respond to the user.
Silence is never allowed,
IMPORTANT:
Your final output MUST be valid JSON.

""",
    tools=[get_news],
    #output_schema=NewsResponse,
    #output_key="news"
)

