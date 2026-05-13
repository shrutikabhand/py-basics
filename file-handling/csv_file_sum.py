# This program stores comma-separated integer values into a CSV file named data.csv.
# Each row of integers is written into the file using write() function.
# The file is then read line by line in read mode.
# Each line is split using commas to separate the integer values.
# The program calculates the sum of integers for every row and prints the result.



N = int(input())
file = open("data.csv", "w")
for _ in range(N):
    data = input()
    file.write(data +"\n")
file.close()

file = open("data.csv", "r")
for line in file:
    numbers = line.strip().split(",")
    count = 0
    for num in numbers :
        count += int(num)
    print(count)
file.close()

