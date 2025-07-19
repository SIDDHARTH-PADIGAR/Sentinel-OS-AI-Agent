import requests
import os

def call_openrouter(prompt: str) -> str:
    api_key = os.getenv("OPEN_ROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPEN_ROUTER_API_KEY not found in environment variables")

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mixtral-8x7b",  # or whatever model you're using
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    # Force print response if error
    if response.status_code != 200:
        print("Response text:", response.text)
        response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
