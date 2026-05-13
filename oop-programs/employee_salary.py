# This program demonstrates inheritance and method overriding in Python.
# A parent class Employee is created with attributes name and base_salary.
# The child class Manager inherits from Employee and adds a bonus attribute.
# The display_salary() method is overridden in the Manager class
# to calculate and display the total salary including the bonus.
# Finally, a Manager object is created using user input values.



class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def display_salary(self):
        print(f"{self.name}'s Salary: {self.base_salary}")

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def display_salary(self):
        total_salary = self.base_salary + self.bonus
        print(f"{self.name}'s Salary: {total_salary}")

name = input()
base_salary = int(input())
bonus = int(input())
m = Manager(name, base_salary, bonus)
m.display_salary()

