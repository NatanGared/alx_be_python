def perform_operation(num1, num2, operation):
    if operation == "add":
        solution = float(num1) + float(num2)
    elif operation == "subtract":
        solution = float(num1) - float(num2)
    elif operation == "multiply":
        solution = float(num1) * float(num2)
    elif operation == "divide":
        if num2 == 0:
            print("That is an invalid operation")
        else:
            solution = float(num1) / float(num2)
    else:
        print("you have inserted the wrong kind of data or argument! Kindly review what you have done!")

    return solution
