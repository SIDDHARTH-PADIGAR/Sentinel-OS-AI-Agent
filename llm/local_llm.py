def parse_task(prompt: str) -> dict:
    """
    Returns a dict with:
    - task_type: what to do (write, summarize, format, etc.)
    - payload: necessary data for execution
    """
    # MOCK parser — replace with LLM later
    if "write" in prompt.lower():
        return {
            "task_type": "write_document",
            "payload": {
                "title": "Generated_Doc.docx",
                "content": prompt.replace("Write", "").replace("write", "").strip()
            }
        }

    raise ValueError("Task not understood. Try rephrasing.")
from dotenv import load_dotenv
load_dotenv()

import os
import requests
import json

OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")
MODEL = "mistralai/mistral-7b-instruct"
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPEN_ROUTER_API_KEY}",
    "Content-Type": "application/json",
}

def call_llm(prompt: str) -> str:
    body = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    }
    resp = requests.post(BASE_URL, headers=HEADERS, json=body)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()

def parse_task(user_input: str) -> dict:
    # For now, only support write_document
    content = call_llm(user_input)
    return {
        "task_type": "write_document",
        "payload": {
            "title": None,  # can be None, handled downstream
            "content": content,
        },
    }
