import json

class ToDoList:
    def __init__(self):
        self.__tasks = []
        self.__load_json__()
        self.__get_current_tasks__()
        
    def __load_json__(self):
        with open('./tasks.json') as json_file:
            self.data = json.load(json_file)

    def __str__(self):
        for task in self.__tasks:
            print(task)
    
    def __get_current_tasks__(self):
        for task in self.data:
            self.__tasks.append(task)

    def save_and_exit(self):
        pass

    def add_task(self):
        pass

    def remove_task(self):
        pass

    def view_list(self):
        pass
