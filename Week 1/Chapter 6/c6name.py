def check_name_in_list():
    # 1. Define a list containing names
    names_list = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
    
    # 2. Get the name to search for from the user
    search_name = input("Enter the name you want to search for: ")
    
    # 3. Check for existence using the 'in' operator (Case-sensitive exact match)
    if search_name in names_list:
        print(f"Yes, '{search_name}' is present in the list.")
    else:
        print(f"No, '{search_name}' is not present in the list.")

# Run the program
if __name__ == "__main__":
    check_name_in_list()
