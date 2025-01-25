class Task:
    def __init__(self, title, description, tag, due_date, priority):
        self.title = title
        self.description = description
        self.tag = tag
        self.completed = False
        self.due_date = due_date
        self.priority = priority

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "tag": self.tag,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed
        }
