Code Purpose:
Using the PyPoll csv file, create an analysis of Towns voting data to summarize the voting results in total and by candidate

Code Description:
1) Imported the data from a CSV file (election_data.csv) using the OS and CSV modules
2) The file was located at C:\Chris\but-ind-data-pt-12-2020-u-c\Week-03-Python\Homework\python-challenge\PyPoll\Resources
3) Using the data from the election_data.csv, created a zip list with 3 columns - 1) voter id, 2) county and candidate
4) Computed the total number of votes based on a count (length of list) of the voter ID column
5) Determined the name of all candiates that had votes by creating a set
6) Created the infrastructure for a dictionary using the total number of votes each candidate received as the key
	a) Calculated the of percent of votes each candidate received 
	b) inserted the candidates and the percent of votes each candidate received into the dictionary
7) Using a list of the dictionary keys
	a) sorted the keys in decending order
	b) pulled data from the dictionary to be printed
8) Determined the maximum dictionary key and used this to determine the winning candicate
9) Printed to the Terminal and to the Text file a summary of the results of the election
	a) Total votes
	b) Each candidates percent and number of votes
	c) Name of the winner


