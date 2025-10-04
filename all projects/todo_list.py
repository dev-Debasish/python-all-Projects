import sys

# add each code chunks into the specific functions 

#   show menu
def menu():
    print()
    print("==== TO-DO LIST MENU ====")
    print("1. Add Task")
    print("2. View all Tasks")
    print("3. Mark Task as complete")
    print("4. Delete Task")
    # print("5. Save or. load tasks")
    print("5. Exit")
    # print()


# 1. add a task
list_of_tasks = []
def add_task():
    # while True:
    task_name = input("What is your task name? ")
    list_of_tasks.append(task_name)
    print("Task added Successfully!")
        # should_continue = input("Do you like to add more tasks(y/n): ").lower()
        # if should_continue == "n":
        #     break
    # print(list_of_tasks)


# 2. view all tasks
complete_task = []
def view_all_task():
    print("Your Tasks:")
    for index, task_name in enumerate(list_of_tasks):
        task_no = index + 1
        if task_no in complete_task:
            status = "[x]"
        else:
            status = "[ ]"
        print(f"{task_no}. {status} {task_name}")
            
    
# 3. mark as completed 

def mark_task():
    marked_task = int(input("Enter task number to mark as complete? "))
    complete_task.append(marked_task)
    print(f"✅ Task marked as complete: {list_of_tasks[marked_task-1]}")
    
    

# 4. delete the task
#!   not properly maintained??
def delete_task():
    deleted_task = int(input("Enter the task no. that you want to delete: "))
    for deleted_task, task_name in enumerate(list_of_tasks):
        list_of_tasks.pop(deleted_task - 1)
    print(f"🗑️ Task deleted: {list_of_tasks[deleted_task - 1]}")


    
def main():    
    while True:
        menu()
        choice = int(input("Enter the choice: "))
        print()
        match choice:
            case 1:
                add_task()
            case 2:
                view_all_task()
            case 3:
                mark_task()
            case 4:
                delete_task()
            case 5:
                print("Goodbye! 👋")
                sys.exit(0)
            case _:
                print("Invalid Input,Try Again!")
                
                
                
                
if __name__ == "__main__":
    main()