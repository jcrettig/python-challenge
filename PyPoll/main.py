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

# Export to textfile
# csvpath = os.path.join('PyPoll', 'Analysis', 'Election_Results_Summary.txt')
# with open(csvpath,'w') as txt:
    
    # txt.writelines("Election Results")
    # txt.writelines("----------------------------")
    # txt.writelines(f"Total Votes: {total_votes}")
    # txt.writelines("----------------------------")

#Create list of unique candidates
candidate_list = set(candidate_column)

#For each candidate in "candidates" find the number of votes the candidate won and store it
candidate_info = {}#Jacob
for candidate_x in candidate_list:
    Number_of_Votes = len([x for x in candidate_column if x == candidate_x])
        
    #Calculate perecent of votes
    canidate_percent = 100 * Number_of_Votes / total_votes


    candidate_info[Number_of_Votes] = (candidate_x, canidate_percent)#Jacob

    #Print to Terminal
    #print(f"{candidate_x}: {canidate_percent}% ({Number_of_Votes})")


votes = list(candidate_info.keys())#Jacob Section
votes.sort()
for key in votes:
    name = candidate_info[key][0]
    percent = candidate_info[key][1]
    numVotes = key
    print(f'{name}: {percent}% ({numVotes})')

    
print("----------------------------")

    #Export to textfile
    # csvpath = os.path.join('PyPoll', 'Analysis', 'Election_Results_Summary.txt')
    # with open(csvpath,'w') as txt:
    # txt.writelines(f"{candidate_x}: {canidate_percent}% ({Number_of_Votes})")
    # txt.writelines("----------------------------")




#print(f"Winner: {Z}")
#print("----------------------------")

#Export to Text File
#------------------------------------------------------------------------------------------------------------------------
# csvpath = os.path.join('PyPoll', 'Analysis', 'Election_Results_Summary.txt')

# with open(csvpath,'w') as txt:
    
    # txt.writelines("Election Results")
    # txt.writelines("----------------------------")
    # txt.writelines(f"Total Votes: {X}")
    # txt.writelines("----------------------------")
    # txt.writelines(f"Kahn: {Y1%}% ({Y1#})")
    # txt.writelines(f"Correy: {Y2%}% ({Y2#})")
    # txt.writelines(f"Li: {Y3%}% ({Y3})")
    # txt.writelines(f"O'Tooley: {Y4%}% ({Y4#})")
    # txt.writelines("----------------------------")
    # txt.writelines(f"Winner: {Z}")
    # txt.writelines("----------------------------")