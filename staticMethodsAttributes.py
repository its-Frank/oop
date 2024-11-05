"""
Write a Calculator class with a static method add() that takes two numbers and returns their sum. 
Also, add a static attribute count to track the number of times the add() method has been called. 
Show how to use this static method and update count.
"""
class Calculator:
    count = 0

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

# Call the static add() method
result1 = Calculator.add(5, 10)
print(f"The sum is: {result1}")
print(f"The add() method has been called {Calculator.count} times.")

result2 = Calculator.add(3, 7)
print(f"The sum is: {result2}")
print(f"The add() method has been called {Calculator.count} times.")