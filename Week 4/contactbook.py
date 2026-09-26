def display_menu():
    """Prints the available options to the user."""
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def contact_book():
    contacts = {}
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            name = input("Enter contact name: ").strip()
            if name in contacts:
                print(f"Error: '{name}' already exists. Use the update option to modify it.")
            else:
                phone = input("Enter phone number: ").strip()
                contacts[name] = phone
                print(f"Success: Contact '{name}' added successfully!")
                
        elif choice == '2':
            if not contacts:
                print("Your contact book is empty.")
            else:
                print("\n--- ALL CONTACTS ---")
                for name, phone in contacts.items():
                    print(f"Name: {name} | Phone: {phone}")
                    
        elif choice == '3':
            name = input("Enter the name to search: ").strip()
            if name in contacts:
                print(f"Found! Name: {name} | Phone: {contacts[name]}")
            else:
                print(f"Contact '{name}' not found.")
                
        elif choice == '4':
            name = input("Enter the contact name to update: ").strip()
            if name in contacts:
                new_phone = input(f"Enter new phone number for {name}: ").strip()
                contacts[name] = new_phone
                print(f"Success: Contact '{name}' updated successfully!")
            else:
                print(f"Contact '{name}' does not exist.")
                
        elif choice == '5':
            name = input("Enter the contact name to delete: ").strip()
            if name in contacts:
                contacts.pop(name)
                print(f"Success: Contact '{name}' deleted successfully!")
            else:
                print(f"Contact '{name}' not found.")
                

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
            
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    contact_book()
