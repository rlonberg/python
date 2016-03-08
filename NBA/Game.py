#Game.py
import re

"""
Game.py describes an object containing the necessary fields for a given NBA game of the night.
- based on data fields supplied by the XML feed of pinnacleSports
"""

class Game:

    def __init__(self):
        self.home = ""
        self.away = ""
        self.tipoff = ""
        self.valid = False
        self.line = ""

    def __repr__(self):
    	if self.valid:
        	return self.away + " at " + self.home + " tips off " + self.tipoff + "\n      with " + self.line + "\n"
        
        else:
        	return ""

    def fillKeys(self, xmlFeed, datetime):
    	teams = []
    	home_away = []
    	visiting_line = []
        for line in xmlFeed:
        	if "participant_name" in line:
        		teams += [line.replace("<participant_name>","").replace("</participant_name>","").replace("\t","").replace("\r\n","")]
        	if "visiting_home_draw" in line:
        		home_away += [line.replace("<visiting_home_draw>","").replace("</visiting_home_draw>","").replace("\t","").replace("\r\n","")]
        	if "spread_visiting" in line:
        		visiting_line += [line.replace("<spread_visiting>","").replace("</spread_visiting>","").replace("\t","").replace("\r\n","")]
        		
        try:
        	self.home = teams[home_away.index("Home")]
        	self.away = teams[home_away.index("Visiting")]
        	self.tipoff = self.setDatetime(datetime)
        	self.line = self.setLine(visiting_line)
        	self.valid = True

        	#ignore 2nd halfs
        	if "2nd Halfs" in self.away:
        		self.home = "_"
        		self.away = "_"
        		self.tipoff = "_"
        		self.line = "_"
        		self.valid = False

        except:
        	self.home = "_"
        	self.away = "_"
        	self.tipoff = "_"
        	self.valid = False

    """
    Takes a GMT datetime object, extracts time, and converts to EST.
    EST conversion is hardcoded in right now to be 5 hours ahead,
     - will need to adjust for daylight savings in the future
    """
    def setDatetime(self, datetime):
    	time = re.compile("\d{2}:\d{2}") # [24hour:60minute]
    	date = re.compile("-\d{2}-\d{2}") # [-[month]-[day]]

    	''' prepare time, converting from 24-hour GMT to 12-hour EST '''
    	GMT_24 = time.findall(datetime)[0]
    	EST_24 = int(GMT_24[:2]) - 5 #int!
    	EST_12 = EST_24 % 12 #int!
    	EST = str(EST_12) + GMT_24[2:]

    	''' prepate date, chopping off first "-0" from month indicator '''
    	getDate = date.findall(datetime)[0]
    	getDate = getDate[2:]

    	return EST + "pm EST" + " on " + getDate


    """
    Takes a list of visiting lines through periods 0(entire game) through 1st half.
    Current implementation only sets the line for the entire game, valid until tipoff.
    """
    def setLine(self, visitingLine):
    	gameLine = float(visitingLine[0]) # visiting spread from period 0 (entire game)
    	if gameLine < 0:
    		return "visitors favored by -" + str(abs(gameLine))
    	else:
    		return "home favored by -" + str(abs(gameLine))












