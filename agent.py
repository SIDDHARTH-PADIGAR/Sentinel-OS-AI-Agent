from llm.openrouter_llm import call_openrouter
from task.ms_word import write_document

def run_agent(task_input: str) -> str:
    """
    End-to-end agent that takes unstructured user input,
    uses LLM to parse it, and creates the document.
    """
    prompt = f"""
You are a task parser. Given the user's request, extract the following fields:
- title
- bullet_points
- conclusion

Return a JSON like:
{{
    "title": "...",
    "content": {{
        "bullet_points": ["...", "..."],
        "conclusion": "..."
    }}
}}

USER REQUEST:
{task_input}
    """

    llm_response = call_openrouter(prompt)

    try:
        # If you want to be strict, replace with `json.loads()` and sanitize input
        structured = eval(llm_response.strip())  

        title = structured["title"]
        bullet_points = structured["content"]["bullet_points"]
        conclusion = structured["content"]["conclusion"]

        # Format into one string
        content = "\n".join(f"- {point}" for point in bullet_points)
        content += f"\n\nConclusion:\n{conclusion}"

        return write_document({
            "title": title,
            "content": content
        })

    except Exception as e:
        print("Failed to parse LLM response:", e)
        print("Raw LLM output:\n", llm_response)
        return "Document generation failed."
