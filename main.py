def main():
    
    while True:
        print("To Do List Workspace")
        print("-----------------------------")
        print("1. Add a new task")
        print("2. View all current tasks")
        print("3. Mark Task as COMPLETED")
        print("4. Delete Task")
        print("5. Save and Exit")


        choice = input("Choose an option (1-5):")

        if choice == "1":
            print("You picked the first option")
        elif choice == "2":
            print("You picked the option number 2")
        elif choice == "3":
            print("You picked the option number 3")
        elif choice == "4":
            print("You picked the option number 4")
        elif choice == "5":
            print("-----------------------------")
            print("Thank you for using our ToDoList, save and exit it is my Lord :D ")
            break
        else:
            raise Exception("There is no such choice!")








if __name__=="__main__":
    main()