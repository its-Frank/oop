"""
Python does not directly support constructor overloading, but you can simulate it using default arguments. 
Write a class Rectangle with a constructor that can initialize the rectangle with either one (for a square) or two parameters (for a general rectangle). 
Add a method to calculate the area, and test it by creating squares and rectangles.
"""
class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width  # Square
        else:
            self.height = height  # Rectangle

    def calculate_area(self):
        return self.width * self.height

# Create a square
square = Rectangle(5)
print(f"Area of the square: {square.calculate_area()}")

# Create a rectangle
rectangle = Rectangle(4, 6)
print(f"Area of the rectangle: {rectangle.calculate_area()}")