import requests

def search_github_repos(query, limit=3):
    url  = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    results = []
    for item in data.get("items", [])[:limit]:
        repo_info = {
            "name": item["full_name"],
            "stars": item["stargazers_count"],
            "description": item["description"]
        }
        results.append(repo_info)
    
    return results