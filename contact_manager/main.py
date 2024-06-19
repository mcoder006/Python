import json

print("=="*20)
print("Contact Manager Python : ")
print("=="*20)

def load_contact():
    try:
        with open("Contact.txt", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    
def save_data_helper(contacts):
    with open("Contact.txt", "w") as file:
        json.dump(contacts, file)

def add_contact(contacts):
    name = input("Enter name : ")
    phone = input("Enter phone number : ")
    email = input("Enter email address : ")
    contact = {"name": name, "phone_number": phone, "email_address": email}
    contacts.append(contact)
    save_data_helper(contacts)
    print("\n")

def view_contacts(contacts):
    if not contacts:
        print("No contact found.")
    else:
        print("=="*20)
        for i, contact in enumerate(contacts, start=1):
            print(f"Contact {i} : ")
            print(f"Name : {contact['name']}")
            print(f"Phone Number : {contact['phone_number']}")
            print(f"Email Address : {contact['email_address']}")
            print("-"*35)
        print("=="*20)
        print("\n" )

def update_contact(contacts):
    if not contacts:
        print("No contact found.")
    else:
        view_contacts(contacts)
        update_no = int(input("Enter the number of contact to update : "))
        if update_no < 0 and update_no > len(contacts):
            print("Invalid Index")
        else:
            name = input("Enter name : ")
            phone = input("Enter phone number : ")
            email = input("Enter email address : ")
            contact = {"name": name, "phone_number": phone, "email_address": email}
            contacts[update_no - 1] = contact
            save_data_helper(contacts)
            print("\n")

def delete_contact(contacts):
    if not contacts:
        print("No contact found.")
    else:
        view_contacts(contacts)
        delete_no = int(input("Enter the number of contact to delete : "))
        if delete_no < 0 and delete_no > len(contacts):
            print("Invalid Index")
        else:
            del contacts[delete_no - 1]
            save_data_helper(contacts)
            print("\n") 


def main():
    contacts = load_contact()
    while True:  
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Delete Contact")
        print("4. Update Contact")
        print("5. Exit")
        choice = input("Enter your choice : ")
        match choice:
            case "1":
                add_contact(contacts)
            case "2":
                view_contacts(contacts)
            case "3":
                delete_contact(contacts)
            case "4":
                update_contact(contacts)
            case "5":
                exit()
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()

