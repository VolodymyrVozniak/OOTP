from task import Task
from task_list import TaskList
from patterns.strategy import PrioritySortStrategy, DueDateSortStrategy
from patterns.observer import TaskObserver
from patterns.command import CreateTaskCommand, UpdateTaskCommand, CompleteTaskCommand


def main():
    task_list = TaskList()

    # Register an observer to display tasks when the list changes
    task_observer = TaskObserver()
    task_list.register_observer(task_observer)

    # Create tasks
    task1 = Task(1, "Do something", 26)
    task2 = Task(2, "Do something else", 23)
    task3 = Task(3, "Do another thing", 21)
    create_task_command1 = CreateTaskCommand(task_list, task1)
    create_task_command2 = CreateTaskCommand(task_list, task2)
    create_task_command3 = CreateTaskCommand(task_list, task3)
    create_task_command1.execute()
    create_task_command2.execute()
    create_task_command3.execute()

    # Update task
    update_task_command = UpdateTaskCommand(task_list, 1, description="Updated Task")
    update_task_command.execute()

    # Complete task
    complete_task_command = CompleteTaskCommand(task_list, 2)
    complete_task_command.execute()

    # Display tasks
    task_list.display_tasks()

    # Undo complete task
    complete_task_command.undo()
    task_list.display_tasks()

    # Display tasks sorted by priority
    task2.set_priority("high")
    task_list.display_tasks(sort_strategy=PrioritySortStrategy())

    # Display tasks sorted by due date
    task_list.display_tasks(sort_strategy=DueDateSortStrategy())


if __name__ == "__main__":
    main()
