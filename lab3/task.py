class Task:
    def __init__(self, id, description, due_date=None):
        self.id = id  # Unique identifier
        self.description = description
        self.due_date = due_date
        self.priority = "medium"  # Default priority
        self.completed = False

    def __str__(self):
        return f"Task {self.id}: {self.description}"

    def set_priority(self, priority):
        self.priority = priority

    def complete(self):
        self.completed = True
