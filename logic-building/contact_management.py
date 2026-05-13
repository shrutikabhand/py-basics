# This program implements a simple contact management system using dictionaries.
# It stores names and phone numbers entered by the user.
# The program displays all saved contacts
# and allows searching for a contact by name.
# If the contact exists, the details are displayed; otherwise,
# a "Contact not found" message is shown.



contacts = {}
n = int(input("Enter number of contacts: "))

for i in range(n):
    name = input("Enter name: ")
    phone_number = input("Enter contact number: ")
    contacts[name] = phone_number

print("\n--- Contact List ---")

for name, phone_number in contacts.items():
    print(f"Name: {name}, Contact Number: {phone_number}")

search = input("\nEnter contact name to search: ")

if search in contacts:
    print("Contact found!")
    print("Name:", search)
    print("Phone Number:", contacts[search])

else:
    print("Contact not found.")