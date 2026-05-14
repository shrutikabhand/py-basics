# This program demonstrates abstraction, inheritance,
# and polymorphism in Python using different shapes.
# The program calculates area and perimeter
# for Circle, Rectangle, Triangle, and Square objects
# using a menu-driven approach.



from abc import ABC, abstractmethod

# Abstract Parent Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Circle Class
class Circle(Shape):

    def __init__(self):

        self.radius = float(input("Enter radius: "))

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Rectangle Class
class Rectangle(Shape):

    def __init__(self):

        self.length = float(input("Enter length: "))
        self.breadth = float(input("Enter breadth: "))

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

# Triangle Class
class Triangle(Shape):

    def __init__(self):

        self.base = float(input("Enter base: "))
        self.height = float(input("Enter height: "))

        self.side1 = float(input("Enter side 1: "))
        self.side2 = float(input("Enter side 2: "))
        self.side3 = float(input("Enter side 3: "))

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Square Class
class Square(Shape):

    def __init__(self):
        self.side = float(input("Enter side: "))

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


# Menu-driven Program
while True:

    print("\n----- Shape Calculator -----")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        c = Circle()
        print("Area:", c.area())
        print("Perimeter:", c.perimeter())

    elif ch == 2:
        r = Rectangle()
        print("Area:", r.area())
        print("Perimeter:", r.perimeter())

    elif ch == 3:
        t = Triangle()
        print("Area:", t.area())
        print("Perimeter:", t.perimeter())

    elif ch == 4:
        s = Square()
        print("Area:", s.area())
        print("Perimeter:", s.perimeter())

    elif ch == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid choice")