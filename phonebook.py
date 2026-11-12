# a phonebook system


phone = dict()


while True:
    choice = input(" Enter what you want to do: \n 1. add contact \n 2. search for contact \n 3. display the phonebook \n 4. delete a contact \n 5. edit a contact \n 6. exit \n :")
    if choice == "1":
        print("add a contact")
        name = input("enter contact name:").capitalize()
        phone_number = input("enter phone number:")
        phone[name] = phone_number
        print(f'{name} succesfully added')
    elif choice == "2":
        print("search a contact")
        search_contact = input("enter contact name to search for:")
        if search_contact in phone:
            print(f'{search_contact} found in {phone[search_contact][phone_number]}')
        else:
            print(f'{search_contact} not found')
    elif choice == "3":
       print("display all contact")
       if phone:
           for name, phone_number in phone.items():
            print(f'All saved contact displayed: \n {phone[name][phone_number]}')
       else:
          print("Phonebook is empty.")

    elif choice == "4":
        print("delete a contact")
        name = input("Enter the contact name to delete: ").capitalize()
        if name in phone:
            del phone[name]
            print(f"{name} deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("edit a contact")
        name = input("Enter the contact name to edit: ").capitalize()
        if name in phone:
            new_number = input("Enter new phone number: ")
            phone[name] = new_number
            print(f"{name} updated successfully!")
        # elif phone_number in phone:
        #     new_name = input("Enter the new name ").capitalize()
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Exiting phonebook. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
 