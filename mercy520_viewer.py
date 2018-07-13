import csv
from collections import defaultdict
import sqlite3
import sys

#build query for choice of records
#query="SELECT id, QB, RB1, RB2, WR1, WR2, WR3, TE, Flex, DST, corrScore, homeScore, spreadScore, totalScore, totalCost, projPts from LINEUP WHERE id > 2334 AND corrScore > .3 AND QB= 'Cam Newton' "

query="SELECT id, QB, RB1, RB2, WR1, WR2, WR3, TE, Flex, DST, corrScore, homeScore, spreadScore, totalScore, totalCost, projPts from LINEUP WHERE id > 3554 AND projPts > 125 AND corrScore > 0"

#connect to db
conn = sqlite3.connect('/root/Desktop/mercy520/lineup.db')
print "opened db"


#initialize a count variable 
count = 0

#execute query 
cursor = conn.execute(query)

#print rows
for row in cursor:
	print ("ID = %s")%(row[0])
	print ("QB = %s")%(row[1])
	print ("RB1 = %s")%(row[2])
	print ("RB2 = %s")%(row[3])
	print ("WR1 = %s")%(row[4])
	print ("WR2 = %s")%(row[5])
	print ("WR3 = %s")%(row[6])
	print ("TE = %s")%(row[7])
	print ("Flex = %s")%(row[8])
	print ("DST = %s")%(row[9])
	print ("corrScore = %s")%(row[10])
	print ("homeScore = %s")%(row[11])
	print ("spreadScore = %s")%(row[12])
	print ("totalScore = %s")%(row[13])
	print ("totalSalary = %s")%(row[14])
	print ("projPts = %s")%(row[15])
	print"*******************************"
	print"*******************************"
	print"*******************************"
        #increment count variable for each row
	count = count + 1

#print total number of records for selected criteria  
print (count)
#close db connection
conn.close()








