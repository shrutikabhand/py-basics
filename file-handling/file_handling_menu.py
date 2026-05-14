# This program demonstrates basic file handling operations in Python.
# It allows the user to create, read, append,
# and verify file contents using a menu-driven system.
# The program uses functions to organize different file operations.



def create_file():
    file = open("example.txt", "w")
    file.write("Python is easy to learn.\n")
    file.write("File handling is very useful.\n")
    file.close()
    print("File created and data written successfully")
    print("--------------------------------------------------------------\n")

def read_file():
    file = open("example.txt", "r")
    print("\nFile Content:\n")
    print(file.read())
    file.close()
    print("--------------------------------------------------------------\n")

def append_file():
    file = open("example.txt", "a")
    line = input("Enter line to append: ")
    file.write(line + "\n")
    file.close()
    print("Data appended successfully")
    print("--------------------------------------------------------------\n")

def verify_file():
    file = open("example.txt", "r")
    print("\nUpdated Content:\n")
    print(file.read())
    file.close()
    print("--------------------------------------------------------------\n")


# Menu-driven program
while True:
    print("\n----- File Handling Menu -----")
    print("1. Create & Write File")
    print("2. Read File")
    print("3. Append Data")
    print("4. Verify Updated Content")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_file()

    elif choice == 2:
        read_file()

    elif choice == 3:
        append_file()

    elif choice == 4:
        verify_file()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
print("-----------------------------END-----------------------------------\n")
