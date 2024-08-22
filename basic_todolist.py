def show_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

tasks = []
while True:
    print("\nTo-Do List:")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Quit")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
    elif choice == '2':
        show_tasks(tasks)
    elif choice == '3':
        show_tasks(tasks)
        try:
            task_idx = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_idx < len(tasks):
                tasks.pop(task_idx)
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a valid number")
    elif choice == '4':
        break
    else:
        print("Invalid input")
