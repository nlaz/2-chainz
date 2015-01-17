from __future__ import print_function
import random

dict = {}
def readInFile(file):
	input_file = open(file, 'r')
	words = input_file.read().rsplit() #note that split without arguments splits on whitespace
	for i in range(len(words)-1):
		pair = words[i]+' '+words[i+1]
		if i < len(words)-2: 
			value = words[i+2]
			if pair not in dict: 
				dict[pair] = [value]
			else:
				dict[pair].append(value)

def printNumLine(numLines):
	lineCount = 0
	while lineCount < numLines:
		current_pair = random.choice(dict.keys())
		print(current_pair.capitalize(), end=' ')
		# print(current_pair.capitalize())
		count = 0
		while current_pair in dict and lineCount < numLines:
			next_word = random.choice(dict[current_pair])
			print(next_word, end=' ')
			# print('['+ current_pair +'] ->'+ next_word)
			comp = current_pair.split()
			current_pair = comp[1]+ ' '+next_word
			count += 1
			if count >= 6:
				lineCount += 1
				count = 0
				print()
		lineCount += 1
		print()

def loadSeuss():
	readInFile('fox-in-socks.txt')
	readInFile('cat-in-the-hat.txt')
	readInFile('green-eggs-and-ham.txt')
	readInFile('one-fish-two-fish.txt')

def loadGambino():
	readInFile('freaks-and-geeks.txt')
	readInFile('bonfire.txt')

loadSeuss()
loadGambino()

printNumLine(5)



