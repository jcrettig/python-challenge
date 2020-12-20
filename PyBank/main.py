#Import OS and CSV Modules
import os
import csv

# Store file path to budget_data.csv
# Assumes running from following path: C:\Chris\but-ind-data-pt-12-2020-u-c\Week-03-Python\Homework\python-challenge>
csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')

#Read using CSV module
with open(csvpath) as csvfile:

    #Specify delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter=',')

    print(csvreader)
