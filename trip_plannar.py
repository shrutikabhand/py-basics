# You are planning a trip and want to estimate how much fuel will be required.
#Write a program that: - Takes the destination name as a string. - Takes the total distance to the destination in kilometers (float). - Takes the vehicle’s fuel efficiency in kilometers per liter (float).

destination = input()
distance = float(input())
fuel_efficiency = float(input())
litres = distance / fuel_efficiency
print(f"To reach {destination}, you need{litres: .2f} liters of fuel.")