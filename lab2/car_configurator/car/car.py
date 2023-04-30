class Car:
    def __init__(self, make: str, model: str, color: str):
        self.make = make
        self.model = model
        self.color = color

    def __str__(self):
        return f"Car(make={self.make}, model={self.model}, color={self.color})"
