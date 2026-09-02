#CRUD Operations


# Create
items = ["Apple", "Banana", "Orange"]
print("Initial list:", items)

# Read
print("First item:", items[0])
print("All items:", items)

# Update
items[1] = "Mango"
print("After update:", items)

# Delete
items.remove("Orange")
print("After delete:", items)

# Add (part of Create)
items.append("Grapes")
print("After adding:", items)
