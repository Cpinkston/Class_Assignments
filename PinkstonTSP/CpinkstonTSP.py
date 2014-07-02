#Connor Pinkston Traveling Salesman Problem
import csv
import networkx as nx
import matplotlib.pyplot as plt
import math
import random
import sys


count = 0
coordinates = []
graph = nx.Graph()
totalDistance = 0
algorithmType = sys.argv[1]
fileName = sys.argv[2]
		
def tripDistance(list):
	totalDistance = 0.0
	for i in range(0,len(list)):
		distance = math.sqrt((float(list[i-1][1]) - float(list[i][1]))**2 + (float(list[i-1][2]) - float(list[i][2]))**2)
		totalDistance += distance
	return totalDistance

#Open the file and put the data into a list
#with open('wi29.tsp', 'rb') as corrdinateFile:
with open(fileName, 'rb') as corrdinateFile:
	tspReader = csv.reader(corrdinateFile, delimiter=' ', quotechar='|')
	for row in tspReader:
		if count > 7:
			coordinates.append(row)
		count += 1

#delete the last entry that is end of file		
del coordinates[-1]

#Random Search Algorithm
if algorithmType == '1':	
	#Shuffle the list
	random.shuffle(coordinates)

	#re-order the stop numbers
	for i in range(0,len(coordinates)):
		coordinates[i][0] = i + 1

#Nearest Neighbor Algorithm
if algorithmType == '2':
	neighborList = []
	tempDistance = None
	currentDistance = None
	nearestName = None
	
	#Add a boolean to track if a point has been used
	for i in range(0,len(coordinates)):
		coordinates[i].append(False)
		
	#Add in the first point as the starting point
	neighborList.append(coordinates[0])
	coordinates[0][3] = True
	
	#Append the next nearest coordinate point
	for i in range(0,len(coordinates)-1):
		currentDistance = 10000000000.0
		for x in range(0,len(coordinates)):
			if coordinates[x][3] == False:
				tempDistance = math.sqrt((float(neighborList[i][1]) - float(coordinates[x][1]))**2 + (float(neighborList[i][2]) - float(coordinates[x][2]))**2)
				if tempDistance < currentDistance:
					nearestName = int(coordinates[x][0]) - 1
					currentDistance = tempDistance
		coordinates[int(nearestName)][3] = True
		neighborList.append(coordinates[int(nearestName)])	
	#re-order the stop numbers
	for i in range(0,len(neighborList)):
		neighborList[i][0] = i + 1
	coordinates = neighborList	

#Insertion Hueristic
if algorithmType == '3':
	
	#Setup
	selectedCities = []
	unselectedCities = []
	selectedCities.append(coordinates[0])
	for x in range(1,len(coordinates)):
		selectedCities.append(coordinates[x])
		
	bestCity = None
	bestCityIndex = None
	minDistance = None
	
	#Algorithm
	while len(unselectedCities) > 0:
		selectedCities.insert(0,unselectedCities[0])
		minDistance = tripDistance(selectedCities)
		bestCity = unselectedCities[0]
		bestCityIndex = 0
		selectedCities.remove(0)
		
		#Go through all insertions
		for i in range(0,len(unselectedCities)):
			for j in range(0,len(selectedCities)):
				selectedCities.insert(j,unselectedCities[i])
				distance = tripDistance(selectedCities)
				if distance < minDistance:
					minDistance = distance
					bestCity = unselectedCities[i]
					bestCityIndex = j
	 			selectedCities.remove(j)
	 	selectedCities.insert(bestCityIndex,bestCity)
	 	unselectedCities.Remove(unselectedCities.index(bestCity))
	 	
	#Add in the new path 	
	coordinates = selectedCities


#graph the points in the graph
for entrys in coordinates:
	graph.add_node(entrys[0], pos = (float(entrys[1]),float(entrys[2])))


#add in the edges between the points and calculate the distance
for i in range(0,len(coordinates)):
	graph.add_edge(coordinates[i-1][0], coordinates[i][0])
	distance = math.sqrt((float(coordinates[i-1][1]) - float(coordinates[i][1]))**2 + (float(coordinates[i-1][2]) - float(coordinates[i][2]))**2)
	totalDistance += distance


print "The total distance of the trip is: %i" %(totalDistance)
	
	
pos = nx.get_node_attributes(graph,'pos')	
	
nx.draw(graph,pos = pos, with_labels = True)
plt.show()	
	

