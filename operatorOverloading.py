"""
Define a class Vector that represents a vector in 2D space with x and y components. 
Overload the + operator to allow vector addition. 
Test this functionality by creating two Vector objects and adding them.
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Create two Vector objects and add them
vector1 = Vector(1, 2)
vector2 = Vector(3, 4)
result = vector1 + vector2
print(f"Vector 1: {vector1}")
print(f"Vector 2: {vector2}")
print(f"Result: {result}")