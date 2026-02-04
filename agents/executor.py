from tools.github_tool import search_github_repos
from tools.weather_tool import get_weather
from tools.news_tool import get_news

def execute_task(plan):
    """
    Executes the plan produced by the Planner Agent.
    Calls real APIs via tool modules and return results raw resultis.
    """
    results = {}
    
    if not plan or "steps" not in plan:
        raise ValueError("Invalid or empty plan")

    
    for step in plan["steps"]:
        tool = step.get("tool")

        if tool == "github":
            query = step.get("query")
            if not query:
                raise ValueError("Missing 'query' for GitHub tool.")
            results["github"] = search_github_repos(query)

        elif tool == "weather":
            city = step.get("city")
            if not city:
                raise ValueError("Missing 'city' for Weather tool.")   
            results["weather"] = get_weather(city)

        elif tool == "news":
            query = step.get("query")
            if not query:
                raise ValueError("Missing 'query' for News tool.")
            results["news"] = get_news(query)

        else:
            raise ValueError(f"Unknown tool requested: {tool}")
        
    return results