## Objective

Develop a car factory application that creates and manages different car types and engines. The application should allow for the creation of Sedan, Hatchback, and SUV car types with Gasoline, Diesel, and Electric engines.

## Requirements

1. Implement the following car types as separate classes:
    * Sedan
    * Hatchback
    * SUV

2. Implement the following engine types as separate classes:
    * Gasoline Engine
    * Diesel Engine
    * Electric Engine

3. Create a clear and organized project directory structure with separate folders for car and engine classes.

4. The car classes should accept an engine object as an argument during instantiation and store it as a property.

5. Each car class should have a `start_engine()` method that prints the car type and delegates the engine start to the corresponding engine object.

6. Each engine class should have a `start()` method that prints the engine type and a message indicating that the engine has started.

7. Create a `main.py` file that demonstrates the creation and usage of different car and engine combinations.