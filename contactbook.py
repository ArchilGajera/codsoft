contacts = []

def add_contact():
    print("Add a new contact:")
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {
        "Name": name,
        "Phone Number": phone_number,
        "Email": email,
        "Address": address
    }
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contact_list():
    print("List of Contacts:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['Name']} - Phone: {contact['Phone Number']}")
    print()

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = []
    for contact in contacts:
        if (
            search_term.lower() in contact['Name'].lower()
            or search_term in contact['Phone Number']
        ):
            found_contacts.append(contact)
    if found_contacts:
        print("Search Results:")
        for index, contact in enumerate(found_contacts, start=1):
            print(
                f"{index}. Name: {contact['Name']} - Phone: {contact['Phone Number']}"
            )
    else:
        print("No contacts found with the given search term.")
    print()

def update_contact():
    search_term = input("Enter name or phone number to update: ")
    for contact in contacts:
        if (
            search_term.lower() in contact['Name'].lower()
            or search_term in contact['Phone Number']
        ):
            print("Choose what to update:")
            print("1. Name")
            print("2. Phone number")
            print("3. Email")
            print("4. Address")
            choice = input("Enter your choice: ")
            if choice == "1":
                new_name = input("Enter the new name: ")
                contact['Name'] = new_name
            elif choice == "2":
                new_phone = input("Enter the new phone number: ")
                contact['Phone Number'] = new_phone
            elif choice == "3":
                new_email = input("Enter the new email: ")
                contact['Email'] = new_email
            elif choice == "4":
                new_address = input("Enter the new address: ")
                contact['Address'] = new_address
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    search_term = input("Enter name or phone number to delete: ")
    for contact in contacts:
        if (
            search_term.lower() in contact['Name'].lower()
            or search_term in contact['Phone Number']
        ):
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

# User interface
while True:
    print("CONTACT MANAGEMENT SYSTEM")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Please enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact_list()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank you. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.\n")
