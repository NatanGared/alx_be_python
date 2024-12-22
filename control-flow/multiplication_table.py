number = int(input("Enter a number to see its multiplication table: "))
y = range(1,11)

for x in y:
    z = x * number
    print(f"{number} * {x} = {z}")

