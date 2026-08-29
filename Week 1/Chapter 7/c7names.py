l1 = [" Harry", "Sohan", "Sachin", "Rahul"]

# Loop through each name in the list
for name in l1:
    # .strip() removes any leading accidental spaces (like the one before " Harry")
    # .startswith("S") checks if the name begins with the letter 'S'
    if name.strip().startswith("S"):
        print(f"Hello, {name.strip()}!")
