Connor Pinkston
Traveling Salesman Problem
General Assembly LA Data Science

This program's dependencies are:
1. csv
2. networkx
3. matplotlib
4. math
5. random
6. sys

There are three algorithms you can use to solve the traveling salesman problem.
1. Random
2. Nearest Neighbor
3. Insertion Heuristic

to run this program you will need to:
1. need to unzip the folder

2. add in any data files (.tsp files) into the folder
	i. The file must have 8 leading lines of comments
	(I had to add in an extra comment line into wi29.tsp
	for the program to run correctly)
	ii. following those lines it must contain data in this 
	order: node number <tab> X Value <tab> Y Value
	iii. the last line must say: EOF
	iv. view sample.tsp for examples

3. Open up the Terminal

4. Navigate to the folder PinkstonTSP

5. type the following to run the program:
	python CpinktonTSP.py (# corresponding to the desired algorithm above) (TSP file)
	
	EX. python CpinkstonTSP.py 2 sample.tsp
	This will run the Nearest Neighbor Algorithm on the sample.tsp file