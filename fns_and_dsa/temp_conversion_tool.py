FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

A = int(input("Enter the temperature to convert: "))
B = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if B == "F":
    print(f"{A}°F is {convert_to_celsius(A)}°C")
elif B == "C":
    print(f"{A}°C is {convert_to_fahrenheit(A)}°F")
else:
    print("“Invalid temperature. Please enter a numeric value.”")

