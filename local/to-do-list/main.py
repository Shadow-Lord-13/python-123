import json

def display_menu():
    print(
    "\nOptions available :\n"
    "1 -> Add task\n"
    "2 -> Edit task\n"
    "3 -> Delete task\n"
    "4 -> View task\n"
    "5 -> Exit App\n"
)

def display_task_options():
    print(
    "\nOptions available :\n"
    "1 -> Update task\n"
    "2 -> Update date\n"
    "3 -> Update priority\n"
    "4 -> Exit update menu\n"
)

def add_task(tasks):
    task = input("\nPlease enter the task description: ")
    due_date = input("Please enter the due date: ")
    priority = input("Please enter the task priority (Low/Medium/High): ")

    new_task = {
        "task": task,
        "priority": priority,
        "due_date": due_date
    }
    tasks.append(new_task)

    print("Task added successfully")

def view_task(tasks):
    if not tasks:
        print("No task available")
    else:
        print(f"\n{'No.':<5} {'Task':<30} {'Priority':<10} {'Due Date':<10}")
        print("-" * 57)
        for i, task in enumerate(tasks, start=1):
            task_des = task.get("task", "N/A")
            priority = task.get("priority", "N/A")
            due_date = task.get("due_date", "N/A")
            print(f"{i:<5} {task_des:<30} {priority:<10} {due_date:<10}")

def update_task(tasks):
    view_task(tasks)
    task_no = int(input("\nPlease enter the task to be updated: "))
    if tasks:
        try:
            if 1 <= task_no <= len(tasks):
                while True:
                    display_task_options()
                    user_choice = int(input("Please select the option to be updated: "))

                    if user_choice==1:
                        updated_task = input("Enter the update discription for the task: ")
                        tasks[task_no-1]['task'] = updated_task
                        print("Task description updated successfully")
                    elif user_choice==2:
                        updated_date = input("Enter the update date for the task: ")
                        tasks[task_no-1]['date'] = updated_date
                        print("Task date updated successfully")
                    elif user_choice==3:
                        updated_priority = input("Enter the update priority for the task: ")
                        tasks[task_no-1]['priority'] = updated_priority
                        print("Task priority updated successfully")
                    elif user_choice==4:
                        print("Exiting Update Menu.")
                        break
                    else:
                        print("Invalid choice, Please try again!")
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
            user_input = int(input("Please select from the avaialble options: "))

            if user_input == 1:
                add_task(tasks)
            elif user_input == 2:
                update_task(tasks)
            elif user_input == 3:
                delete_task(tasks)
            elif user_input == 4:
                view_task(tasks)
            elif user_input == 5:
                print("Thanks for using our App!!!")
                break
            else:
                print("Error: Please enter valid input!")
    except Exception as e:
        print(f" Error: {e}")


if __name__ == "__main__":
    main()
