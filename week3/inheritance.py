# Parent class: Animal
class Animal:
    def eat(self):
        return "I can eat!"

# Child class: Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        return "I can bark!"

# Create a Dog object
my_dog = Dog()

# Dog can both eat and bark
print(my_dog.eat())  # Output: "I can eat!" (inherited from Animal)
print(my_dog.bark())  # Output: "I can bark!" (unique to Dog)
