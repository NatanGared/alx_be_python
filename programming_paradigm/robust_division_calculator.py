def safe_divide(numerator, denominator):
    numerator = (numerator)
    denominator = (denominator)

    try:
        if denominator ==0:
            return ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            return f"The result of the division is {float(numerator / denominator)}"
    except Exception as a:
        return ValueError("Error: Please enter numeric values only.")
        
            



