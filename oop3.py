"""
How can we utilize the objects created from the class blueprint 
employee , to get the company's total payroll in class Payroll ? 
"""
"""
Employee payro;ll system
add an employee and add a salary on the same
return total cost on payroll
"""

"""
{
  "salary" : ,
  "name" " , 
}
"""

"""
  [ 
    {
  "salary" : ,
  "name" " , 
}, 
{
  "salary" : ,
  "name" " , 
},

    
  ]
"""
employees = []

def add_employee(employees, name,salary):
    return employees + [{"name" : name, "salary" : salary}]

def calculate_total_payroll(employees):
    return sum(employee["salary"] for employee in employees if employee["salary"] > 0)

# usage
employees = add_employee(employees,"Joseph", 1000)
employees = add_employee(employees,"Habiba",2000)
total_payroll = calculate_total_payroll(employees)
print(total_payroll)
print(employees)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp1 = Employee("Bob", "40000")
print(f"{emp1.name} {emp1.salary}")

class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_payroll(self):
        total = 0
        for employee in self.employees:
            total += employee.salary
        return total

# Usage
payroll = Payroll()
payroll.add_employee(Employee("Joseph", 1000))
payroll.add_employee(Employee("Habiba", 2000))
total_payroll = payroll.calculate_total_payroll()
print(total_payroll)  # Output: 3000

















