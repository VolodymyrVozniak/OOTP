class PrioritySortStrategy:
    def sort(self, tasks):
        return sorted(tasks, key=lambda task: task.priority)


class DueDateSortStrategy:
    def sort(self, tasks):
        return sorted(tasks, key=lambda task: task.due_date)
