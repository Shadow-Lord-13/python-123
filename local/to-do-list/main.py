

def display_menu():
    print(
    "\nOptions available :\n"
    "1 -> Add task\n"
    "2 -> Edit task\n"
    "3 -> Delete task\n"
    "4 -> View task\n"
    "5 -> Exit App\n"
)

def add_task(tasks):
    task = input("Please enter the task description: ")
    tasks.append({"task": task})
    print("Task added")

def view_task(tasks):
    if not tasks:
        print("No task available")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']}")

def update_task(tasks):
    view_task(tasks)
    task_no = int(input("Please enter the task to be updated: "))
    if tasks:
        try:
            if 1 <= task_no <= len(tasks):
                updated_task = input("Enter the update discription for the task: ")
                tasks[task_no-1]['task'] = updated_task
                print("Task updated successfully")
            else:
                print("Invaild task number!!!")
        except Exception as e:
            print(f"Error: {e}")

def delete_task(tasks):
    view_task(tasks)
    task_no = int(input("Enter task to be deleted: "))
    if tasks:
        try:
            if 1<= task_no <= len(tasks):
                removed_task = tasks.pop(task_no-1)
                print(f"Removed task: {removed_task}")
        except Exception as e:
            print(f"Error: {e}")

def main():
    
    tasks = []
    print("Welcome to the To-Do List App!!!")
    try:
        while True:
            display_menu() 
            user_input = input("")

            if user_input=='1':
                add_task(tasks)
            elif user_input=='2':
                update_task(tasks)
            elif user_input=='3':
                delete_task(tasks)
            elif user_input=='4':
                view_task(tasks)
            elif user_input=='5':
                print("Thanks for using our App!!!")
                break
            else:
                print("Error: Please enter valid input!")
    except Exception as e:
        print(f" Error: {e}")


if __name__ == "__main__":
    main()
