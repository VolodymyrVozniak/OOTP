from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def __init__(self, engine):
        self.engine = engine

    @abstractmethod
    def start_engine(self):
        pass
