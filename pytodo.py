import json
from datetime import datetime
from pathlib import Path

TASK_FILE = Path("tasks.json")

def load_tasks():
    if TASK_FILE.exists():
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def display_menu():
    print("\n========= TO-DO LIST MENU =========")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete a Task")
    print("5. Exit")

def add_task(tasks):
    desc = input("Enter task description: ").strip()
    if not desc:
        print("⚠ Task cannot be empty.")
        return

    date_str = input("Enter due date (YYYY-MM-DD) [optional]: ").strip()
    due_date = None
    if date_str:
        try:
            due_date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("⚠ Invalid date format. Skipping due date.")

    tasks.append({
        "description": desc,
        "due": due_date,
        "completed": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    print("✔ Task added.")

def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
        return
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        due = f"(Due: {task['due']})" if task.get("due") else ""
        print(f"{i}. {status} {task['description']} {due} [Added: {task['created']}]")

def complete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number to mark as complete: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["completed"] = True
                print("✔ Task marked as complete.")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("⚠ Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"🗑 Removed: {removed['description']}")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("⚠ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Choose an option (1–5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
