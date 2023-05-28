from .base import Car
from engines.base import Engine


class Sedan(Car):
    def __init__(self, engine: Engine):
        super().__init__(engine)

    def start_engine(self):
        print("Starting engine for Sedan")
        self.engine.start()
