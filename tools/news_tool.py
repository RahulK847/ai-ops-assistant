import os
import requests 

def get_news(query, limit=3):
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        raise ValueError("NEWS_API_KEY environment variable not set")
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "apiKey": api_key,
        "pageSize": limit,
        "sortBy": "relevance"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    
    articles = []
    for item in data.get("articles", []):
        article_info = {
            "title": item["title"],
            "description": item["description"],
            "url": item["url"]
        }
        articles.append(article_info)
    return articles