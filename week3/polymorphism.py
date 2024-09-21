# Parent class: Animal
class Animal:
    def make_sound(self):
        return "Some generic animal sound"

# Child class: Dog, inherits from Animal but changes the behavior of make_sound
class Dog(Animal):
    def make_sound(self):
        return "Bark!"

# Child class: Cat, inherits from Animal but changes the behavior of make_sound
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Create objects of Dog and Cat
my_dog = Dog()
my_cat = Cat()

# Even though both objects have make_sound method, they behave differently
print(my_dog.make_sound())  # Output: "Bark!"
print(my_cat.make_sound())  # Output: "Meow!"