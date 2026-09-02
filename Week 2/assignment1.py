contacts = {}

while True:
    c = input("\n1.Add 2.Search 3.Update 4.Delete 5.Exit: ")

    if c == "1":
        n = input("Name: ")
        contacts[n] = input("Phone: ")
        print(contacts)

    elif c == "2":
        n = input("Name: ")
        print(contacts.get(n, "Not found"))

    elif c == "3":
        n = input("Name: ")
        if n in contacts:
            contacts[n] = input("New phone: ")
            print(contacts)
        else:
            print("Contact not found")

    elif c == "4":
        n = input("Name: ")
        contacts.pop(n, None)
        print(contacts)

    elif c == "5":
        break
