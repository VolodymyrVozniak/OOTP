from .base import Car

class Sedan(Car):
    def __init__(self, engine):
        super().__init__(engine)

    def start_engine(self):
        print("Starting engine for Sedan")
        self.engine.start()
