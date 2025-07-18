import requests
from config import OPENROUTER_API_KEY

def run_openrouter_llm(prompt: str, model="mistralai/mistral-7b-instruct") -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    json = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=json, headers=headers)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']
