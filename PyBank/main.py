#Import OS and CSV Modules
import os
import csv

# Store file path to budget_data.csv
# Assumes running from following path: C:\Chris\but-ind-data-pt-12-2020-u-c\Week-03-Python\Homework\python-challenge>
csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')

#Define lists
months = []
profit_losses = []

#Read using CSV module
with open(csvpath) as csvfile:

    #Specify delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile,delimiter=',')

    #Read header row but exclude from lists
    next(csv_reader)

    #Read each row of data and insert it into the respective list
    for row in csv_reader:
        months.append(row[0])    
        profit_losses.append(row[1])
    
print(months)
print(profit_losses)



