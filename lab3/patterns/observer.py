class TaskObserver:
    def update(self, task):
        print(f"Notify that `{task}` was completed!")


class TaskSubject:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)
