## Task Description

The task is to develop a simple task manager application that allows users to create, update, and complete tasks. The application should provide various functionalities to manipulate tasks, such as adding notes, setting due dates, and assigning priorities.

## Requirements

The task manager application should satisfy the following requirements:

1. Create a task:
    * The application should allow users to create a new task by providing an id, description, and optional due date.
    * Each task should have a unique identifier.
    * The application should assign a default priority to the task (e.g., medium).
    * The created task should be added to the task list.

2. Update a task:
    * The application should allow users to update an existing task by providing the task's unique identifier.
    * Users can update the task's id, description, due date, and priority.
    * The application should validate and handle any input errors gracefully.

3. Complete a task:
    * The application should allow users to mark a task as completed by providing the task's unique identifier.
    * Once a task is marked as completed, it should be removed from the task list.

4. Display tasks:
    * The application should provide options to display all tasks or filter tasks based on their priority.
    * Users should be able to view the task list sorted by priority or due date.

## Class Decomposition

1. `main.py`: The main entry point of the application.
2. `task.py`: Defines the `Task` class, representing a single task with attributes such as title, description, due date, priority, and completion status.
3. `task_list.py`: Implements the `TaskList` class, which manages a collection of tasks. It provides methods to add, update, complete, and display tasks.
4. `patterns/strategy.py`: Implements the Strategy pattern for sorting tasks by priority or due date. It defines the `PrioritySortStrategy` and `DueDateSortStrategy` classes.
5. `patterns/observer.py`: Implements the Observer pattern to notify observers when a task's completion status changes. It defines the `TaskObserver` and `TaskSubject` classes.
6. `patterns/command.py`: Implements the Command pattern to encapsulate task-related operations as commands. It defines the `Command` interface and concrete command classes such as `CreateTaskCommand`, `UpdateTaskCommand`, and `CompleteTaskCommand`.
