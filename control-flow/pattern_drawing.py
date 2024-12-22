pattern = int(input("Enter the size of the pattern: "))
row = 0

while row < pattern:
    for x in range(pattern):
        print("*", end="")
    row += 1
    print()