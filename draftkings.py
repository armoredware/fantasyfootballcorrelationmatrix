import csv
from collections import defaultdict
import sqlite3
import sys

#query="SELECT id, QB, RB1, RB2, WR1, WR2, WR3, TE, Flex, DST, corrScore, homeScore, spreadScore, totalScore, totalCost, projPts from LINEUP"
# GROUP BY QB ---sql
#query="SELECT id, QB, RB1, RB2, WR1, WR2, WR3, TE, Flex, DST, corrScore, homeScore, spreadScore, totalScore, totalCost, projPts from LINEUP WHERE corrScore >= '0.30' AND DST LIKE 'Patriots' OR corrScore >= '0.30' AND DST LIKE 'Chiefs'"

#query="SELECT id, QB, RB1, RB2, WR1, WR2, WR3, TE, Flex, DST, corrScore, homeScore, spreadScore, totalScore, totalCost, projPts from LINEUP WHERE corrScore >= '0.2' AND QB like 'Aaron%'"

query="SELECT id, QB, RB1, RB2, WR1, WR2, WR3, TE, Flex, DST, corrScore, homeScore, spreadScore, totalScore, totalCost, projPts from LINEUP WHERE id > 3554 AND projPts > 120 AND corrScore > 0"


#query="SELECT id, QB, RB1, RB2, WR1, WR2, WR3, TE, Flex, DST, corrScore, homeScore, spreadScore, totalScore, totalCost, projPts from LINEUP WHERE id > 2474 AND corrScore > .39 AND projPts > 138"

#query="SELECT id, QB, RB1, RB2, WR1, WR2, WR3, TE, Flex, DST, corrScore, homeScore, spreadScore, totalScore, totalCost, projPts from LINEUP WHERE corrScore >= '1.0'"

#query="SELECT id, QB, RB1, RB2, WR1, WR2, WR3, TE, Flex, DST, corrScore, homeScore, spreadScore, totalScore, totalCost, projPts from LINEUP WHERE corrScore >= '0.7'"

conn = sqlite3.connect('/root/Desktop/mercy520/lineup.db')
#conn = sqlite3.connect('/root/Desktop/ga/py/lineup.db')
print "QB,RB,RB,WR,WR,WR,TE,FLEX,DST"

count = 0
cursor = conn.execute(query)
for row in cursor:
	#print ("ID = %s")%(row[0])
	print ("%s,%s,%s,%s,%s,%s,%s,%s,%s")%(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
	#print ("RB1 = %s")%(row[2])
	#print ("RB2 = %s")%(row[3])
	#print ("WR1 = %s")%(row[4])
	#print ("WR2 = %s")%(row[5])
	#print ("WR3 = %s")%(row[6])
	#print ("TE = %s")%(row[7])
	#print ("Flex = %s")%(row[8])
	#print ("DST = %s")%(row[9])
	#print ("corrScore = %s")%(row[10])
	#print ("homeScore = %s")%(row[11])
	#print ("spreadScore = %s")%(row[12])
	#print ("totalScore = %s")%(row[13])
	#print ("totalSalary = %s")%(row[14])
	#print ("projPts = %s")%(row[15])
	#print"*******************************"
	#print"*******************************"
	#print"*******************************"
	count = count + 1


print (count)
conn.close()

'''
def view_lineup(query):
	conn = sqlite3.connect('lineup.db')
	print ("Opened database successfully")
	cursor = conn.execute( query )
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
	       	print ("projPts = %s")%(row[14])

	conn.close()
'''

#query="SELECT id, QB, RB1, RB2, WR1, WR2, WR3, TE, Flex, DST, corrScore, homeScore, spreadScore, totalScore, totalCost, projPts from LINEUP"  
#query="SELECT * from LINEUP"
#view_lineup(query)





