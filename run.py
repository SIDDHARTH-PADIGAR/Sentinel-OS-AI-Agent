from llm.local_llm import parse_task
from task.ms_word import create_letter

def main():
    print("Sentinel Ready")

    while True:
        user_input = input("What would you like me to do? > ")
        if user_input.lower() in ["exit", "quit", "q"]:
            break

        try:
            task = parse_task(user_input)
            create_letter(task)
        except Exception as e:
            print("Error processing task:", e)

if __name__ == "__main__":
    main()
