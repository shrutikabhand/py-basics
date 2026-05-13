# This program demonstrates the use of abstraction in Python using the abc module.
# An abstract class Appliance is created with an abstract method turn_on().
# Child classes WashingMachine and Refrigerator inherit from Appliance
# and provide their own implementation of the turn_on() method.
# Based on user input, the corresponding appliance object is created
# and its turn_on() method is executed.



from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing cycle started.")

class Refrigerator(Appliance):
    def turn_on(self):
        print("Cooling system active.")

appliance_name = input()

if appliance_name == "WashingMachine":
    obj = WashingMachine()

elif appliance_name == "Refrigerator":
    obj = Refrigerator()

obj.turn_on()


