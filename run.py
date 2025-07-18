from llm.local_llm import parse_task
from agent import run_agent

def main():
    print("Sentinel Ready")

    while True:
        ui = input("\n> What would you like me to do? ")
        if ui.lower() in ["exit", "quit", "q"]:
            break
        try:
            task = parse_task(ui)
            print("\n--- Parsed Task ---", task.get("task_type"))
            result = run_agent(task)
            print("\nCompleted:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
