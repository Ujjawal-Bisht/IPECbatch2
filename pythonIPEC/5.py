# WAP for address book management system using functions and exception handling and dictionary

class Person:
    _book = dict()
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        Person._book[name] = self

    def intro(self):
        print(f"Name: {self.name} | Phone: {self.phone} | Email: {self.email}")


def add_contact():
    """Add a contact to the address book."""
    name = input("Enter contact name: ")

    if name in Person._book:
        print(f"Contact '{name}' already exists in address book.")
        return
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    Person(name, phone, email)

def view():
    Person.intro(Person)
# def view():
#     """View all contacts in the address book."""
#     if not book:
#         print("Address book is empty.")
#         return
#     else:
#         for name, info in book.items():
#             print(f"Name: {name} | Phone: {info['phone']} | Email: {info['email']}")


def delete_contact():
    """Delete a contact from the address book."""
    name = input("Enter contact name to delete: ")
    try:
        del book[name]
        print(f"Contact '{name}' deleted successfully.")
    except KeyError:
        print(f"Contact '{name}' not found in address book.")


def update_contact():
    """Update a contact in the address book."""
    name = input("Enter contact name to update: ")
    if name not in book:
        print(f"Contact '{name}' not found in address book.")
        return
    
    phone = input("Enter updated phone number: ")
    email = input("Enter updated email: ")
    book[name] = {'phone': phone, 'email': email}
    print(f"Contact '{name}' updated successfully.")


if __name__ == "__main__":
    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Update Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            print("Closing Address Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
