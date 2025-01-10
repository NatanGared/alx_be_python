import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d")
    print(formatted_datetime)
    return current_date


a = int(input("what is the number of days? "))

def calculate_future_date():
    D = datetime.timedelta(days=a)
    future_date = display_current_datetime()
    formatted_datetime = future_date + D
    print(formatted_datetime.strftime("%Y-%m-%d"))

calculate_future_date()