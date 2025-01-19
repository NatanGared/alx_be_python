def safe_divide(numerator, denominator):
    numerator = float(numerator)
    denominator = float(denominator)

    try:
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            return f"The result of the division is {float(numerator / denominator)}"
    except ValueError:
        print("Error: Please enter numeric values only.")
        
            



