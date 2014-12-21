from datetime import datetime
import csv

fileCopy = []

# Printing out each row in order to show what is there
with open("exampleData.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter = ",")
	for row in reader:
		fileCopy.append(row)

csvfile.close()

# print fileCopy

tickerNames = []
tickerNamesCounter = 0


# Isolate the ticker names into the tickerNames list
for x in fileCopy[0]:
	if x == '':
	    pass
	else:
	    tickerNames.append(x)

# Verify that ticker names are transferred to the list
# print tickerNames

# Pair dates and ticker names into a double dictionary structure
indexCounterStart = 2
valueCounter = 0

# All available dates
dates1 = []
dates2 = []

# Dictionaries
dateToValue1 = {}
dateToValue2 = {}

# Start reading in dates from 2nd row on
for x in fileCopy[2:]:
        if(x[0] != ''):
            date_1 = datetime.strptime(x[0], '%m/%d/%Y')
	    dates1.append(date_1)
            dateToValue1[date_1.strftime('%m-%d-%Y')] = x[1]
        if(x[3] != ''):    
            date_2 = datetime.strptime(x[3], '%m/%d/%Y')
	    dates2.append(date_2)
	    dateToValue2[date_2.strftime('%m-%d-%Y')] = x[4]

# Check to make sure that everything works
# print dates1,
# print ""
#print dates2,

# TODO: Find the earliest overlapping date between the two sets of lists
if dates1[0] < dates2[0]:
    #The first date in the dates1 list is earlier than the other, so earliest overlapping
    #   date must be dates2 first value
    #   This is of course assuming Bloomberg data is complete for each date
    earliest_date = dates2[0].strftime('%m-%d-%Y')
else:
    earliest_date = dates1[0].strftime('%m-%d-%Y')

print "earliest date: " + str(earliest_date)
# TODO: Objective 1: isolate the dates and values for each of the corresponding lists
# *Remember that each list has its own set of values, and is independent
#  from any other list.

