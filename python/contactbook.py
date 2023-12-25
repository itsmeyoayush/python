class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {'Phone Number': phone_number, 'Email': email, 'Address': address}
        print(f"Contact {name} added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("\nContact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone Number: {details['Phone Number']}")
                print(f"Email: {details['Email']}")
                print(f"Address: {details['Address']}")
                print("---------------")

    def search_contact(self, search_key):
        search_results = []
        for name, details in self.contacts.items():
            if search_key.lower() in name.lower() or search_key in details['Phone Number']:
                search_results.append((name, details))
        return search_results

    def update_contact(self, name, phone_number, email, address):
        if name in self.contacts:
            self.contacts[name] = {'Phone Number': phone_number, 'Email': email, 'Address': address}
            print(f"Contact {name} updated successfully!")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact {name} not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)

        elif choice == '2':
            contact_book.view_contact_list()

        elif choice == '3':
            search_key = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(search_key)
            if results:
                print("\nSearch Results:")
                for name, details in results:
                    print(f"Name: {name}")
                    print(f"Phone Number: {details['Phone Number']}")
                    print(f"Email: {details['Email']}")
                    print(f"Address: {details['Address']}")
                    print("---------------")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter name to update: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_book.update_contact(name, phone_number, email, address)

        elif choice == '5':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
