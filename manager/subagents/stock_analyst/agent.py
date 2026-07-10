import yfinance as yf
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

'''def say(message: str) -> str:
    """Returns the final response to the user."""
    return message'''

def get_stock_price(ticker: str) -> dict:
    """Retrieves current stock price and saves to session state."""
    print(f"--- Tool: get_stock_price called for {ticker} ---")

    try:
        # Fetch stock data
        stock = yf.Ticker(ticker)
        current_price = stock.info.get("currentPrice")

        if current_price is None:
            return {
                "status": "error",
                "error_message": f"Could not fetch price for {ticker}",
            }

        # Get current timestamp
        #current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {
            "status": "success",
            "ticker": ticker,
            "price": current_price,
            #"timestamp": current_time,
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error fetching stock data: {str(e)}",
        }
model = LiteLlm(
    model="ollama/qwen2.5:7b-instruct",
    api_base="http://localhost:11434"
)
root_agent = Agent(
name="stock_analyst",
model=model,
description="An agent that can look up stock prices and track them over time.",
instruction="""
You are a helpful stock market assistant that helps users track their stocks of interest.

When asked about stock prices:
1. Use the get_stock_price tool to fetch the latest price for the requested stock(s)
2. Format the response to show each stock's current price and the time it was fetched
3. If a stock price couldn't be fetched, mention this in your response

Example response format:
"Here are the current prices for your stocks:
- GOOG: $175.34 
- TSLA: $156.78 
- META: $123.45"

After every tool call, your next action MUST be one of these:

1. Produce plain text to the user.
2. If the request is outside your responsibility, deligate the request to the manager agent.

Never call:
- respond_to_user say, or any other function that does not exist.

These functions do not exist.

There is no function for responding.
Simply output plain text directly.
Do NOT wrap your final answer in any function call.
""",
tools=[get_stock_price],
)