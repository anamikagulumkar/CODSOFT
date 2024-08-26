import os

TODO_FILE = 'todos.txt'

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        return [line.strip() for line in file]

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def list_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: {task}")

def remove_task(tasks, index):
    try:
        task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed task: {task}")
    except IndexError:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List:")
        list_tasks(tasks)
        print("\nCommands:")
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Exit")

        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            task = input("Enter the task: ").strip()
            add_task(tasks, task)
        elif choice == '2':
            index = int(input("Enter task number to remove: ").strip())
            remove_task(tasks, index)
        elif choice == '3':
            list_tasks(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
