# This program stores inventory item names and quantities in a file.
# The details are written in the format ItemName:Quantity.
# The program then reads the file and checks which items have stock
# quantity less than the given threshold value T.
# Finally, it prints the names of items with low stock.



N = int(input())
file = open("inventory.txt", "w")
for _ in range(N):
    item, quantity = input().split()
    file.write(f"{item} : {quantity} \n")
file.close()

T = int(input())

file = open("inventory.txt", "r")
for line in file:
    item, quantity = line.strip().split(":")
    
    if int(quantity) < T:
        print(item)
file.close()

