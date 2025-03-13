# Contact Manager Application

# MENU LIST
def menu():
    print("\n-> Contacts Manager")
    print(" 1. Add New Contact")
    print(" 2. View All Contacts")
    print(" 3. Search a Contact")
    print(" 4. Update a Contact")
    print(" 5. Delete a Contact")
    print(" 6. EXIT")
    return int(input("Enter your choice: "))

contacts = []

# DUPLICATE CHECK
def duplicate_check(cont_name):
    cont_name = cont_name.lower() 
    for cont in contacts:
        if cont[0].lower() == cont_name: 
            print(f"Contact '{cont_name}' - {cont[1]} already exists! Use another name.")
            return True
    return False

# ADD NEW CONTACT FN
def add_cont():
    while True:
        cont_name = input("Enter the Name: ")
        if not duplicate_check(cont_name): 
            break
    cont_num = int(input("Enter the Phone number: "))
    cont_email = input("Enter Email: ")
    contacts.append((cont_name, cont_num, cont_email))
    print(f"{cont_name} Contact added successfully!")

# VIEW CONTACTS FN
def view_conts():
    if contacts:
        print("\nContact List:")
        for i, cont in enumerate(contacts, 1):
            print(f"{i}. Name: {cont[0]}, Phone: {cont[1]}, Email: {cont[2]}")
    else:
        print("\nNo contacts available!")

# SEARCH CONTACT FN
def search_cont():
    cont_name=input("Enter name to search: ")
    cont_name=cont_name.lower()
    for cont in contacts:
        if cont[0].lower() == cont_name:
            print(f"Contact found {cont[0]} - {cont[1]} - {cont[2]}")
            return
    print(f"{cont_name} not found in contacts")

# UPDATE CONTACT FN
def update_cont():
    cont_name = input("Enter the name to update: ").lower()
    for i, cont in enumerate(contacts):
        if cont[0].lower() == cont_name: 
            cont_num = int(input("Enter new phone number: "))
            contacts[i] = (cont[0], cont_num, cont[2])
            print("Contact Updated Successfully")
            return
    print(f"{cont_name} not found in contacts")
            
# DELETE CONTACT FN
def delete_cont():
    cont_name=input("Enter the name to update: ")
    cont_name=cont_name.lower()
    for cont in contacts:
        if cont[0].lower() == cont_name: 
            contacts.remove(cont)
            print("Contact Deleted Successfully")
            return
    print(f"{cont_name} not found in contacts")


while True:
    choice = menu()  

    if choice == 1:
        add_cont()
    elif choice == 2:
        view_conts()
    elif choice == 3:
        search_cont()
    elif choice == 4:
        update_cont()
    elif choice == 5:
        delete_cont()
    elif choice == 6:
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1-6.")
