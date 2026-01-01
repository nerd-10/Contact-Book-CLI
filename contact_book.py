import json

contacts = []

#add details to contact book

def add_details():
    name = input("Please enter the name: ")
    try:
        phone = input("Please enter the phone number: ")
        if len(phone) != 10:
            raise ValueError("Invalid phone number length.")
    except ValueError as ve:
        print(ve)
        return
    try:
        email = input("Please enter the email address: ")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
    except ValueError as ve:
        print(ve)
        return
    address = input("Please enter your address: ")
    contact = {
        "Name": name,
        "Phone Number": phone,
        "Email": email,
        "Address": address
    }
    contacts.append(contact)
    save_contacts_to_file()
    print("\n Contact added successfully!")

def save_contacts_to_file():
    with open("Contact_Book.json", "w") as f:
        json.dump(contacts, f, indent = 4)
        print("Contacts saved to Contact_Book.json file successfully.")

def load_contacts_from_file():
    try:
        with open("Contact_Book.json", "r") as f:
            book= json.load(f)
            contacts.clear()
            contacts.extend(book)
            print("Contacts loaded from Contact_Book.json file successfully.")
    except FileNotFoundError:
        print("No existing contact data found.")


def view_contacts():
    if len(contacts) == 0:
        print("No contacts to display.")
    else:
        for index, contact in enumerate(contacts, start = 1):
            print("Contact", index)
            print("Name:", contact["Name"])
            print("Phone Number:", contact["Phone Number"])
            print("Email:", contact["Email"])
            print("Address:", contact["Address"])
            print()
def search_contact():
    found = False
    search_name = input("Enter the name of the contact to search: ")
    for c in contacts:
        if search_name.lower() == c["Name"].lower():
            found = True
            print("Contact found:")
            print("Name:", c["Name"])
            print("Phone Number:", c["Phone Number"])
            print("Email:", c["Email"])
            print("Address:", c["Address"])
            break

    if not found:
        print("Contact not found.")


def delete_contact():
    if len(contacts) == 0:
        print("No contacts to delete.")
        return
    else:
        try:
            name_to_delete = input("Please enter the name of the contact you want to delete: ")
            for c in contacts:
                if name_to_delete.lower() == c["Name"].lower():
                    removed_contact = contacts.pop(contacts.index(c))
                    print(f"Contact {removed_contact['Name']} is removed successfully.")
                    save_contacts_to_file()
                    break
            else:
                print("No such Name found in the contact book.")
        except ValueError:
            print("Invalid input. Please try again.")
            
def menu():
    while True:
        print("\n Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        print()
        if choice == "1":
            add_details()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    load_contacts_from_file()
    menu()
