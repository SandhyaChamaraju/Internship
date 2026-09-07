def check_name_in_list():
    names_list = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
    search_name = input("Enter the name you want to search for: ")
    
    if search_name in names_list:
        print(f"Yes, '{search_name}' is present in the list.")
    else:
        print(f"No, '{search_name}' is not present in the list.")

if __name__ == "__main__":
    check_name_in_list()
