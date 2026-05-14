# This program demonstrates different operations
# on Python data structures such as Lists, Sets, and Tuples.
# It uses classes, functions, and a menu-driven approach
# to perform various operations interactively.


# List Operations Class
class ListOperations:

    def operations(self):

        print("\n-------------- LIST OPERATIONS --------------\n")
        numbers = list(map(int,input("Enter list elements: ").split()))
        print("\nOriginal List:", numbers)

        # Append
        append_value = int(input("Enter element to append: "))
        numbers.append(append_value)
        print("After Append:", numbers)

        # Insert
        insert_index = int(input("Enter index to insert element: "))
        insert_value = int(input("Enter element to insert: "))
        numbers.insert(insert_index, insert_value)
        print("After Insert:", numbers)

        # Remove
        remove_value = int(input("Enter element to remove: "))
        if remove_value in numbers:
            numbers.remove(remove_value)
        print("After Remove:", numbers)

        # Pop
        pop_index = int(input("Enter index to pop element: "))
        if pop_index < len(numbers):
            numbers.pop(pop_index)
        print("After Pop:", numbers)

        # Modify
        modify_index = int(input("Enter index to modify: "))
        new_value = int(input("Enter new value: "))
        if modify_index < len(numbers):
            numbers[modify_index] = new_value
        print("After Modification:", numbers)

        # Sorting
        numbers.sort()
        print("Ascending Order:", numbers)
        numbers.sort(reverse=True)
        print("Descending Order:", numbers)

        # Maximum, Minimum, Sum
        print("Maximum:", max(numbers))
        print("Minimum:", min(numbers))
        print("Sum:", sum(numbers))

        # Remove duplicates
        unique_list = list(set(numbers))
        print("After Removing Duplicates:", unique_list)

        # Slicing
        start = int(input("Enter slice start index: "))
        end = int(input("Enter slice end index: "))
        print("Sliced List:", unique_list[start:end])

        print("\n-------------------- END --------------------\n")


# Set Operations Class
class SetOperations:

    def operations(self):

        print("\n--------------- SET OPERATIONS --------------\n")
        set1 = set(map(int,input("Enter elements of Set 1: ").split()))
        set2 = set(map(int,input("Enter elements of Set 2: ").split()))

        print("\nSet1:", set1)
        print("Set2:", set2)

        print("Union:", set1.union(set2))
        print("Intersection:",set1.intersection(set2))
        print("Difference (Set1 - Set2):",set1.difference(set2))
        print("Symmetric Difference:",set1.symmetric_difference(set2))
        print("Is Set1 subset of Set2?",set1.issubset(set2))
        print("Is Set1 superset of Set2?",set1.issuperset(set2))
        print("Are sets disjoint?",set1.isdisjoint(set2))

        # Common Elements
        common = set1.intersection(set2)
        print("Common Elements:",sorted(list(common)))

        print("\n-------------------- END --------------------\n")


# Tuple Operations Class
class TupleOperations:

    def operations(self):

        print("\n------------- TUPLE OPERATIONS --------------\n")
        data = tuple(input("Enter tuple elements: ").split())
        print("\nOriginal Tuple:", data)

        # Find index
        element = input("Enter element to find index: ")
        if element in data:
            print("Index of element:",
                  data.index(element))

        # Count occurrences
        count_element = input("Enter element to count: ")
        print("Count of element:",
              data.count(count_element))

        # Convert tuple to list
        temp_list = list(data)

        # Modify element
        modify_index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        if modify_index < len(temp_list):
            temp_list[modify_index] = new_value

        # Convert back to tuple
        data = tuple(temp_list)
        print("Modified Tuple:", data)

        print("\n-------------------- END --------------------\n")


# Menu-driven Program
while True:

    print("\n----- Data Structure Operations -----")
    print("1. List Operations")
    print("2. Set Operations")
    print("3. Tuple Operations")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        obj = ListOperations()
        obj.operations()

    elif choice == 2:
        obj = SetOperations()
        obj.operations()

    elif choice == 3:
        obj = TupleOperations()
        obj.operations()

    elif choice == 4:
        print("Exiting Program...")
        print("\n------------------- CLOSE -------------------\n")
        break

    else:
        print("Invalid choice")
        print("\n----------------- TRY AGAIN -----------------\n")