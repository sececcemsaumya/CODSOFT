def print_tasks():
    task_list.sort(key=lambda x: -int(x[2]))
    for row in task_list:
        print(f"{row}")

task_list = []

while True:
    print("""TODO List Management System
    1: Add
    2: View
    3: Remove
    4: Edit
    5: Exit""")
    w = input()
    if w == '1':
        add = input("What do you want to add: ")
        task_list.append((len(task_list) + 1, add, "0"))
        print("Task added!")
    elif w == '2':
        print_tasks()
    elif w == '3':
        task_number = int(input("Enter the task number to remove: "))
        for i, task in enumerate(task_list):
            if task[0] == task_number:
                task_list.pop(i)
                break
        else:
            print("Invalid task number.")
    elif w == '4':
        task_number = int(input("Enter the task number to edit: "))
        for i, task in enumerate(task_list):
            if task[0] == task_number:
                new_task = input("Enter the new task: ")
                task_list[i] = (task_number, new_task, task[2])
                break
        else:
            print("Invalid task number.")
    elif w == '5':
        print("Exiting the To-Do List.")
        break
    else:
        print("Invalid choice. Please try again.")