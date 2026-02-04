# AI Ops Assistant

A Python-based **multi-agent GenAI Operations Assistant** that accepts natural language tasks, plans actions using an LLM, executes real API calls, and verifies results before returning a final response.

---

## Overview

This project demonstrates an **agent-based AI system** built using a **Planner–Executor–Verifier** architecture.

### Agents

- **Planner Agent**
  - Uses an LLM to convert user input into a **structured JSON plan**
  - Decides which tools (APIs) to use and with what parameters

- **Executor Agent**
  - Executes the plan by calling **real third-party APIs**
  - Does not use any LLM logic

- **Verifier Agent**
  - Uses an LLM to verify completeness and consistency of results
  - Formats the final response into a clean, human-readable output
  - Does not call APIs or invent data

---

## Features

- Natural language task processing
- **Multi-agent architecture (Planner, Executor, Verifier)**
- Structured JSON planning using LLMs
- Integration with **real APIs**
- End-to-end execution pipeline
- Runs locally with a single command

---

## Integrated APIs

This project integrates the following **real third-party APIs**:

- **GitHub API** – Search and retrieve top repositories
- **OpenWeatherMap API** – Fetch current weather by city
- **NewsAPI** – Retrieve latest news articles by topic

---

## Setup Instructions (Local)

### 1. Clone Repository
```bash
git clone https://github.com/RahulK847/ai-ops-assistant.git
cd ai-ops-assistant
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file in the project root using the template provided in `.env.example`:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENWEATHER_API_KEY=your_openweather_api_key_here
NEWS_API_KEY=your_newsapi_api_key_here
```



### 4. Run the Project
```bash
python main.py
```

---

## Example Prompts

1. Find top Python GitHub repositories  
2. Show weather in Delhi  
3. Get latest AI news  
4. Find Python GitHub repos, weather in Mumbai, and AI news  
5. Search machine learning repos and show weather in Bangalore  

---

## Example Planner Output (JSON)

```json
{
  "steps": [
    { "tool": "github", "query": "Python" },
    { "tool": "weather", "city": "Delhi" },
    { "tool": "news", "query": "AI" }
  ]
}
```

---

## Known Limitations / Trade-offs

- Command-line interface only (no UI)
- Sequential execution of API calls
- Basic error handling
- Subject to third-party API rate limits
- No parallel tool execution

---

## License

MIT
