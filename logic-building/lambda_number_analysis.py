# This program demonstrates the use of lambda functions,
# map(), filter(), and reduce() in Python.
# It performs different numerical operations
# on a list of user-entered numbers.

from functools import reduce


# Number Analysis Function
def number_analysis(numbers):

    # Sum
    total = reduce(lambda x, y: x + y, numbers)

    # Product
    product = reduce(lambda x, y: x * y, numbers)

    # Maximum
    maximum = reduce(lambda x, y: x if x > y else y, numbers)

    # Minimum
    minimum = reduce(lambda x, y: x if x < y else y, numbers)

    # Average
    average = total / len(numbers)

    # Even & Odd Numbers
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

    # Squares using map
    squares = list(map(lambda x: x * x, numbers))

    # Cubes using map
    cubes = list(map(lambda x: x ** 3, numbers))

    # Sorted Lists
    ascending = sorted(numbers)

    descending = sorted(numbers, reverse=True)

    # Display Results
    print("\n----- Number Analysis -----")

    print("Numbers:", numbers)
    print("Sum =", total)
    print("Product =", product)
    print("Maximum =", maximum)
    print("Minimum =", minimum)
    print(f"Average = {average:.2f}")
    print("Even Numbers =", even_numbers)
    print("Odd Numbers =", odd_numbers)
    print("Squares =", squares)
    print("Cubes =", cubes)
    print("Ascending Order =", ascending)
    print("Descending Order =", descending)


# Main Program
numbers = list(map(int, input("Enter numbers: ").split()))

number_analysis(numbers)