#Import Module
import os, csv
from pathlib import Path 

#Use Pathlib To Name File Location
input_file = Path("./Resources/budget_data.csv")

#Make Empty Lists 
total_months = []
total_profit = []
monthly_profit_change = []
 
#Open csv
with open(input_file,newline="", encoding="utf-8") as budget:

     #Put Budget_data.csv In csvreader
    csvreader = csv.reader(budget,delimiter=",") 

    #Bypass Header (don't want this included in data)
    header = next(csvreader)  

    #Specify Rows
    for row in csvreader: 

        #Append Total Amount of Months & Profit/Losses
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    #Repeatedly Execute Through Profits To Get Monthly Change
    for i in range(len(total_profit)-1):
        
        #Find Difference Between 2 Months
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
#Calculate The Max/Min of Monthly Profit Change
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

#Associate Max/Min With Proper Month
#+1 month (or next month)
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

#Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

#Output The File
output_file = Path("./Resources/Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    
#What To Print In Financial_Analysis_Summary:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
