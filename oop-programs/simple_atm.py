# This program simulates a simple ATM banking system.
# It allows the user to check balance, deposit money,
# and withdraw money using different commands.
# The program uses loops and conditional statements
# to continuously process user actions until the user exits.
# It also checks for insufficient balance during withdrawal operations.



balance = int(input("Enter account balance: "))

while True:
    command = input("Enter command: ").lower()

    if command == "check":
        print("Balance:",balance)

    elif command == "deposit":
        amount = int(input("Enter amount to deposit: "))
        balance += amount

    elif command == "withdraw":
        amount = int(input("Enter amount to withdraw: "))

        if(amount <= balance):
            balance -= amount

        else:
            print("Insufficient Balance!")

    elif command =="quit":
        break

            


