#Import OS and CSV Modules
import os
import csv

# Store file path to election_data.csv
# Assumes running from following path: C:\Chris\but-ind-data-pt-12-2020-u-c\Week-03-Python\Homework\python-challenge>
csvpath = os.path.join('PyPoll','Resources', 'election_data.csv')

#Read using CSV module
with open(csvpath) as csvfile:

    #Specify delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile,delimiter=',')

    #Create ZipList from election_data.csv 
    elect_data_zl = list(zip(*csv_reader))
    
    #Pull out column 0 and take off header
    voter_id = elect_data_zl[0][1:]       

    #Change all of the contents in column 0 from strings to integers
    voter_id_column = [int(row) for row in voter_id]
    
    #Pull out columns 1 and 2 and take off header
    county_column = elect_data_zl[1][1:]
    candidate_column = elect_data_zl[2][1:]
    
# Calculations and Output Setup:
#------------------------------------------------------------------------------------------------------------------------
#Calculate Total Votes                                         
total_votes = (len(voter_id_column))

#Print to Terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")

#Print to Text File
csvpath = os.path.join('PyPoll', 'Analysis', 'Election_Results_Summary.txt')

with open(csvpath,'w') as txt:
    
    txt.writelines("Election Results\n")
    txt.writelines("----------------------------\n")
    txt.writelines(f"Total Votes: {total_votes}\n")
    txt.writelines("----------------------------\n")

    #Determine who are the unique candidates
    candidate_list = set(candidate_column)

    #Create Dictionary infrastructure and identify number_of_votes and the key
    candidate_info = {}
    for candidate_x in candidate_list:
        number_of_votes = len([x for x in candidate_column if x == candidate_x])
            
        #Calculate perecent of votes
        canidate_percent = 100 * number_of_votes / total_votes

        #Insert components of dictionary consisting of number_of_votes, candidate_x and candidate_percent
        candidate_info[number_of_votes] = (candidate_x, canidate_percent)

    #Create a list from the "candidate_info" dictionary of the keys
    votes = list(candidate_info.keys())

    #sort keys (votes) in decending order
    votes.sort(reverse=True)
    # pull data from dictionary to print
    for key in votes:
        value = candidate_info[key]
        name = value[0]
        percent = value[1]
        numVotes = key
        
        #Print to Terminal
        print(f'{name}: {percent:.3f}% ({numVotes})')  

        #Print to Text File            
        txt.writelines(f'{name}: {percent:.3f}% ({numVotes})\n')

    #Identify  maximum votes(key)
    winner_key = max(votes)

    #pull name of winner based on key
    winner = candidate_info[winner_key][0]

    #Print to Terminal
    print("----------------------------")
    print(f'Winner: {winner}')
    print("----------------------------")

    #Print to Text File            
    txt.writelines("----------------------------\n")
    txt.writelines(f'Winner: {winner}\n')
    txt.writelines("----------------------------\n")
