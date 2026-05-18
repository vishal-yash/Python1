import json

#open the json file and load the tasks.
TASKS_FILE = 'model/devtrack.json'
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"{TASKS_FILE} not found. Starting with an empty task list.")
        return []
    except json.JSONDecodeError:
        print(f"{TASKS_FILE} is empty or invalid. Starting with an empty task list.")
        return []
    
#to save the tasks to the json file.
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)  