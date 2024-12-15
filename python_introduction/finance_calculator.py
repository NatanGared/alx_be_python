monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your monthly expense: "))

monthly_savings = float(monthly_income) - float(monthly_expense)

rate = 0.05
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"your monthly savings are ${monthly_savings}")
print(f"Projected savings afterone year, with interest, is: ${Projected_Savings}")
