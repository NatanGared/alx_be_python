def __init__(self):
    pass
def safe_divide(self, numerator, denominator):
    self.numerator = float(numerator)
    self.denominator = float(denominator)

    try:
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            print(float(numerator / denominator))
    except ValueError:
        print("Error: Please enter numeric values only.")
        
            



