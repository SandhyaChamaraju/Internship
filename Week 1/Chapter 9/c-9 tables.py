import os

# Create a folder named Tables
os.makedirs("Tables", exist_ok=True)

# Generate tables from 2 to 20
for i in range(2, 21):
    with open(f"Tables/Table_{i}.txt", "w") as file:
        for j in range(1, 11):
            file.write(f"{i} x {j} = {i * j}\n")

print("Multiplication tables from 2 to 20 have been created.")
