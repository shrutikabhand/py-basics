# This program takes text input from the user and stores it in a file.
# The file content is then read using read() function.
# The text is split into separate words using split().
# The program checks each word using isalpha() to count only alphabetic words.
# Finally, it prints the total number of valid words present in the file.



texts = input()
file = open("data.txt", "w")
file.write(texts)
file.close()

file = open("data.txt", "r")
data = file.read()
words = data.split()
count = 0
for word in words:
    if word.isalpha():
        count += 1
print(count)
file.close()

