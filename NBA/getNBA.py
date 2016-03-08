"""parselines works with fixed input from a text file in the same directory, for the purposes of working online
"""
from urllib import urlopen
from Game import *

league = "NBA" #enter a different league here for different lines

#vegas, realtime sport betting lines, in xml form
lines = "http://xml.pinnaclesports.com/"

#create a channel
sock = urlopen(lines)

#read from channel
htmlSource = sock.read()

#close channel
sock.close()

#set up iterables
record = False
datetime = ""
xmlFeed = []
gameFeed = []

for line in htmlSource.splitlines():
	#grab datetime
	if "event_datetime" in line:
		datetime = line

	if league in line:
		record = True

	if ("</event>" in line) and (record):
		record = False

		thisGame = Game()
		thisGame.fillKeys(xmlFeed,datetime)
		gameFeed += [thisGame]
		xmlFeed = []

	if record:
		xmlFeed += [line]


""" finished parsing xml feed from pinnaclesports """

print("\n")
for game in gameFeed:
	if game.valid:
		print(game)
print("\n")
