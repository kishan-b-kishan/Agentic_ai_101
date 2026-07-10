#print("Hello World!")
'''from dotenv import load_dotenv
import os
import google.generativeai as genai
#import asyncio
#from agents import Agent, Runner, trace
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API")

agent = Agent(name="Jokester", instructions="You are a joke teller", model="gemini-2.5-flash")


async def main():
    with trace("Telling a joke"):
        result = await Runner.run(agent, "Tell a joke about Autonomous AI Agents")
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())


import asyncio
from dotenv import load_dotenv
from google.adk.agents import Agent
#from google.adk.graphs.graph import Graph
load_dotenv()
from google.adk.agents import invocation_context 

#agent = Agent(name="test", model="gemini-2.5-flash")
#print(dir(agent))
root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.5-flash",
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    """,
)
async def main():
    # Use run_async (it is likely async so await it)
    #result = await root_agent.run_async(parent_context=None)
    #print("Agent output:", result)
    initial_context = invocation_context.InvocationContext()
    async for step in root_agent.run_async(parent_context=initial_context):
        print("Step output:", step)

if __name__ == "__main__":
    asyncio.run(main())    '''
#GEMINI MAIN
'''
from google.adk.agents import Agent
from dotenv import load_dotenv
#import os
#import google.generativeai as genai
load_dotenv()
#api_key = os.getenv("GOOGLE_API_KEY")
#print("google api key loaded :", api_key)
#genai.configure(api_key=api_key)
root_agent = Agent(
    name="basicagent101",
    model="gemini-3.0-flash",
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    """,
)
'''
#ENDS HERE
'''
from google.adk.agents import Agent
from autogen_ext.models.ollama import OllamaChatCompletionClient
# Connect to local Ollama server
model_client = OllamaChatCompletionClient(
    model="mistral",
    base_url="http://localhost:11434"
)
root_agent = Agent(
    name="basicagent101",
    model_client=model_client,
    description="Greeting agent",
    instruction="""
You are a helpful assistant that greets the user.
Ask for the user's name and greet them by name.
"""
)
'''
#
#MAIN OLLAMA MISTRAL

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# Tell LiteLLM to use Ollama
model = LiteLlm(
    model="ollama/qwen2.5:7b-instruct",
    #model="ollama/mistral",   # IMPORTANT FORMAT
    api_base="http://localhost:11434",
    custom_llm_provider="ollama"
    
)
root_agent = Agent(
    name="basicagent101",
    model=model,
    description="Greeting agent",
    instruction="""
You are a helpful assistant that greets the user.
Ask for the user's name and greet them by name.
""")
