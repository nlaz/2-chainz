from __future__ import print_function
import random

dict = {}
starting_words = []
input_file = open('fox-in-socks.txt', 'r')
words = input_file.read().split() #note that split without arguments splits on whitespace
for i in range(len(words)-1):
	pair = words[i]+' '+words[i+1]
	if pair[0].isupper():
		starting_words.append(pair)
	# print pair
	if i < len(words)-2: 
		value = words[i+2]
		# print value
		if pair not in dict: 
			dict[pair] = [value]
		else:
			dict[pair].append(value)
# print dict
	# for word in words:
for i in range(4):
	print()
	current_pair = random.choice(starting_words)
	print(current_pair, end=' ')
	while current_pair in dict:
		next_word = random.choice(dict[current_pair])
		print(next_word, end=' ')
		# print '['+ current_pair +'] ->'+ next_word
		comp = current_pair.split()
		current_pair = comp[1]+ ' '+next_word
		if ('?' in current_pair) or ("!" in current_pair) or ("." in current_pair):
			break


