
import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d")
    return current_date

print(f"Current date and time: {display_current_datetime()}")

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    D = datetime.timedelta(days=number_of_days)
    future_date = display_current_datetime()
    formatted_datetime = future_date + D
    print(f"Future date: {formatted_datetime.strftime("%Y-%m-%d")}")

calculate_future_date()