"""
Project 04: Task Manager & Activity Logger
Concepts: Functions, File I/O (Read/Write), Exception Handling, List Manipulation
"""

import os

FILE_NAME = "tasks.txt"


def load_tasks():
    """Load tasks from the text file."""
    tasks = []
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                for line in file:
                    task = line.strip()
                    if task:
                        tasks.append(task)
        except Exception as e:
            print(f"[Error] Could not read file: {e}")
    return tasks


def save_tasks(tasks):
    """Save the current list of tasks to the text file."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(f"{task}\n")
    except Exception as e:
        print(f"[Error] Could not save file: {e}")


def show_tasks(tasks):
    """Display all current tasks."""
    if not tasks:
        print("\n[!] Your task list is empty. Time to relax or do some coding!")
        return

    print("\n--- Current Tasks ---")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print("---------------------")


def add_task(tasks):
    """Add a new task to the list."""
    new_task = input("\nEnter the new task: ").strip()
    if new_task:
        tasks.append(f"[ ] {new_task}")
        save_tasks(tasks)
        print(f"Task '{new_task}' added successfully!")
    else:
        print("[!] Task description cannot be empty.")


def complete_task(tasks):
    """Mark a task as completed."""
    show_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("\nEnter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            if tasks[task_num - 1].startswith("[X]"):
                print("[!] This task is already marked as completed.")
            else:
                tasks[task_num - 1] = tasks[task_num - 1].replace("[ ]", "[X]", 1)
                save_tasks(tasks)
                print(f"Great job! Task {task_num} completed.")
        else:
            print("[!] Invalid task number.")
    except ValueError:
        print("[!] Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n=== Personal Task Logger ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("\nExiting Task Logger. Keep coding, ثنا! Goodbye.")
            break
        else:
            print("[!] Invalid choice. Please pick between 1 and 4.")


if __name__ == "__main__":
    main()
