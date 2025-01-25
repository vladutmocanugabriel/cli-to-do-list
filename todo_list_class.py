import json
from task_class import Task

class ToDoList:
    def __init__(self):
        self.__tasks = []
        
    def load_json(self):
        with open('./tasks.json') as json_file:
            data = json.load(json_file)
        self.__tasks = data
    
    def get_current_tasks(self):
        if len(self.__tasks) == 0:
            print("\nThere is no task in your ToDo List")
        for task in self.__tasks:
            print(task)

    def upload_new_task_json(self, tasks):
        with open("./tasks.json", "w") as f:
            json.dump(tasks, f, indent=4)

    def save_and_exit(self):
        pass

    def add_task(self):
        self.load_json()
        new_task = Task("Primul meu Task", "Descrierea primului meu task", "Tagul meu", "Maine", "High")
        self.__tasks.append(new_task.to_dict())
        self.upload_new_task_json(self.__tasks)


    def remove_task(self):
        pass

    def view_list(self):
        pass
