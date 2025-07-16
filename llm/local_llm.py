import subprocess
import json
import re

def extract_json(text):
    try:
        matches = re.findall(r"\{.*?\}", text, re.DOTALL)
        longest = max(matches, key=len)
        return json.loads(longest)
    except Exception as e:
        print("Failed to extract valid JSON from LLM output:")
        print(text)
        raise e

def parse_task(prompt: str) -> dict:
    system_prompt = """
You are a strict JSON generator.

Given a user command, output only a valid JSON object with the following keys:

- task (string): e.g., "write_letter"
- tone (string): e.g., "formal"
- duration (string): e.g., "2 days"
- output_format (string): e.g., "pdf"
- destination (string): e.g., "desktop"

🚫 Do NOT add extra commentary or explanation.
🚫 Do NOT mention constraints.
✅ Just output JSON. Nothing else.
"""

    command = f"{system_prompt}\n\nUser: {prompt}"

    try:
        result = subprocess.run(
            ["ollama", "run", "phi3"],
            input=command.encode(),
            capture_output=True,
            timeout=90
        )

        output = result.stdout.decode().strip()

        with open("debug_llm_output.txt", "w", encoding="utf-8") as f:
            f.write(output)

        return extract_json(output)

    except Exception as e:
        print("LLM JSON extraction failed:")
        print(output)
        raise e




def get_letter_content(prompt: str) -> str:
    """
    Sends a plain prompt to the local LLM (phi3 via Ollama) and returns the generated text.
    Used to generate the actual letter content after task parsing.
    """
    result = subprocess.run(
        ["ollama", "run", "phi3"],
        input=prompt.encode(),
        capture_output=True,
        timeout=90
    )

    return result.stdout.decode().strip()
