"""
Create a base class Animal with methods like eat() and sleep(). 
Then create a subclass Dog that inherits from Animal and adds a method bark(). 
Show how you can use both the inherited methods and the new method in an instance of Dog.
"""
class Animal:
    def eat(self):
        print("The animal is eating.")

    def sleep(self):
        print("The animal is sleeping.")

class Dog(Animal):
    def bark(self):
        print("The dog is barking.")

# Create an instance of the Dog class
my_dog = Dog()

# Use the inherited methods
my_dog.eat()
my_dog.sleep()

# Use the new method
my_dog.bark()