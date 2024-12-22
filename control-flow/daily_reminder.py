Task = input("Enter your task: ")
Time_Bound = input("Is it time bound? (yes/no): ")
Priority = input("Priority (high/medium/low): ")

match Priority:
    case "high":
        result = "high priority"
    case "medium":
        result = "medium priority"
    case "low":
        result = "low priority"
    case _:
        print("Input a proper priority level")
if Time_Bound == "yes":
    print(f"Reminder: '{Task}' ia a {result} task that requires immediate attention today!")
elif Time_Bound == "no":
    print(f"Note: '{Task}' ia a {result} task. consider completing it when you have free time")
else:
    print("Kindly insert a proper answer")