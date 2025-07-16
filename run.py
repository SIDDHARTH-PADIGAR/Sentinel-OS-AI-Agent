from agent import process_task

print("Sentinel Ready.")
while True:
    user_input = input("What would you like me to do? > ")
    process_task(user_input)
