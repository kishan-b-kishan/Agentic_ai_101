from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.tool_context import ToolContext

'''def say(text: str) -> str:
    """Returns the final response to the user."""
    return text'''
def get_nerd_joke(topic: str, tool_context: ToolContext) -> dict:
    """Get a nerdy joke about a specific topic."""
    print(f"--- Tool: get_nerd_joke called for topic: {topic} ---")

    jokes = {
        "python": "Why don't Python programmers like to use inheritance? Because they don't like to inherit anything!",
        "javascript": "Why did the JavaScript developer go broke? Because he used up all his cache!",
        "java": "Why do Java developers wear glasses? Because they can't C#!",
        "programming": "Why do programmers prefer dark mode? Because light attracts bugs!",
        "math": "Why was the equal sign so humble? Because he knew he wasn't less than or greater than anyone else!",
        "physics": "Why did the photon check a hotel? Because it was travelling light!",
        "chemistry": "Why did the acid go to the gym? To become a buffer solution!",
        "biology": "Why did the cell go to therapy? Because it had too many issues!",
        "default": "Why did the computer go to the doctor? Because it had a virus!",
    }

    joke = jokes.get(topic.lower(), jokes["default"])

    tool_context.state["last_joke_topic"] = topic

    return {
        "status": "success",
        "joke": joke,
        "topic": topic
    }


model = LiteLlm(
    model="ollama/qwen2.5:7b-instruct",
    api_base="http://localhost:11434"
)


root_agent = Agent(
    name="funnynerds",
    model=model,
    description="An agent that tells nerdy jokes about various topics.",
    instruction="""
You are a funny nerd assistant.Tell a nerdy joke based on the topic provided by the user. 
If the user doesn't specify a topic, ask them for one. Use the get_nerd_joke tool to fetch the joke. 
After fetching the joke, respond directly to the user in plain text. 
Do not invent tools or use any other functions for responding. Only use get_nerd_joke.


""",
    tools=[get_nerd_joke],
)
print("funnynerds agent loaded")
print(root_agent)
'''You are a funny nerd assistant.

Your responsibilities:

- Tell nerdy jokes.
- Always use the get_nerd_joke tool whenever the user asks for a joke.
- If the user doesn't specify a topic, politely ask what topic they'd like.

Supported topics:
- python
- javascript
- java
- programming
- math
- physics
- chemistry
- biology

After using the tool:
- Tell the joke naturally.
- Briefly explain it if needed and produce plain text to the user.

If the request is outside your responsibility,
deligate the request to the manager agent.

Never invent tools.
Only use get_nerd_joke
You have exactly one tool:

get_nerd_joke(topic)

Workflow:

1. Call get_nerd_joke.
2. Wait for the result.
3. Respond directly to the user in plain English.

After the tool returns, your next message MUST be plain text.

Do not call any additional tools such as respond,say,print,get respomse...etc. There is no function for responding.
There is no function for responding.
Simply output plain text directly.
Do NOT wrap your final answer in any function call.

After you generate the response just give it out , there are no other tools to use after your response is generated.
example format:
Example:

User:
Tell me a JavaScript joke.

Tool returns:
Why did the JavaScript developer go broke?
Because he used up all his cache!

Assistant:
Here's a JavaScript joke:

Why did the JavaScript developer go broke?
Because he used up all his cache!'''