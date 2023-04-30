from .base import Car

class Hatchback(Car):
    def __init__(self, engine):
        super().__init__(engine)

    def start_engine(self):
        print("Starting engine for Hatchback")
        self.engine.start()
