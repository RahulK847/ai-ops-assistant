import json 
from llm.llm_client import call_llm

SYSTEM_PROMPT ="""
You are a Verifier Agent.

Your responsibilities:
- Check if the executor output is complete and consistent
- Fix minor formatting issues
- Produce a clean, human-readable final response

Rules:
- Do not invent new data
- Do not call APIs
- Use only the provided data
"""

def verify_and_format(raw_result):
    """
    Uses LLM to verify and format the executor output.
    Returns a final user-facing response.
    """
    response = call_llm(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=json.dumps(raw_result, indent=2)
    )
    return response