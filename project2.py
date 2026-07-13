print("Welcome to your To-Do list app." )

def add_task(filename):
    try:
        add_task = input("\nInput a task: ")
        with open(filename, "a") as task_file:
            text = task_file.write(add_task + "\n")
        print(f"\nYour task '{add_task}' has successfully been added.")
    
        

    except FileNotFoundError:
        print("The required file is not found in this directory")

def view_tasks(filename):
    try: 
        with open(filename, "r") as task_file:
            tasks = task_file.read()
            print(f"\n{tasks}")
    
    except FileNotFoundError:
        print("The required file is not found in this directory")

def completed(filename):
    try:
        task_num = int(input("\nWhat is the number of the task completed? "))

        with open(filename, "r") as task_file:
            all_tasks = task_file.readlines() 
            task_index = task_num - 1 

            if task_index < len(all_tasks):
                old_task = all_tasks[task_index].strip()

                new_task = f"{old_task} - Completed\n"
                all_tasks[task_index] = new_task

                print(f"\nThe task '{old_task}' has been completed.")

                with open(filename, "w") as task_file:
                    task_file.writelines(all_tasks)
            else: 
                print("Please enter a valid number.")

    except ValueError:
        print("\nThe number inputted is not in the list.")

def delete_task(filename):
    try:
        task_num = int(input("\nWhat is the number of the task you want to delete? "))
    
        task_index = task_num - 1

        with open(filename, "r") as file:
            all_tasks = file.readlines()

        if task_index < len(all_tasks):
            removed_task = all_tasks.pop(task_index)
            print(f"\n'{removed_task.strip()}' has successfully being removed from your task list.")
            
            with open(filename, 'w') as file:
                file.writelines(all_tasks)
        else:
            print("The number entered is not in the list.")
    except ValueError:
        print("Please input a valid number")
        

while True:
    ops = input("\nEnter any of the following options('add', 'view', 'completed', 'delete', 'exit': ").strip().lower()

    if ops == "add":
        add_task("tasks.txt")
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
    