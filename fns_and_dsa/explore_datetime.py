from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return current_date

print(f"Current date and time: {display_current_datetime()}")

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    D = timedelta(days=number_of_days)
    future = display_current_datetime()
    future_date = future + D
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

calculate_future_date()