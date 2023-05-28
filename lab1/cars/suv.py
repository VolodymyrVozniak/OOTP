from .base import Car

class SUV(Car):
    def __init__(self, engine):
        super().__init__(engine)

    def start_engine(self):
        print("Starting engine for SUV")
        self.engine.start()
