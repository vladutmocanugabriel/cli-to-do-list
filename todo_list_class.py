import json
from tabulate import tabulate # type: ignore
from task_class import Task

class ToDoList:
    def __init__(self):
        self.__tasks = []
        
    def load_json(self):
        with open('./tasks.json') as json_file:
            data = json.load(json_file)
        self.__tasks = data
    
    def __get_current_tasks(self):
        if len(self.__tasks) == 0:
            print("\nThere is no task in your ToDo List")
        self.pretty_table(self.__tasks)

    def __upload_new_task_json(self, tasks):
        with open("./tasks.json", "w") as f:
            json.dump(tasks, f, indent=4)

    def save_and_exit(self):
        self.__upload_new_task_json(self.__tasks)

    def add_task(self):
        title = input("> Enter the title of the task:")
        description = input("> Enter the description of the task:")
        tag = input("> Enter the #TAG you want to assign to this task (e.g. Work, Personal, Fun, Training):")
        due_date = input("> Enter the due date for this task in dd/mm/year (e.g. 26/01/2025):")
        priority = input("> Choose a priority for this task (e.g. HIGH, MEDIUM, LOW):")

        if not title:
            print("Title cannot be empty. Task not created.")
            return
        if priority not in ("HIGH", "MEDIUM", "LOW"):
            print("Invalid priority. Please enter HIGH, MEDIUM or LOW. Task not created.")
            return

        self.load_json()
        new_task = Task(title, description, tag, due_date, priority)
        self.__tasks.append(new_task.to_dict())
        
        for task in self.__tasks:
            task["id"] = self.__tasks.index(task) + 1

        self.__upload_new_task_json(self.__tasks)
        print("\n> Adding your new task...")

    def choose_remove(self):
        remove_method = input("Would you prefer to remove by title or by ID?")

        if remove_method == "title":
            self.__remove_task_by_title()
        elif remove_method == "id":
            self.__remove_task_by_id()


    def __remove_task_by_title(self):
        print("\n Here you have all the available tasks to remove:")
        self.__get_current_tasks()
        print("\n -----------------------------")
        task_to_remove = input("> Write the title of the task you want to remove:")
        for task in self.__tasks:
            if task_to_remove in task["title"]:
                self.__tasks.remove(task)
        self.__upload_new_task_json(self.__tasks)

    def __remove_task_by_id(self):
        print("\n Here you have all the available tasks to remove:")
        self.__get_current_tasks()
        print("\n -----------------------------")
        task_id_to_remove = int(input("> Write the id of the task you want to remove:"))
        for task in self.__tasks:
            print(f"This is the task you want to be removed: ID-{task_id_to_remove} and has type {type(task_id_to_remove)}")
            if task_id_to_remove == task["id"]:
                self.__tasks.remove(task)
        self.__upload_new_task_json(self.__tasks)
            

    def view_list(self):
        return self.__get_current_tasks()
    
    def mark_completed(self):
        print("\n Here you have all the available tasks to mark as completed:")
        not_completed = []
        for task in self.__tasks:
            if task["completed"] == False:
                not_completed.append(task)
        self.pretty_table(not_completed)

        print("\n -----------------------------")

        task_to_complete = input("> Write the title of the task you want to set as completed:")
        for task in self.__tasks:
            if task_to_complete in task["title"]:
                task["completed"] = True
        self.__upload_new_task_json(self.__tasks)

    def pretty_table(self, tasks):
        formatted = tabulate(tasks, headers="keys", tablefmt="grid")
        print(formatted)
