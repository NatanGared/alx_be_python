number = int(input("Enter a number to see its multiplication table: "))
y = [1,2,3,4,5,6,7,8,9,10]

for x in y:
    z = x * number
    print(f"{number} * {x} = {z}")

