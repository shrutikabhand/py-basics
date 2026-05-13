# This program creates a file named data.txt and stores the input string in it.
# The content of the file is then read using the read() function.
# The string is reversed using slicing operation [::-1].
# The reversed string is written into another file named rev_data.txt.
# Finally, the program reads and prints the contents of rev_data.txt.



S = input()

file = open("data.txt", "w")
file.write(S)
file.close()

file = open("data.txt", "r")
data = file.read()
file.close()

rev_data = data[::-1]

file = open("rev_data.txt", "w")
file.write(rev_data)
file.close()

file = open("rev_data.txt", "r")
print(file.read())
file.close()

