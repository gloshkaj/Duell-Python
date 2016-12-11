from game import game
class tournament:
    #initializer
    def __init__(self, game = game()):
        self.game = game
    '''
    Function name: getWinner
    Purpose: Determines the winner of the tournament.
    Parameters: None
    '''
    def getWinner(self):
        #Get number of human and computer wins
        human = self.game.getHumanWins()
        computer = self.game.getComputerWins()
        #If the human won more rounds, the human won. If the computer won more rounds, the computer won. Otherwise it was a draw
        print "The human won " + str(human) + " rounds and the computer won " + str(computer) + " rounds.",
        if (human < computer):
            print " So the computer has won the tournament!"
        elif(human > computer):
            print " So Garen has won the tournament!"
        else:
            print " So the scores were tied. Therefore this tournament was a draw!"
        '''
        Function name: playSeries
        Purpose: Plays a series of rounds.
        Parameters: None
        Algorithm:
        1) While the user wants to play new rounds:
        1a) Play a new round.
        1b) Ask the user if they want to play again and validate that they typed Y or N
        1c) If they typed in N, get the winner of the tournament and end the program.
        '''
    def playSeries(self):
        choice = ""
        #While the user wants to play more rounds,
        while True:
            #Play a new round
            self.game.playGame()
            #Ask the user if they want to play again
            while choice.upper() != "N" and choice.upper() != "Y":
                #validate input
                choice = raw_input("Do you want to play another round (Y/N, not case sensitive)?")
                if choice.upper() == "N":
                    #If they said no then get the winner of the series and end the program
                    print "This tournament has ended! ",
                    self.getWinner()
                    return
            choice = ""