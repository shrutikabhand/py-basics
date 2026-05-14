# This program implements a simple student record management system.
# It allows users to add, display, and search student records using file handling.
# Student details such as roll number, name, and marks are stored in a text file.
# The program uses functions, exception handling, and a menu-driven approach
# to manage records efficiently.



def add_record():
    try:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        with open("students.txt", "a") as file:
            file.write(roll + "," + name + "," + str(marks) + "\n")

        print("Record added successfully")

    except ValueError:
        print("Invalid marks input")


def display_records():
    try:
        with open("students.txt", "r") as file:
            print("\nAll Records:")

            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("No records found")


def search_record():
    roll_search = input("Enter Roll No to search: ")

    found = False

    try:
        with open("students.txt", "r") as file:

            for line in file:
                data = line.strip().split(",")

                if data[0] == roll_search:
                    print("Record Found:", data)
                    found = True
                    break

        if not found:
            print("Record not found")

    except FileNotFoundError:
        print("File not found")


# Menu-driven program
while True:

    print("\n1.Add Record\n2.Display Records\n3.Search Record\n4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_record()

    elif choice == 2:
        display_records()

    elif choice == 3:
        search_record()

    elif choice == 4:
        break

    else:
        print("Invalid choice")