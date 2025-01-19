def safe_divide(numerator, denominator):

    try:
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            return f"The result of the division is {float(numerator) / float(denominator)}"
    except ValueError:
        return ValueError("Error: Please enter numeric values only.")
            



