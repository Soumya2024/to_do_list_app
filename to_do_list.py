# To-Do List Application

# Define an empty list to store tasks
tasks = []

# Function to add a new task
def add_task(title, description):
    task = {
        'title': title,
        'description': description,
        'done': False
    }
    tasks.append(task)
    print("Task added successfully!")

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Done" if task['done'] else "Pending"
            print(f"{i}. {task['title']} - {task['description']} - Status: {status}")

# Function to mark a task as done
def mark_task_done(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")

# Main program loop
while True:
    print("\nTo-Do List Menu:")
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Mark a task as done")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        add_task(title, description)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        list_tasks()
        task_number = int(input("Enter the task number to mark as done: "))
        mark_task_done(task_number)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
