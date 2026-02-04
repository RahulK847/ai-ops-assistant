import json
from llm.llm_client import call_llm

SYSTEM_PROMPT = """
You are a planner agent and your job is to convert user requests into a structured plan in JSON format.

Available tools:
1. github -> requires: {"query": "<search terms>"}
2. weather -> requires: {"city": "<city name>"}
3. news -> requires: {"query": "<news topic>"}

Rules:
- Always respond in valid JSON format.
- Do not include any explanations or additional text outside the JSON structure.
- Do not include markdown.
- Do not invent tools or parameters not listed above

JSON Structure:
{
    "steps": [
        { "tool": <tool_name>, "...": "..."} 
    ]
}
"""
def create_plan(user_request):
    response = call_llm(SYSTEM_PROMPT, user_request)
    try:
        plan = json.loads(response)
        return plan
    except json.JSONDecodeError:
        raise ValueError("Failed to parse LLM response as JSON")
