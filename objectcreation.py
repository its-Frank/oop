"""
Write a Python class named Car with attributes for make, model, and year. 
Add a method called display_info() that prints out the car’s details. 
Create an instance of the Car class and call the display_info() method.

"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This is a {self.year} {self.make} {self.model}.")

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Call the display_info() method
my_car.display_info()