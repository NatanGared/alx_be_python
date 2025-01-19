def safe_divide(numerator, denominator):
    numerator = float(numerator)
    denominator = float(denominator)

    try:
        if ZeroDivisionError:
            raise "Error: Cannot divide by zero."
        else:
            return f"The result of the division is {float(numerator / denominator)}"
    except ValueError:
        return "Error: Please enter numeric values only."
        
            



