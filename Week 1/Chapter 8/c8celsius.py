def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

try:
    user_celsius = float(input("Enter temperature in Celsius: "))
    converted_fahrenheit = celsius_to_fahrenheit(user_celsius)
    print(f"{user_celsius:.2f}°C is equal to {converted_fahrenheit:.2f}°F")

except ValueError:
    print("Invalid input! Please enter a valid numerical value.")
