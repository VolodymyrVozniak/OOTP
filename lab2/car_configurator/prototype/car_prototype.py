from ..car.car import Car

class CarPrototype:
    def __init__(self, car: Car):
        self._car = car

    def clone(self, **kwargs):
        car_attrs = self._car.__dict__.copy()
        car_attrs.update(kwargs)
        return Car(**car_attrs)
