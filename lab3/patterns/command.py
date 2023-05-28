from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class CreateTaskCommand(Command):
    def __init__(self, task_list, task):
        self.task_list = task_list
        self.task = task

    def execute(self):
        self.task_list.add_task(self.task)

    def undo(self):
        self.task_list.tasks.remove(self.task)


class UpdateTaskCommand(Command):
    def __init__(self, task_list, task_id, **kwargs):
        self.task_list = task_list
        self.task_id = task_id
        self.old_state = {}

        task = self.task_list.get_task_by_id(task_id)
        if task:
            for attr, value in kwargs.items():
                self.old_state[attr] = getattr(task, attr)
                setattr(task, attr, value)
        else:
            raise ValueError(f"No task found with id {task_id}")

    def execute(self):
        pass  # No action required

    def undo(self):
        task = self.task_list.get_task_by_id(self.task_id)
        if task:
            for attr, value in self.old_state.items():
                setattr(task, attr, value)
        else:
            raise ValueError(f"No task found with id {self.task_id}")


class CompleteTaskCommand(Command):
    def __init__(self, task_list, task_id):
        self.task_list = task_list
        self.task_id = task_id
        self.task = None

    def execute(self):
        self.task = self.task_list.get_task_by_id(self.task_id)
        if self.task:
            self.task_list.complete_task(self.task_id)
        else:
            raise ValueError(f"No task found with id {self.task_id}")

    def undo(self):
        if self.task:
            self.task.completed = False
            self.task_list.tasks.append(self.task)
        else:
            raise ValueError(f"No task found with id {self.task_id}")
