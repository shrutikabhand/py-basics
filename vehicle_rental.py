# This program implements a simple vehicle rental system using a class.
# A private attribute __daily_rate is used to securely store the rental rate per day.
# The calculate_bill() method calculates the total rental cost based on the number of days.
# User inputs include vehicle type, daily rental rate, and rental duration.
# Finally, the program displays the vehicle type along with the total bill amount.



class Vehicle:
    
    def __init__(self, vehicle_type, daily_rate):
        self.vehicle_type = vehicle_type
        self.__daily_rate = daily_rate  

    def calculate_bill(self, days):
        return self.__daily_rate * days


vehicle_type = input()
daily_rate = int(input())
days = int(input())

v = Vehicle(vehicle_type, daily_rate)

total = v.calculate_bill(days)
print(f"Vehicle: {vehicle_type}, Total Bill: {total}")
