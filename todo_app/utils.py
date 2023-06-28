import os
import json
from dotenv import load_dotenv
from .models import Task

load_dotenv()

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
DATA_FILE = os.path.join(DATA_DIR, "tasks.txt")


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
DATA_FILE = os.path.join(DATA_DIR, "tasks.json")

def save_tasks(tasks):
    task_list = []
    for task in tasks:
        task_data = {
            "description": task.description,
            "completed": task.completed
        }
        task_list.append(task_data)

    with open(DATA_FILE, 'w') as f:
        json.dump(task_list, f, indent=2)

def load_tasks():
    tasks = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            task_list = json.load(f)
            for task_data in task_list:
                description = task_data.get("description")
                completed = task_data.get("completed")
                if description is not None and completed is not None:
                    task = Task(description, completed=bool(completed))
                    tasks.append(task)
                else:
                    print(f"Ignoring invalid task entry: {task_data}")
    return tasks