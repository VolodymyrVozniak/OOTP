from patterns.observer import TaskSubject


class TaskList:
    def __init__(self):
        self.tasks = []
        self.observers = []

    def add_task(self, task):
        task.id = len(self.tasks) + 1
        self.tasks.append(task)
        # self.notify_observers()

    def update_task(self, task_id, **kwargs):
        task = self.get_task_by_id(task_id)
        if task:
            for attr, value in kwargs.items():
                setattr(task, attr, value)
            # self.notify_observers()
        else:
            raise ValueError(f"No task found with id {task_id}")

    def complete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.complete()
            self.tasks.remove(task)
            self.notify_observers(task)
        else:
            raise ValueError(f"No task found with id {task_id}")

    def display_tasks(self, sort_strategy=None, filter_completed=None):
        if sort_strategy:
            self.tasks = sort_strategy.sort(self.tasks)
        if filter_completed is not None:
            filtered_tasks = [task for task in self.tasks if task.completed == filter_completed]
            self.tasks = filtered_tasks
        print()
        for task in self.tasks:
            print(task)
    
    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, task):
        for observer in self.observers:
            observer.update(task)
