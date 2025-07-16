from llm.local_llm import parse_task
from task.ms_word import create_letter
import logging

def process_task(prompt: str):
    logging.info("Parsing task with LLM...")
    task = parse_task(prompt)
    
    if task["task"] == "write_letter":
        create_letter(task)
    else:
        print("Sorry, I don't know how to handle that task yet.")