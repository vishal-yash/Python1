from datetime import datetime
from model.task_model import tasks as default_tasks
from dev_service.devtask_json import load_tasks, save_tasks

tasks = load_tasks() or default_tasks


def create_task():

    task_id = int(input("Enter task id: "))
    emp_name = input("Enter employee name: ")
    emp_dept = input("Enter employee department: ")
    task = input("Enter task: ")
    task_status = input("Enter task status (To do, In progress, Done): ")
    priority = input("Enter priority (High, medium, Low): ")
    created_date = datetime.now().strftime("%Y-%m-%d")
    dedline = input("Enter deadline (YYYY-MM-DD): ")

    task_info = {
        "task_id": task_id,
        "emp_name": emp_name,
        "emp_dept": emp_dept,
        "task": task,
        "task_status": task_status,
        "priority": priority,
        "created_date": created_date,
        "dedline": dedline,
    }
    tasks.append(task_info)
    save_tasks(tasks)
    print("Task added successfully!")


def display_tasks(task_list):
    if not task_list:
        print("No matching tasks found.")
        return

    print("\nStored Tasks:")
    for task in task_list:
        print("------------------------------")
        print(f"Task ID: {task['task_id']}")
        print(f"Employee: {task['emp_name']} ({task['emp_dept']})")
        print(f"Task: {task['task']}")
        print(f"Status: {task['task_status']}")
        print(f"Priority: {task['priority']}")
        print(f"Created: {task['created_date']}")
        print(f"Deadline: {task['dedline']}")
    print("------------------------------")


def view_tasks_menu():
    from constants.dev_const import (
        VIEW_MENU_HEADER,
        VIEW_MENU_OPTIONS,
        VIEW_MENU_PROMPT,
        INVALID_VIEW_OPTION_MESSAGE,
    )

    while True:
        print(VIEW_MENU_HEADER)
        for option in VIEW_MENU_OPTIONS:
            print(option)

        choice = input(VIEW_MENU_PROMPT)
        saved_tasks = load_tasks() or []

        if choice == "1":
            display_tasks(saved_tasks)
        elif choice == "2":
            display_tasks(
                [
                    task
                    for task in saved_tasks
                    if task["task_status"].strip().lower() == "to do"
                ]
            )
        elif choice == "3":
            display_tasks(
                [
                    task
                    for task in saved_tasks
                    if task["task_status"].strip().lower() == "in progress"
                ]
            )
        elif choice == "4":
            display_tasks(
                [
                    task
                    for task in saved_tasks
                    if task["task_status"].strip().lower() == "done"
                ]
            )
        elif choice == "5":
            display_tasks(
                [task for task in saved_tasks if task["priority"].strip().lower() == "high"]
            )
        elif choice == "6":
            display_tasks(
                [task for task in saved_tasks if task["priority"].strip().lower() == "medium"]
            )
        elif choice == "7":
            display_tasks(
                [task for task in saved_tasks if task["priority"].strip().lower() == "low"]
            )
        elif choice == "8":
            break
        else:
            print(INVALID_VIEW_OPTION_MESSAGE)


def update_task():
    saved_tasks = load_tasks() or []
    if not saved_tasks:
        print("No tasks available to update.")
        return

    try:
        task_id = int(input("Enter the task id to update: "))
    except ValueError:
        print("Invalid task id. Please enter a number.")
        return

    task_to_update = None
    for task in saved_tasks:
        if task["task_id"] == task_id:
            task_to_update = task
            break

    if task_to_update is None:
        print(f"Task with id {task_id} not found.")
        return

    print("Leave a field blank to keep the current value.")
    new_emp_name = input(f"Employee name [{task_to_update['emp_name']}]: ")
    new_emp_dept = input(f"Employee department [{task_to_update['emp_dept']}]: ")
    new_task = input(f"Task [{task_to_update['task']}]: ")
    new_task_status = input(f"Task status [{task_to_update['task_status']}]: ")
    new_priority = input(f"Priority [{task_to_update['priority']}]: ")
    new_deadline = input(f"Deadline [{task_to_update['dedline']}]: ")

    if new_emp_name:
        task_to_update["emp_name"] = new_emp_name
    if new_emp_dept:
        task_to_update["emp_dept"] = new_emp_dept
    if new_task:
        task_to_update["task"] = new_task
    if new_task_status:
        task_to_update["task_status"] = new_task_status
    if new_priority:
        task_to_update["priority"] = new_priority
    if new_deadline:
        task_to_update["dedline"] = new_deadline

    save_tasks(saved_tasks)
    print("Task updated successfully!")


def delete_task():
    saved_tasks = load_tasks() or []
    if not saved_tasks:
        print("No tasks available to delete.")
        return

    try:
        task_id = int(input("Enter the task id to delete: "))
    except ValueError:
        print("Invalid task id. Please enter a number.")
        return

    for index, task in enumerate(saved_tasks):
        if task["task_id"] == task_id:
            deleted_task = saved_tasks.pop(index)
            save_tasks(saved_tasks)
            print(f"Task {deleted_task['task_id']} deleted successfully.")
            return

    print(f"Task with id {task_id} not found.")


def view_tasks():
    saved_tasks = load_tasks() or []
    display_tasks(saved_tasks)
