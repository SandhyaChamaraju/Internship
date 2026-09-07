import json
import matplotlib.pyplot as plt

with open("data.json", "r") as file:
    data = json.load(file)

x = data["x"]
y = data["y"]

plt.plot(x, y, marker="o")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Graph from JSON Data")
plt.grid(True)

plt.show()
