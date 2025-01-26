from todo_list_class import ToDoList

def main():
    example = ToDoList()
    example.load_json()


    while True:
        print("\nTo Do List Workspace")
        print("-----------------------------")
        print("1. Add a new task")
        print("2. View all current tasks")
        print("3. Mark Task as COMPLETED")
        print("4. Delete Task")
        print("5. Save and Exit")


        choice = input("\nChoose an option (1-5): ")

        if choice == "1":
            example.add_task()
        elif choice == "2":
            example.view_list()
        elif choice == "3":
            example.mark_completed()
            print("\n> Your task is now completed.")
        elif choice == "4":
            example.choose_remove()
            print("\n Ok, we'll delete this task for you...")
        elif choice == "5":
            print("\n> Saving everything...")
            print("-----------------------------")
            print("\n> Thank you for using our ToDoList, save and exit it is my Lord :D ")
            break
        else:
            raise Exception("\n> There is no such choice!")








if __name__=="__main__":
    main()