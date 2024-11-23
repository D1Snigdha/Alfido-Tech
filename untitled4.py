# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V7NC-pV3SNiM3RD5gKO3SuSkyVhzsZsR
"""

tasks = []

def display_tasks():
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks):
            status = "✓" if task['completed'] else "✗"
            print(f"{i + 1}. {task['name']} [{status}]")

def add_task():
    task_name = input("Enter the task: ")
    tasks.append({"name": task_name, "completed": False})
    print("Task added.")

def delete_task():
    display_tasks()
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        tasks.pop(task_num - 1)
        print("Task deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def mark_task_completed():
    display_tasks()
    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        tasks[task_num - 1]['completed'] = True
        print("Task marked as completed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

while True:
    print("\nTo-Do List Application")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Mark a task as completed")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        display_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        mark_task_completed()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")