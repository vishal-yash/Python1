from constants.dev_const import (
    ADD_TASK_OPTION,
    VIEW_TASKS_OPTION,
    UPDATE_TASK_OPTION,
    DELETE_TASK_OPTION,
    EXIT_OPTION,
    MENU_HEADER,
    MENU_OPTIONS,
    MENU_PROMPT,
    EXIT_MESSAGE,
    INVALID_OPTION_MESSAGE,
)
from controllers.task_controller import (
    create_task,
    view_tasks_menu,
    update_task,
    delete_task,
)

def run_task_ui():
    while True:
        print(MENU_HEADER)
        for option in MENU_OPTIONS:
            print(option)

        user_choice = input(MENU_PROMPT)

        if user_choice == ADD_TASK_OPTION:
            create_task()
        elif user_choice == VIEW_TASKS_OPTION:
            view_tasks_menu()
        elif user_choice == UPDATE_TASK_OPTION:
            update_task()
        elif user_choice == DELETE_TASK_OPTION:
            delete_task()
        elif user_choice == EXIT_OPTION:
            print(EXIT_MESSAGE)
            break
        else:
            print(INVALID_OPTION_MESSAGE)
