import re
import csv
from collections import Counter


def countWords(lines):
	wordDict = {}
	for line in lines:
		line = line[19:]
		wordList = lines.split()
		for word in wordList:
			if word in wordDict: 
				wordDict[word] += 1
			else: 
				wordDict[word] = 1
	return wordDict
	
with open('/Users/CPinkston/Desktop/Python/DS-LA-03/src/lesson01/whispers.csv', 'rb') as csvfile:
	#csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	csvreader = csvfile.read()
	
	wordList = re.findall(r'\w+', csvreader)
	normWords = [word.lower() for word in wordList]
	word_counts = Counter(normWords)
print (word_counts)
