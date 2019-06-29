## 2019-06-23: Rice University Data Anayltics BootCamp | Homework #3 | Python | PyRoll
#	In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
#	
#	You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#	
#	 
#	The total number of votes cast
#	A complete list of candidates who received votes
#	The percentage of votes each candidate won
#	The total number of votes each candidate won
#	The winner of the election based on popular vote.
#	
#	
#	As an example, your analysis should look similar to the one below:
#	
#	
#	  Election Results
#	  -------------------------
#	  Total Votes: 3521001
#	  -------------------------
#	  Khan: 63.000% (2218231)
#	  Correy: 20.000% (704200)
#	  Li: 14.000% (492940)
#	  O'Tooley: 3.000% (105630)
#	  -------------------------
#	  Winner: Khan
#	  -------------------------
#	
#	In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#	
#	
#	
#	
#   ++++++++++++++++++++++++++++++++
#	+++ Hints and Considerations +++
#   ++++++++++++++++++++++++++++++++
#	
#	Consider what we've learned so far. To date, we've learned how to import modules like csv; to read and write files in 
# various formats; to store contents in variables, lists, and dictionaries; to iterate through basic data structures; and 
# to debug along the way. Using what we've learned, try to break down you tasks into discrete mini-objectives. This will be
#  a much better course of action than attempting to Google Search for a miracle.

#	As you will discover, for some of these challenges, the datasets are quite large. This was done purposefully, as it 
# showcases one of the limits of Excel-based analysis. While our first instinct, as data analysts, is often to head straight 
# into Excel, creating scripts in Python can provide us with more robust options for handling "big data".

#	Your scripts should work for each dataset provided. Run your script for each dataset separately to make sure that the 
# code works for different data.

#	Feel encouraged to work in groups, but don't shortchange yourself by copying someone else's work. You get what you put in, 
# and the art of programming is extremely unforgiving to moochers. Dig your heels in, burn the night oil, and learn this while 
# you can! These are skills that will pay dividends in your future career.
#	Start early, and reach out for help often! Challenge yourself to identify specific questions for your instructors and TAs. 
# Don't resign yourself to simply saying, "I'm totally lost." Come prepared to show your effort and thought patterns, we'll be 
# happy to help along the way.
#	
#	Always commit your work and back it up with GitHub pushes. You don't want to lose hours of your work because you didn't 
# push it to GitHub every half hour or so.
#
#
# Help Link: https://realpython.com/iterate-through-dictionary-python/
# Help Link: https://docs.python.org/3/library/collections.html#collections.Counter
# Help Link: https://realpython.com/iterate-through-dictionary-python/
# Help Link: https://www.tutorialspoint.com/python3/python_dictionary.htm
# Help Link: https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/
#	
# ===========================================================================================================================
# ===========================================================================================================================


import os
import csv
import datetime

csvpath = os.path.join('python-challenge\PyPoll', 'Resources', 'election_data_sample.csv')

os.system('cls')

def election_results (voting_results):
    greatestincrease = float(voting_results[0])
    greatestdecrease = float(voting_results[0])


with open(csvpath, newline='') as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=',')
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    row_count = 0

    
    voting_results = csv.DictReader(csvfile)

    election_results = {voting_results}
    for row in voting_results:
      print(dict(row))
  

      


# now = datetime.datetime.now()  

# print(f"\033[0;37;41m==================================\033[0;37;40m ") 
# print(f"\033[0;37;41m====\033[1;37;40m\033[1;33;40m\033[2;30;43m                          \033[0;37;41m====\033[0;37;40m     ")
# print(f"\033[0;37;41m====\033[1;37;40m\033[1;33;40m\033[2;30;43m    \033[2;30;43mELECTION RESULTS      \033[0;37;41m====\033[0;37;40m      \033[0;34;40m( Generated on: \033[1;32;40m{str(now)}\033[0;34;40m )")
# print(f"\033[0;37;41m====\033[1;37;40m\033[1;33;40m\033[2;30;43m                          \033[0;37;41m====\033[0;37;40m ")
# print(f"\033[0;37;41m==========================================================================================================================================\033[0;37;40m") 
    
# # Print out Total Number of rows / months
# print(f"\033[0;37;41m===\033[0;37;40m")

# print(f"\033[0;37;41m===\033[0;37;40m  \033[1;34;40mTotal Votes: \033[1;32;40m{row_count} \033[0;37;40m")
# print(f"\033[0;37;41m===\033[0;37;40m  \033[1;34;40m\033[0;37;40m---------------------------")
# print(f"\033[0;37;41m===\033[0;37;40m  \033[1;34;40m\033[0;37;40mCandidate #1: \033[0;33;41m63% ( 2219231 )\033[1;34;40m")
# print(f"\033[0;37;41m===\033[0;37;40m  \033[1;34;40m\033[0;37;40mCandidate #2: \033[0;33;41m63% ( 2219231 )\033[1;34;40m")
# print(f"\033[0;37;41m===\033[0;37;40m  \033[1;34;40m\033[0;37;40mCandidate #3: \033[0;33;41m63% ( 2219231 )\033[1;34;40m")
# print(f"\033[0;37;41m===\033[0;37;40m  \033[1;34;40m\033[0;37;40mCandidate #4: \033[0;33;41m63% ( 2219231 )\033[1;34;40m")
# print(f"\033[0;37;41m===\033[0;37;40m  \033[1;34;40m\033[0;37;40mCandidate #5: \033[0;33;41m63% ( 2219231 )\033[1;34;40m")
# print(f"\033[0;37;41m===\033[0;37;40m  \033[1;34;40m\033[0;37;40m---------------------------")
# print(f"\033[0;37;41m===\033[0;37;40m  \033[1;34;40m\033[0;37;40mWinner: \033[0;33;41mChaka Khan\033[1;34;40m")
# print(f"\033[0;37;41m===\033[0;37;40m  \033[1;34;40m\033[0;37;40m---------------------------")
# print(f"\033[0;37;41m===\033[0;37;40m")
# print(f"\033[0;37;41m==========================================================================================================================================\033[0;37;40m") 
#print("In addition, your final script should both print the analysis to the terminal and export a text file with the results.")

