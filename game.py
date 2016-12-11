import random
import sys
import os
from board import board
from boardView import boardView
from human import human
from computer import computer
from player import player
class game:
    #initializer, getters, and setters
    def __init__(self, firstPlayer = player(), secondPlayer = player()):
        self.computerWins = 0
        self.humanWins = 0
        self.nextPlayer = ""
        self.numRounds = 0
        self.board = board()
        self.boardView = boardView(board)
        self.human = human()
        self.computer = computer()
        self.firstPlayer = firstPlayer
        self.secondPlayer = secondPlayer
    def getComputerWins(self):
        return self.computerWins
    def setComputerWins(self, a_comp):
        self.computerWins = a_comp
    def getHumanWins(self):
        return self.humanWins
    def setHumanWins(self, a_human):
        self.humanWins = a_human
    def getNextPlayer(self):
        return self.nextPlayer
    def setNextPlayer(self, a_next):
        self.nextPlayer = a_next
    def getRoundNo(self):
        return self.numRounds
    def setRoundNo(self, a_round):
        self.numRounds = a_round
    '''
    Function name: getFirstPlayer
    Purpose: To determine who goes first for a given round
    Parameters: none
    '''
    def getFirstPlayer(self):
        compRoll = 0
        humanRoll = 0
        numRolls = 1
        while compRoll == humanRoll:
            print "For dice roll #" + str(numRolls) + ", the human rolled ",
            humanRoll = random.randint(1, 6)
            compRoll = random.randint(1, 6)
            print str(humanRoll) +  " and the computer rolled " + str(compRoll),
            if (humanRoll == compRoll):
                print ", which are the same.",
                numRolls += 1
        if humanRoll < compRoll:
            return "Computer"
        else:
            return "Garen"
    '''
    Function name: isGameOver
    Purpose: To determine if the opponent's key die was captured or the key die was placed on the opponent's key square
    Parameters: None
    Returns: True if the opponent's key die cannot be found or the key die was placed on the enemy key square. False otherwise
    '''
    def isGameOver(self):
        if self.board.getBoard()[1][5] == "H11":#Human placed key piece on computer's key square. Human wins. Increment human wins.
            print "Garen has placed his key piece on the computer's key square! Garen has won this round!"
            self.humanWins += 1
            print "The computer won " + str(self.computerWins) + " rounds and Garen won " + str(self.humanWins) + " rounds. "
            self.resetBoard()
            return True
        elif not self.board.findKeyPiece("H11"): #Computer captured human's key piece. Computer wins. Increment computer score.
            print "The computer has captured Garen's key piece! The computer has won this round!"
            self.computerWins+=1
            print "The computer won " + str(self.computerWins) + " rounds and Garen won " + str(self.humanWins) + " rounds. "
            self.resetBoard()
            return True
        elif self.board.getBoard()[8][5] == "C11": #Computer placed key piece on human's key square. Computer wins. Increment computer wins.
            print "The computer has placed its key piece on Garen's key square! The computer has won this round!"
            self.computerWins+=1
            print "The computer won " + str(self.computerWins) + " rounds and Garen won " + str(self.humanWins) + " rounds. "
            self.resetBoard()
            return True
        elif not self.board.findKeyPiece("C11"): #Human captured computer's key piece. Human wins. Increment human score.
            print "Garen has captured the computer's key piece! Garen has won this round!"
            self.humanWins += 1
            print "The computer won " + str(self.computerWins) + " rounds and Garen won " + str(self.humanWins) + " rounds. "
            self.resetBoard()
            return True
        return False
    '''
    Function name: resetBoard
    Purpose: To reset the board in preparation for a new round.
    Parameters: none
    '''
    def resetBoard(self):
        self.board.setXCoord(1)
        self.board.setYCoord(8)
        self.board.setTopPiece(1)
        self.board.setRightPiece(1)
        #Reset the turn numbers and the board.
        self.setRoundNo(self.numRounds + 1)
    '''
    Function name: isSerialized
    Purpose: To check if the player serialized the game
    Parameters: None
    Returns: True if the user typed Y or y, False otherwise.
    Local Variables:
    file: a filestream object to save the game to
    '''
    def isSerialized(self):
        choice = ""
        isValid = False
        while choice.upper() != "SAVE" and choice.upper() != "CONTINUE":
            choice = raw_input("Please decide if you want to save your current game progress or continue with this game (Save/Continue, not case sensitive).")
            if choice.upper() == "SAVE":
                filename = raw_input("Enter the name of the text file to save your current game.")
                while not isValid:
                    try:
                        file = open(filename, 'w')
                        self.boardView.writeBoardToFile(self.board, file)
                        file.write("Number of rounds won by computer: " + str(self.computerWins) + "\n")
                        file.write("Number of rounds won by Garen: " + str(self.humanWins) + "\n")
                        file.write("Currently, the next player playing is: " + self.nextPlayer + "\n")
                        file.write("This game is currently on round " + str(self.numRounds) + "\n")
                    except IOError:
                        continue
                    isValid = True
                return True
        return False
    ''' *********************************************************************
Function Name: PlayGame
Purpose: To play a round.
Parameters:
None
Local Variables:
file, a filestream object to determine the file to load from.
playerQueue: an array of players to determine which play function to execute based on the first player
lines: an array of strings containing the lines of the file to restore.
strs: an array of strings containing the lines split by space.
Algorithm:
1) If this is the first round, ask if the user want to restore from a saved state. Otherwise, go to step 2.
2) If they say no or this is not the first round, start a new game, draw the initial board, and determine the first player.
3) Otherwise, determine the file to restore from. Check that the file exists, and restore the game from the saved state.
4) In either case, the players will alternte turns. Call isGameOver() to check if the game is over, then call isSerialized() if the game is not over and a turn was made.
5) If any of the conditions for the game being over were met, return.
********************************************************************* '''
    def playGame(self):
        choice = ""
        isValid = False
        #Draw the initial board and display it on the screen
        self.board.drawInitialBoard()
        if self.numRounds == 0:
            #This is not the first round. Ask if they want to start a new series or load from a saved state
            while choice.upper() != "LOAD" and choice.upper() != "NEW":
                choice = raw_input("Do you want to load a saved game or start a new one? (NEW/LOAD, not case sensitive)?")
            if choice.upper() == "NEW":
                #A new series would be played
                print "Starting a new tournament!"
                self.boardView.printBoard(self.board)
                self.numRounds += 1
                playerQueue = []
                #Get the first player and polymorphically circulate the player array
                firstPlayer = self.getFirstPlayer()
                if firstPlayer == "Computer":
                    print ", so the computer gets to move first in round #" + str(self.numRounds) + "!"
                    self.nextPlayer = "Garen"
                    playerQueue = [computer(), human()]
                else:
                    print ", so Garen gets to move first in round #" + str(self.numRounds) + "!"
                    self.nextPlayer = "Computer"
                    playerQueue = [human(), computer()]
                #While the game is not over have the players alternate turns and see if the game was over or saved
                while not self.isGameOver():
                    print firstPlayer + " is playing."
                    playerQueue[0].play(self.board, self.boardView)
                    if self.isGameOver():
                        return
                    if self.isSerialized():
                        sys.exit("Garen saved the game.")
                    print self.nextPlayer + " is playing."
                    playerQueue[1].play(self.board, self.boardView)
                    if self.isGameOver():
                        return
                    if self.isSerialized():
                        sys.exit("Garen saved the game.")
            else:
                #Algorithm is basically the same after we ask for the file to load
                filename = raw_input("Enter the file to restore your progress from")
                while not isValid:
                    if not os.path.exists(filename):
                        filename = raw_input("Enter the file to restore your progress from. ")
                        continue
                    isValid = True
                file = open(filename, 'r+')
                lines = []
                line = file.readline()
                lines.append(line)
                count = 0
                while line:
                    line = file.readline()
                    lines.append(line)
                for row in range(0, 13):
                    #Fill the board row by row
                    strs = str(lines[row]).split()
                    if (count < 9):
                        self.board.fillBoard(strs, count)
                    elif (count == 9):
                        self.setComputerWins(int(strs[6]))
                    elif (count == 10):
                        self.setHumanWins(int(strs[6]))
                    elif (count == 11):
                        self.setNextPlayer(str(strs[6]))
                    elif (count == 12):
                        self.setRoundNo(int(strs[6]))
                    count += 1
                self.boardView.printBoard(self.board)
                playerQueue = []
                firstPlayer = self.nextPlayer
                if firstPlayer == "Computer":
                    self.nextPlayer = "Garen"
                    playerQueue = [computer(), human()]
                else:
                    self.nextPlayer = "Computer"
                    playerQueue = [human(), computer()]
                while not self.isGameOver():
                    print firstPlayer + " is playing."
                    playerQueue[0].play(self.board, self.boardView)
                    if self.isGameOver():
                        return
                    if self.isSerialized():
                        sys.exit("Garen saved the game.")
                    print self.nextPlayer + " is playing."
                    playerQueue[1].play(self.board, self.boardView)
                    if self.isGameOver():
                        return
                    if self.isSerialized():
                        sys.exit("Garen saved the game.")
        else:
            print "Starting a new round!"
            #Same algorithm as before but for a new round
            self.boardView.printBoard(self.board)
            playerQueue = []
            firstPlayer = self.getFirstPlayer()
            if firstPlayer == "Computer":
                print ", so the computer gets to move first in round #" + str(self.numRounds) + "!"
                self.nextPlayer = "Garen"
                playerQueue = [self.computer, self.human]
            else:
                print ", so Garen gets to move first in round #" + str(self.numRounds) + "!"
                self.nextPlayer = "Computer"
                playerQueue = [self.human, self.computer]
            while not self.isGameOver():
                print firstPlayer + " is playing."
                playerQueue[0].play(self.board, self.boardView)
                if self.isGameOver():
                    return
                if self.isSerialized():
                    sys.exit("Garen saved the game.")
                print self.nextPlayer + " is playing."
                playerQueue[1].play(self.board, self.boardView)
                if self.isGameOver():
                    return
                if self.isSerialized():
                    sys.exit("Garen saved the game.")