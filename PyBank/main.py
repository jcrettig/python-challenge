#Import OS and CSV Modules
import os
import csv


# Store file path to budget_data.csv
# Assumes running from following path: C:\Chris\but-ind-data-pt-12-2020-u-c\Week-03-Python\Homework\python-challenge>
csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')

#Define lists
months = []
profit_losses = []
p_l_change = []

#Read using CSV module
with open(csvpath) as csvfile:

    #Specify delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile,delimiter=',')

    #Read header row but exclude from lists
    next(csv_reader)

    #Read each row of data and insert it into the respective list
    for row in csv_reader:
        months.append(row[0])    
        profit_losses.append(int(row[1]))
        #p_l_change.append(int(row[1] + 1))
    
#calculate List of Changes in Profit & Losses
m = len(profit_losses) - 1
p_l_change = [profit_losses[i] - profit_losses[i-1] for i in range(1, len(profit_losses), 1)]

# Calculations:
#------------------------------------------------------------------------------------------------------------------------
#Calculate Total Months                                         Should I use Unique?
Total_Months = (len(months))

#Calculation Net Profits
Net_Profits = sum(profit_losses)

#Calculate Average Change in Profits and Losses
avg_p_l_change = sum(p_l_change) / m

#Calculate the Maximum Change and determine its index
max_change = max(p_l_change)
max_index = p_l_change.index(max_change)

#Determine the index of the related month in the Month list for the Max Change and determine date
max_date_index = max_index + 1
max_date = months[max_date_index]

#Calculate the Minimum Change and determine its index
min_change = min(p_l_change)
min_index = p_l_change.index(min_change)

#Determine the index of the related month in the Month list for the Min Change and determine date
min_date_index = min_index + 1
min_date = months[min_date_index]


#Print to Terminal
#------------------------------------------------------------------------------------------------------------------------
print("Financial Analysis")
print("-----------------------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Net_Profits}")
print(f"Average Change: ${avg_p_l_change:.2f}")
print(f"Greatest Increase in Profits: {max_date} (${max_change})")
print(f"Greatest Decrease in Profits: {min_date} (${min_change})")

#Export to Text File
#------------------------------------------------------------------------------------------------------------------------
csvpath = os.path.join('PyBank', 'Financial_Analysis_Summary.txt')

with open(csvpath,'w') as txt:
    
    txt.writelines("Financial Analysis\n")
    txt.writelines("-----------------------------------------\n")
    txt.writelines(f"Total Months: {Total_Months}\n")
    txt.writelines(f"Total: ${Net_Profits}\n")
    txt.writelines(f"Average Change: ${avg_p_l_change:.2f}\n")
    txt.writelines(f"Greatest Increase in Profits: {max_date} (${max_change})\n")
    txt.writelines(f"Greatest Decrease in Profits: {min_date} (${min_change})\n")