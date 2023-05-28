from abc import ABC, abstractmethod
from engines.base import Engine


class Car(ABC):
    @abstractmethod
    def __init__(self, engine: Engine):
        self.engine = engine

    @abstractmethod
    def start_engine(self):
        pass
