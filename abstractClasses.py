"""
 Use the abc module to create an abstract base class Shape with an abstract method area(). 
 Then, implement subclasses Circle and Square that provide their own implementations of area(). 
 Write code to create instances of Circle and Square, and call area() on each.
"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Create instances of Circle and Square
circle = Circle(5)
square = Square(4)
# Call the area() method on each instance
print(f"Area of the circle: {circle.area()}")
print(f"Area of the square: {square.area()}")