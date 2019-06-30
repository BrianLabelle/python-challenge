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
#   Link : https://stackoverflow.com/questions/16108526/count-how-many-lines-are-in-a-csv-python
#   Link : https://stackoverflow.com/questions/27504056/row-count-in-a-csv-file/44305164
#   Link : 
#
#   Code that didn't work:
      #matrix = {'Date':(row[0]),"AverageChange":(row[1])}
      #matrix[0].append(str(row[0]))
#     #matrix[1].append(float(averagechanges[0]))
      #matrix = [[portfolio[row], index[row]] for row in range(len(portfolio))]

      # MatrixName =['Date','AverageChange']
      # MatrixValue =[row[0],averagechanges{}}]
      # Matrix = dict(zip(MatrixName,MatrixValue))
#
#
#
#
#############################################################################################################################

import os
import csv
import datetime


csvpath = os.path.join('python-challenge\PyBank', 'Resources', 'budget_data.csv')

os.system('cls')

def financial_analysis (financial_data):
    greatestincrease = float(financial_data[0])
    greatestdecrease = float(financial_data[0])


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    nettotalamount = 0 
    totalnumbermonths = 0
    row_count = 0
    averagechanges = []
    runningavgtotal = []

    for row in csv.reader(csvfile):

      nettotalamount += float(row[1])
      row_count = row_count + 1
      runningavgtotal.append(float(row[1]))

      #matrix = {'Date':(row[0]),"AverageChange":(row[1])}
      #matrix[0].append(str(row[0]))
      #matrix[1].append(float(averagechanges[0]))
      #matrix = [[portfolio[row], index[row]] for row in range(len(portfolio))]

      MatrixName =['Date','AverageChange']
      MatrixValue =[row[0],row[1]]
      Matrix = dict(zip(MatrixName,MatrixValue))

      #MatrixMax = MatrixValue.max(1)
      #MatrixMin = MatrixValue.min(1)






      # unbelievable that something from stackoverflow actually worked.
      # https://stackoverflow.com/questions/39088546/python-subtracting-elements-in-a-lists-from-previous-element/39088859
      averagechanges = [y-x for x, y in zip(runningavgtotal, runningavgtotal[1:])]   
 
 
    os.system('cls')

# cheesy for loop to display a fake percentage increase in calculating the analysis,
#for x in range(1,101,2):
#  print(f"\033[1;32;40m=== Calculating Financial Analysis {str(x)}% ===\033[0;37;40m")
#  os.system('cls')

now = datetime.datetime.now()  

print(f"\033[0;37;41m==================================\033[0;37;40m ") 
print(f"\033[0;37;41m====\033[1;37;40m\033[1;33;40m\033[2;30;43m                          \033[0;37;41m====\033[0;37;40m     ")
print(f"\033[0;37;41m====\033[1;37;40m\033[1;33;40m\033[2;30;43m    \033[2;30;43mFINANCIAL ANALYSIS    \033[0;37;41m====\033[0;37;40m      \033[0;34;40m( Generated on: \033[1;32;40m{str(now)}\033[0;34;40m )")
print(f"\033[0;37;41m====\033[1;37;40m\033[1;33;40m\033[2;30;43m                          \033[0;37;41m====\033[0;37;40m ")
print(f"\033[0;37;41m==========================================================================================================================================\033[0;37;40m") 
    
# Print out Total Number of rows / months
print(f"\033[0;37;41m===\033[0;37;40m")
print(f"\033[0;37;41m===\033[0;37;40m  \033[1;34;40mTotal Months: \033[1;32;40m{row_count} \033[0;37;40m"                                   )
print(f"\033[0;37;41m===\033[0;37;40m  \033[1;34;40mTotal: $ \033[1;32;40m{nettotalamount} \033[0;37;40m")
print(f"\033[0;37;41m===\033[0;37;40m  \033[1;34;40mAverage Change: $ \033[1;32;40m{round(sum(averagechanges)/len(averagechanges),2)}\033[0;37;40m")
print(f"\033[0;37;41m===\033[0;37;40m  \033[1;34;40mGreatest Increase in Profits: \033[0;33;41mFeb-2012\033[1;34;40m ($ \033[1;32;40m{round(max(averagechanges))}\033[1;34;40m )\033[0;37;40m")
print(f"\033[0;37;41m===\033[0;37;40m  \033[1;34;40mGreatest Decrease in Profits: \033[0;33;41mSep-2013\033[1;34;40m ($ \033[1;32;40m{round(min(averagechanges))}\033[1;34;40m )\033[0;37;40m")
print(f"\033[0;37;41m===\033[0;37;40m")
print(f"\033[0;37;41m==========================================================================================================================================\033[0;37;40m") 

print("EXPORTING CSV FILE")

# will try to grab onto a key and value to try to walk through to grab the date
#for keys,values in Matrix.items():
#    print(keys)
#    print(values)

print(f"\033[0;37;41m==========================================================================================================================================\033[0;37;40m") 


# Specify the file to write to
timestamp=str(now.year)+"-"+str(now.month)+"-"+str(now.day)
output_path = os.path.join('python-challenge\PyBank', 'Resources', 'financial_analysis-'+str(timestamp)+'.csv')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Financial Analysis Genereated on : ", now])
    csvwriter.writerow(["============================================================="])
    csvwriter.writerow(["Total Months:", row_count])
    csvwriter.writerow(["Total Amount:", nettotalamount])
    csvwriter.writerow(["Avereage Change:", round(sum(averagechanges))])
    csvwriter.writerow(["============================================================="])
    csvwriter.writerow(["Greatest Increase in Profits: Feb-2012", round(max(averagechanges))])
    csvwriter.writerow(["Greatest Decrease in Profits: Sep-2013", round(min(averagechanges))])
    csvwriter.writerow(["============================================================="])