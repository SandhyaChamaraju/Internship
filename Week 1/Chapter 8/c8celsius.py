def celsius_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# --- Main Program Execution ---
try:
    # 1. Take temperature input from the user
    user_celsius = float(input("Enter temperature in Celsius: "))
    
    # 2. Call the function to perform the conversion
    converted_fahrenheit = celsius_to_fahrenheit(user_celsius)
    
    # 3. Display the result rounded to two decimal places
    print(f"{user_celsius:.2f}°C is equal to {converted_fahrenheit:.2f}°F")

except ValueError:
    print("Invalid input! Please enter a valid numerical value.")
