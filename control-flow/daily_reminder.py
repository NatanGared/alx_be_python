task = input("Enter your task: ")
priority = input("(high/medium/low): ")
time_bound = input("Is it time bound? (yes/no): ")

match priority:
    case "high":
        result = "high priority"
    case "medium":
        result = "medium priority"
    case "low":
        result = "low priority"
    case _:
        print("Input a proper priority level")
if time_bound == "yes":
    print(f"'{task}' ia a {result} task that requires immediate attention today!")
elif time_bound == "no":
    print(f"'{task}' ia a {result} task. consider completing it when you have free time")
else:
    print("Kindly insert a proper answer")