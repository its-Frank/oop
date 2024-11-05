"""
Define two classes, Cat and Dog, each with a make_sound() method that prints a different sound specific to each animal. 
Write a function that takes an object and calls make_sound(), 
then demonstrate polymorphism by passing instances of both Cat and Dog to this function.
"""
class Cat:
    def make_sound(self):
        print("Meow!")

class Dog:
    def make_sound(self):
        print("Woof!")

def make_animal_sound(animal):
    animal.make_sound()

# Create instances of Cat and Dog
my_cat = Cat()
my_dog = Dog()

# Demonstrate polymorphism
make_animal_sound(my_cat)
make_animal_sound(my_dog)