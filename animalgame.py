"""
animalgame.py is a self-learning, animal guessing game similar in style to 20 questions.

At the start of the game, the program looks for a pickle_memory.p file in your working directory.
If the file does not exist, it creates one for you. This file will house all of the program's knowledge from previous runs.

Try it out.

"""

import pickle

def play(node):
    """ Play the Animal Game from the given node. """
    player_response = input(node.data + "\nYes/No: ")
    player_response = player_response[0] + player_response[1:] + "?"
    if node.isLeaf():
        if isYes(player_response):
            print("Nice I guessed correctly!\n")
        else:
            print("Looks like I guessed wrong.")
            correct_answer = input("What animal were you thinking of?\nYes/No: ")
            question = ("What question should I have asked to tell the difference between your "
                            + correct_answer + " and my " + node.data + "?\nEnter a question: ")
            lesson = input(question)
            yes = input("... and is the correct answer yes or no?\nYes/No: ")
            if isYes(yes):
                node.right = Node(correct_answer)
                node.left = Node(node.data)
            else:
                node.left = Node(correct_answer)
                node.right = Node(node.data)
            node.data = lesson
                
    else:
        if isYes(player_response):
            play(node.right)
        else:
            play(node.left)


def isYes(response):
    """ Was this a yes response? """
    return ("y" in response) or ("Y" in response)

def main():
    """ Run the Animal Game. """
    # See if they want to print the tree. 
    debugMode = input("Print the tree as you play?\nYes/No: ")
    debug = isYes(debugMode)

    # Assemble the initial tree
    root = Node("Can it fly?")
    left = Node("chicken")
    right = Node("falcon")
    root.left = left
    root.right = right

    try:
        root = pickle.load( open( "pickle_memory.p", "rb" ) )
    except:
        pass
    
    while True:
        
        userChoice = input("Think of an animal.\nEnter: ")
        play(root)
        if debug:
            root.print()
            print()
        response = input("Play again? ")
        if not isYes(response):
            pickle.dump( root, open( "pickle_memory.p", "wb" ) )
            

            break
    
class Node:
    def __init__(self, data):#, isLeaf = False):
        """ Initialize a binary tree node with given data. The left and right
            branches are set to None (null). """
        self.data = data
        self.left = None
        self.right = None

    def isLeaf(self):
        """ Returns True if the Node is of 'leaf' type,
        meaning it contains no more branches,
        and is ready to make an animal guess from its data field.
        """
        return self.left == None or self.right == None

    def print(self):
        """ Print out the tree rooted at this node. """
        lines = []
        strings = []
        self.printNodes(lines, strings)
        st = ""
        for string in strings:
            st = st + string
        print(st)
        
    def printNodes(self, lines, strings):
        """ Helper function for print(). """
        level = len(lines)
        if self.right != None:
            lines.append(False)
            self.printLines(lines, strings, "\n")
            self.right.printNodes(lines, strings)
            lines.pop(level)
        else:
            self.printLines(lines, strings, "\n")

        if level>0:
            old = lines.pop(level-1)
            self.printLines(lines, strings, "  +--")
            lines.append(not old)
        strings.append(self.data + "\n")
        
        if self.left != None:
            lines.append(True)
            self.left.printNodes(lines, strings)
            self.printLines(lines, strings, "\n")
            lines.pop(level)
        else:
            self.printLines(lines, strings, "\n")

    def printLines(self, lines, strings, suffix):
        """ Helper function for print(). """
        for line in lines:
            if line: strings.append("  |  ")
            else:    strings.append("     ")
        strings.append(suffix)

main()
