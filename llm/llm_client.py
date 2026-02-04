import os 
from openai import OpenAi as ai 

client = ai(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature = 0
    )
    return response.choices[0].message.content