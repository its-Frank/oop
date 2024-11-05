"""
Create a base class Employee with a method calculate_salary() that prints a generic message.
 Then create a subclass Manager that overrides calculate_salary() to provide a specific calculation for a manager’s salary. 
 Demonstrate the overridden behavior.
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        print(f"The employee's salary is: {self.salary}")

class Manager(Employee):
    def calculate_salary(self):
        bonus = 0.2 * self.salary
        total_salary = self.salary + bonus
        print(f"The manager's salary is: {total_salary}")

# Create instances of Employee and Manager
employee = Employee("John Doe", 5000)
manager = Manager("Jane Smith", 8000)
# Call the calculate_salary() method on both instances
employee.calculate_salary()
manager.calculate_salary()