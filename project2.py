print("Welcome to your To-Do list app." )

task = []

def save_tasks(all_tasks):
    with open("tasks.txt", "w") as task_file:
        for task in all_tasks:
            task_file.write(f"{task['task']}||{task['status']}\n")
        
def load_tasks(filename):
    try: 
        tasks_list =[]
        with open(filename, "r") as task_file:
            all_tasks = task_file.readlines()
        for task in all_tasks:
                task_parts = task.strip().split("||")

                task_data = {"task": task_parts[0], "status": task_parts[1]}
                tasks_list.append(task_data)
        return tasks_list
    
    except FileNotFoundError:
        print("The required file is not found in this directory")

def add_task():
    try:
        add_task = input("\nInput your task: ").capitalize()

        with open("tasks.txt", "a") as task_file:
                task_file.write(f"{add_task}||Pending\n")

        print(f"\nYour task '{add_task}' has successfully been added.")

    except FileNotFoundError:
        print("The required file is not found in this directory")

def view_tasks(filename):
    all_tasks = load_tasks(filename)
    print("-"*60)
    print(f"|{'ID':<7}|{'Task':<34}|{'Status':<15}|")
    print("-"*60)
    for index, task in enumerate(all_tasks, start=1):
        print(f"|{index:<7}|{task['task']:<34}|{task['status']:<15}|")
    print("-"*60)

def completed(filename):
    view_tasks(filename)
    all_tasks = load_tasks(filename)
    try:
        task_num = int(input("\nEnter the number of the completed task? "))

        task_index = task_num - 1 

        if 0 <= task_index < len(all_tasks):
            old_task = all_tasks[task_index]["task"]
            all_tasks[task_index]["status"] = "Completed"

            save_tasks(all_tasks)
            print(f"\nThe task '{old_task}' has been completed.")
           
        else: 
            print("Please enter a valid number.")

    except ValueError:
        print("\nThe number inputted is not in the list.")

def delete_task(filename):
    view_tasks(filename)
    try:
        all_tasks = load_tasks(filename)
        task_num = int(input("\nWhat is the number of the task you want to delete? "))
    
        task_index = task_num - 1

        if 0 <= task_index < len(all_tasks):
            removed_task = all_tasks.pop(task_index)
            print(f"\n'{removed_task['task']}' has successfully being removed from your task list.")
  
            save_tasks(all_tasks)
        else:
            print("The number entered is not in the list.")
    except ValueError:
        print("Please input a valid number")
        

while True:
    ops = input("\nEnter any of the following options('add', 'view', 'completed', 'delete', 'exit': ").strip().lower()

    if ops == "add":
        add_task()
    elif ops =="view":
        view_tasks("tasks.txt")
    elif ops == "completed":
        completed("tasks.txt")
    elif ops == "delete":
        delete_task("tasks.txt")
    elif ops == "exit":
        print("You're done with your task updates. See you later!")
        break
    else: 
        print("Please make sure your input is among the operations provided.")
    