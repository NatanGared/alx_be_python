def safe_divide(numerator, denominator):

    try:
        if ZeroDivisionError:
            return "Error: Cannot divide by zero."
        else:
            return f"The result of the division is {float(numerator) / float(denominator)}"
    except Exception as a:
        return ValueError("Error: Please enter numeric values only.")
            



