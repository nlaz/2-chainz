from __future__ import print_function
from flask import Flask, render_template, request
import requests
import random
import os

app = Flask(__name__)
app.config["DEBUG"] = True  

dict = {}

@app.route("/", methods=["GET", "POST"])
def site():
	print("TEST")
	if request.method == "POST":
		print("GENERATE YO!")
		return render_template("index.html")
	else: # request.method == "GET"
		return render_template("index.html")

@app.route('/swagger')
def swagger():
	dict = {}
	p1 = request.args.get('p1')
	p2 = request.args.get('p2')
	loadSelectors(p1, p2)
	text = getNumLines(2) + getNumLines(3)
	print(text)
	return text


def readInFile(filename, charset='utf-8'):
	with open("lyrics/" + filename, 'r') as f:
		words = f.read().decode(charset).rsplit()
		for i in range(len(words)-1):
			pair = words[i]+' '+words[i+1]
			if i < len(words)-2: 
				value = words[i+2]
				if pair not in dict: 
					dict[pair] = [value]
				else:
					dict[pair].append(value)

def getNumLines(numLines):
	lineCount = 0
	while lineCount < numLines:
		current_pair = random.choice(dict.keys())
		result = current_pair.capitalize()
		count = 0
		while current_pair in dict and lineCount < numLines:
			next_word = random.choice(dict[current_pair])
			result = result+ ' '+ next_word
			comp = current_pair.split()
			current_pair = comp[1]+ ' '+ next_word
			count += 1
			if count >= 6:
				lineCount += 1
				count = 0
				result = result + "\n"
		lineCount += 1
	return result

def loadSeuss():
	readInFile('fox-in-socks.txt')
	readInFile('cat-in-the-hat.txt')
	readInFile('green-eggs-and-ham.txt')
	readInFile('one-fish-two-fish.txt')
	readInFile('mullberry-street.txt')

def loadGambino():
	readInFile('freaks-and-geeks.txt')
	readInFile('bonfire.txt')

def loadHemingway():
	readInFile('advice-to-son.txt')
	readInFile('i-like-canadians.txt')

def loadJayZ():
	readInFile('empire-state-of-mind.txt')
	readInFile('holy-grail.txt')

def load2Chainz():
	readInFile('we-own-it.txt')
	readInFile('birthday-song.txt')
	readInFile('im-different.txt')
	readInFile('bandz-dance.txt')

def loadSelectors(p1, p2):
	print("HERE "+ p1 + " " + p2 )
	if (p1 == "seuss") or (p2 == "seuss"):
		print("SEUSS")
		loadSeuss()
	if (p1 == "jay-z") or (p2 == "jay-z"):
		print("JAYZ")
		loadJayZ()
	if (p1 == "ernest") or (p2 == "ernest"):
		print("ERNEST")
		loadHemingway()
	if (p1 == "gambino") or (p2 == "gambino"):
		print("GAMBINO")
		loadGambino() 

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run()



