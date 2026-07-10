import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_news(query: str) -> str:
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": query,
        "apiKey": NEWS_API_KEY,
        "pageSize": 3,
        "sortBy": "publishedAt"
    }

    response = requests.get(url, params=params)
    data = response.json()

    articles = data.get("articles", [])

    if not articles:
        return "No news found."

    '''summaries = []

    for article in articles:
        summaries.append(
            f"{article['title']} - {article['source']['name']}"
        )

    return "\n".join(summaries)'''
    summaries = []

    for article in articles:
        title = article.get("title", "No Title")
        source = article.get("source", {}).get("name", "Unknown Source")

        summaries.append(f"{title} - {source}")

    if not summaries:
        return "No news articles found for this query."

    soli="\n".join(summaries)
    return{
        "extracted news": soli
    }
