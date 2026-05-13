# A parking lot has exactly 10 slots. Each slot is represented as:
# 0 → Empty
# 1 → Occupied You are given the current status of all 10 parking slots.
# Your task is to:

# Count total empty slots
# Count total occupied slots
# Determine whether parking is FULL or NOT FULL
# Print slot numbers (1-based indexing) that are empty



slots = []
for i in range(10):
    n = int(input())
    slots.append(n)

# slots = input().split()

empty = 0
occupied = 0
empty_slots = []

for i in range(10):
    if (slots[i]) == 0:
        empty = empty + 1
        empty_slots.append(i+1)
    else:
        occupied = occupied + 1

if empty == 0 :
    status = "FULL"
else:
    status = "NOT FULL"

print("Empty Slots:", empty)
print("Occupied Slots:", occupied)
print("Parking Status:", status)

print("Empty Slot Numbers:", end=" ")
for s in empty_slots:
    print(s, end=" ")


