# This program stores multiple system log entries into a file named system.log.
# The log entries are written line by line using write() function.
# The file is then opened in read mode to check each log entry.
# The program searches for the keyword "ERROR" in a case-sensitive manner.
# Finally, it counts and prints the total number of lines containing "ERROR".



N = int(input())
file = open("system.log", "w")
for _ in range(N):
    log = input()
    file.write(log + "\n")
file.close()

file = open("system.log", "r")
count = 0 
for line in file:
    if "ERROR" in line:
        count += 1
print(count)
file.close()

