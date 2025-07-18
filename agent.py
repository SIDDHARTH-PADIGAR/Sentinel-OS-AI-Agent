from task.ms_word import write_document

def run_agent(task: dict) -> str:
    task_type = task.get("task_type")
    payload = task.get("payload", {})

    if task_type == "write_document":
        return write_document(payload)

    raise ValueError(f"Unsupported task type: {task_type}")
