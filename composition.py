"""
Define two classes, Engine and Car. The Car class should have an attribute engine that is an instance of the Engine class. 
Write methods for Engine (e.g., start() and stop()) and show how the Car class can use these methods to control the engine.
"""
class Engine:
    def start(self):
        print("The engine has started.")

    def stop(self):
        print("The engine has stopped.")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()

    def stop_car(self):
        self.engine.stop()

# Create an instance of the Car class
my_car = Car()

# Start and stop the car
my_car.start_car()
my_car.stop_car()