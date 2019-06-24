## 2019-06-23: Rice University Data Anayltics BootCamp | Homework #3 | Python | PyBank

#	In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
#   You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. 
#   (Thankfully, your company has rather lax standards for accounting so the records are simple.)
#	 
#	Your task is to create a Python script that analyzes the records to calculate each of the following:
#	
#	The total number of months included in the dataset
#	The net total amount of "Profit/Losses" over the entire period
#	The average of the changes in "Profit/Losses" over the entire period
#	The greatest increase in profits (date and amount) over the entire period
#	The greatest decrease in losses (date and amount) over the entire period
#	
#	As an example, your analysis should look similar to the one below:
#	
#	  Financial Analysis
#	  ----------------------------
#	  Total Months: 86
#	  Total: $38382578
#	  Average  Change: $-2315.12
#	  Greatest Increase in Profits: Feb-2012 ($1926159)
#	  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#	
#	In addition, your final script should both print the analysis to the terminal and export a text file with the results.
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
# ===========================================================================================================================
# ===========================================================================================================================
#
#
#   +++++++++++++++++++++++++
#	+++ Interesting Read +++
#   +++++++++++++++++++++++++
#
#    Link : https://stackoverflow.com/questions/16108526/count-how-many-lines-are-in-a-csv-python
#
#
#############################################################################################################################

import os
import csv
import datetime

csvpath = os.path.join('python-challenge\PyBank', 'Resources', 'budget_data.csv')
os.system('cls')

### Your task is to create a Python script that analyzes the records to calculate each of the following:

### The total number of months included in the dataset
### The net total amount of "Profit/Losses" over the entire period
### The average of the changes in "Profit/Losses" over the entire period
### The greatest increase in profits (date and amount) over the entire period
### The greatest decrease in losses (date and amount) over the entire period

def financial_analysis (financial_data):
    #totalnumbermonths = str(financial_data[0])
    #totalnumbermonths = csvreader.line_num-1
    #nettotalamount = float(financial_data[1])
    
    avgchanges = int()
    #greatestincrease = int()
    #greatestdecrease = int()  
    # 
nettotalamount = 0.00 

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        totalnumbermonths = len(list(csvreader))
        nettotalamount += float(row[1])
        print(row)


# reader_file = csv.reader(input_file)
# value = len(list(reader_file))  
  

os.system('cls')
    #for x in range(1,101,2):
      #  print(f"=== Calculating Financial Analysis {str(x)}% ===")
     #   os.system('cls')
now = datetime.datetime.now()

print("============================") 
print(f"==== Financial Analysis ==== ( Generated on: {str(now)} )")
print("====================================================================================") 
    
    # Print out Total Number of rows / months -1 for the header.
print(f"Total Months: {str(totalnumbermonths)}")
print(f"Total: ${str(nettotalamount)}")
    #print('The total is {}'.format(total))
print(f"PRINT ROWS:{str(row[1])}")


####################################################################


    
