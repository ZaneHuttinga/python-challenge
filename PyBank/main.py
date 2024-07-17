# Import modules
import pandas as pd
import csv

# Load dataset from CSV file
BudgetData = pd.read_csv("~/python-challenge/PyBank/Resources/budget_data.csv")



# Define stats

# Pull out second column of data set
ProfitLosses = BudgetData['Profit/Losses']

# Basic stats
months = len(ProfitLosses)
net = sum(ProfitLosses)

# Monthly changes
changes = []
dates = []
for i in range (months-1):
    dates.append(BudgetData['Date'][i+1])
    j = ProfitLosses[i+1] - ProfitLosses[i]
    changes.append(j)

avg = sum(changes)/len(changes)
increase = max(changes)
decrease = min(changes)

# Find dates for greatest increase and decrease
inc_index = changes.index(increase)
inc_date = dates[inc_index]
dec_index = changes.index(decrease)
dec_date = dates[dec_index]

# Print analysis in terminal
print("\nFinancial Analysis\n")
print("----------------------------\n")
# Print number of months
print(f"Total Months: {months}\n")
# Print total change
print(f"Total: ${net}\n")
# Print average change
print(f"Average Change: ${avg:.2f}\n")
# Print greatest increase
print(f"Greatest Increase in Profits: {inc_date} (${increase})\n")
# Print greatest decrease
print(f"Greatest Decrease in Profits: {dec_date} (${decrease})\n")

# Print analysis in file
with open("python-challenge/PyBank/Analysis/PyBank.txt", "w") as f:
    print("Financial Analysis\n", file=f)
    print("----------------------------\n", file=f)
    # Print number of months
    print(f"Total Months: {months}\n", file=f)
    # Print total change
    print(f"Total: ${net}\n", file=f)
    # Print average change
    print(f"Average Change: ${avg:.2f}\n", file=f)
    # Print greatest increase
    print(f"Greatest Increase in Profits: {inc_date} (${increase})\n", file=f)
    # Print greatest decrease
    print(f"Greatest Decrease in Profits: {dec_date} (${decrease})\n", file=f)