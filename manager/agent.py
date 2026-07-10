from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.agent_tool import AgentTool

from .subagents.funnynerds.agent import root_agent as  funnynerds
#from .subagents.news_analyst.agent import news_analyst
from .subagents.stock_analyst.agent import root_agent as stock_analyst
from Newstool_agent.agent import root_agent as news_analyst
#from .tools.tools import get_current_time
'''def say(message: str) -> str:
    """Returns the final response to the user."""
    return message'''

model = LiteLlm(
    model="ollama/qwen2.5:7b-instruct",
    api_base="http://localhost:11434"
)

root_agent = Agent(
    name="manager",
    model=model,
    description="Manager agent",
    instruction="""
You are a manager agent.

Your job is to delegate work to the appropriate agent.

Available agents:
- stock_analyst
- funnynerds
- news_analyst



Rules:
- Delegate stock-related tasks to stock_analyst.
- Delegate news analysis tasks to news_analyst.
- Delegate jokes or fun conversations to funnynerds.
- Never answer a task yourself if another agent specializes in it.
- DO NOT invent tools or new agents. Only use the tools and agents provided.

After every tool call, your next action MUST be one of these:

1. Produce plain text to the user.
2. Call one of the available tools.

Never call:
- respond_to_user , say, or any other function that does not exist.
These functions do not exist.

There is no function for responding.
Simply output plain text directly.
Do NOT wrap your final answer in any function call.
""",
    sub_agents=[
        funnynerds,
        stock_analyst,
        
    ],
    tools=[
        AgentTool(news_analyst),
        #AgentTool(say),
        #get_current_time,
    ],
)
#litellm 1.81.8