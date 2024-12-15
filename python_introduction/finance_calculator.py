monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expense: "))

monthly_savings = float(monthly_income) - float(monthly_expenses)

rate = 0.05
Projected_Savings = float(monthly_savings) * 12 + (float(monthly_savings) * 12 * 0.05)

print(f"your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${Projected_Savings}")
