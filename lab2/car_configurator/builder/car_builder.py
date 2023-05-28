from copy import deepcopy
from ..car.car import Car


class CarBuilder:
    def __init__(self):
        self._car = Car(make='', model='', color='')

    def set_make(self, make: str):
        self._car.make = make
        return self

    def set_model(self, model: str):
        self._car.model = model
        return self

    def set_color(self, color: str):
        self._car.color = color
        return self

    def build(self) -> Car:
        return deepcopy(self._car)
