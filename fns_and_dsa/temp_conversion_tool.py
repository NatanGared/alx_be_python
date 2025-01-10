X = 0
FAHRENHEIT_TO_CELSIUS_FACTOR = ((X +32) *(5/9))
CELSIUS_TO_FAHRENHEIT_FACTOR = (((9/5)* X)+32)

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    global X

    X = fahrenheit
    FAHRENHEIT_TO_CELSIUS_FACTOR = ((X +32) *(5/9))
    return FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    global X

    X = celsius
    CELSIUS_TO_FAHRENHEIT_FACTOR = (((9/5)* X)+32)
    return CELSIUS_TO_FAHRENHEIT_FACTOR

A = int(input("Enter the temperature to convert: "))
B = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

print(convert_to_celsius(-40))
if B == "C":
    print(f"{A}°F is {convert_to_fahrenheit(A)}°C")
elif B == "F":
    print(f"{A}°C is {convert_to_celsius(A)}°F")
else:
    print("“Invalid temperature. Please enter a numeric value.”")

