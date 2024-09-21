class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        self.speed = 0  # Car starts with speed 0

    def start(self):
        return "Car has started"

    def accelerate(self):
        self.speed += 10
        return f"Car is now going {self.speed} km/h"

    def stop(self):
        self.speed = 0
        return "Car has stopped"
my_car = Car("Red", "Toyota Corolla", 2020)
your_car = Car("Blue", "Honda Civic", 2022)

print(my_car.start())  # Output: "Car has started"
print(your_car.start())  # Output: "Car has started"
