# Personal budget tracker
import csv

income = float(input("Enter your Salary or income: "))
print("Your income is: ",income)

gr_expense = float(input("Enter your groceries expense:"))

water_bill_expense = float(input("Enter your water bill : "))

gas_bill_expense = float(input("Enter your gas bill: "))

electricity_bill_expense = float(input("Enter your electricity bill: "))

rent = float(input("Enter your rents (if have  or write 0): "))

internet_expense = float(input("Enter your internet bill: "))

travel_expense = float(input("Enter your travel expense including monthly transportation or vehical expense"))

entertainment_expense = float(input("Enter your monthly basis entertainment expense:"))

if_other_expense = float(input("Enter sum of other expenses if exist in your life: "))

print("\n")

sum_expenses = gr_expense + water_bill_expense + gas_bill_expense + electricity_bill_expense + rent + internet_expense + travel_expense + entertainment_expense + if_other_expense
print("Sum of all given expenses is: ",sum_expenses)

print("\n")

balance_calc = income - sum_expenses
print("Balance calculation of your given inputs is: ",balance_calc)

print("\n")

budget_tracker = [income, sum_expenses, balance_calc]
with open("budget_tracker.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(budget_tracker)

with open("budget_tracker.csv","r",newline="")as file:
  reader = csv.reader(file)

print("Your data has been saved to budget_tracker.csv")
print("\n")
