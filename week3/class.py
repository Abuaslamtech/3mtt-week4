class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def start(self):
        return "Car has started"

my_car = Car("Red", "Toyota Corolla")  # An object of the Car class
your_car = Car("Blue", "Honda Civic")  # Another object
dev = Car("black", "Pigeot")
print(dev.color)
