from car_configurator import Car, CarPrototype, CarBuilder

def main():
    # Using CarPrototype
    car_prototype = CarPrototype(Car(make='Toyota', model='Corolla', color='red'))
    car1 = car_prototype.clone()
    car2 = car_prototype.clone(color='blue')
    car3 = car_prototype.clone(model='Camry', color='black')

    print(car1)
    print(car2)
    print(car3)

    # Using CarBuilder
    car_builder = CarBuilder().set_make('Toyota').set_model('Corolla').set_color('red')
    car4 = car_builder.build()
    car_builder.set_color('blue')
    car5 = car_builder.build()
    car_builder.set_model('Camry').set_color('black')
    car6 = car_builder.build()

    print(car4)
    print(car5)
    print(car6)

if __name__ == "__main__":
    main()
