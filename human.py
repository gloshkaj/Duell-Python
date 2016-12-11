from player import player
import random
class human(player):
    def __init__(self, front = 1, lat = 1, firstDirection = "", secondDirection= "", startRow = 1, startCol = 1, endRow = 1, endCol = 1):
        self.firstDirection = firstDirection
        self.secondDirection = secondDirection
        self.front = front
        self.lat = lat
        self.startRow = startRow
        self.startCol = startCol
        self.endRow = endRow
        self.endCol = endCol
    '''
    Function name: usedSuggestedMove
    Purpose: To check if the user said Y or N to automatically use the move that the computer suggested.
    Parameters: None
    Returns: True if the user types Y, false otherwise
    '''
    def usedSuggestedMove(self):
        #If they enter yes, they took the computer's help. Otherwise they would have to enter coordinates.
        choice = ""
        while choice.upper() != "N" and choice.upper() != "Y":
            choice = raw_input("Are you sure you want to do this (Y/N, not case sensitive)?")
        if choice.upper() == "Y":
            return True
        return False
    '''
    Function name: isValidHumanDestinationSquare
    Purpose: To check if the destination square does not have a human die on it.
    Parameters:
    a_board, the 2d array containing the human and computer dice.
    a_top, an integer. It contains the number at the top of the die.
    Returns: True if the move does not land on an ally die or go out of bounds of the board, false otherwise.
    '''
    def isValidHumanDestinationSquare(self, a_board, a_top):
        #Report error if the user attempts to capture his own dice or tries to move out of bounds of the board.
        if self.endRow < 1 or self.endRow > 8 or self.endCol < 1 or self.endCol > 9:
            return False
        if str(a_board[9 - self.endRow][self.endCol]).startswith("H"):
            return False
        #Report error if the number of spaces covered is not equal to the number on the top of the die
        # Must use Math.absolute value because the user can move their dice in the following directions.
        #Up, down, left, and right
        if abs(abs(self.endRow - self.startRow) + abs(self.endCol - self.startCol)) != abs(a_top):
            return False
        return True

    ''' *********************************************************************
    Function Name: IsValidPath
    Purpose: To check if a path is valid
    Returns: True if valid, false if not.
    Parameters:
    a_board, the current board passed by reference. It holds the all the computer and human dice.
    Algorithm:
    1) Get the frontal and lateral distance.
    2) If they both are not zero, then check if the paths are valid. If there are dice in the way, return false.
    3) If frontal is zero, check the lateral path, and vice versa. If there are dice in the way, return false.
    Assistance Received: none
    ********************************************************************* '''
    def isValidPath(self, a_board):
        self.front = abs(self.endRow - self.startRow)
        self.lat = abs(self.endCol - self.startCol)
        if (self.front != 0 and self.lat != 0):
            if not self.isValidFrontLatPath(a_board) and not self.isValidLatFrontPath(a_board):
                return False
            elif not self.isValidFrontLatPath(a_board):
                self.firstDirection = "laterally"
                self.secondDirection = "frontally"
                return True
            else:
                self.firstDirection = "frontally"
                self.secondDirection = "laterally"
                return True
        elif self.lat != 0:
            if not self.isValidLatPath(a_board):
                return False
            self.firstDirection = "laterally"
            self.secondDirection = "frontally"
            return True
        elif self.front != 0:
            if not self.isValidFrontPath(a_board):
                return False
            self.firstDirection = "frontally"
            self.secondDirection = "laterally"
            return True
        return False
    '''Function name: isValidLatPath
    Purpose: To check if a horizontal path is valid.
    Parameters: a_board, the 2d array of human and computer dice passed by value
    Returns: True if valid, false otherwise.'''
    def isValidLatPath(self, a_board):
        occupied = False
        if self.startCol < self.endCol:
            for i in range(self.startCol + 1, self.endCol):
                if str(a_board[9 - self.startRow][i]) != "0":
                    occupied = True
        else:
            for i in range(self.startCol - 1, self.endCol, -1):
                if str(a_board[9 - self.startRow][i]) != "0":
                    occupied = True
        if occupied:
            return False
        return True
    '''Function name: isValidFrontPath
    Purpose: To check if a vertical path is valid.
    Parameters: a_board, the 2d array of human and computer dice passed by value
    Returns: True if valid, false otherwise.'''
    def isValidFrontPath(self, a_board):
        occupied = False
        if self.startRow < self.endRow:
            for i in range(self.startRow + 1, self.endRow):
                if str(a_board[9 - i][self.startCol]) != "0":
                    occupied = True
        else:
            for i in range(self.startRow - 1, self.endRow, -1):
                if str(a_board[9 - i][self.startCol]) != "0":
                    occupied = True
        if occupied:
            return False
        return True
    '''Function name: isValidFrontLatPath
    Purpose: To check if a vertical then horizontal path is valid.
    Parameters: a_board, the 2d array of human and computer dice passed by value
    Returns: True if valid, false otherwise.'''
    def isValidFrontLatPath(self, a_board):
        #Check frontal path first. If there is a die in the way it is an invalid path.
        occupied = False
        if self.startRow < self.endRow:
            for i in range(self.startRow + 1, self.endRow + 1):
                if str(a_board[9 - i][self.startCol]) != "0":
                    occupied = True
        else:
            for i in range(self.startRow - 1, self.endRow - 1, -1):
                if str(a_board[9 - i][self.startCol]) != "0":
                    occupied = True
        if self.startCol < self.endCol:
            for i in range(self.startCol + 1, self.endCol):
                if str(a_board[9 - self.endRow][i]) != "0":
                    occupied = True
        else:
            for i in range(self.startCol - 1, self.endCol, -1):
                if str(a_board[9 - self.endRow][i]) != "0":
                    occupied = True
        if occupied:
            return False
        return True
    '''Function name: isValidLatFrontPath
    Purpose: To check if a horizontal then vertical path is valid.
    Parameters: a_board, the 2d array of human and computer dice passed by value
    Returns: True if valid, false otherwise.'''
    def isValidLatFrontPath(self, a_board):
        #Check the lateral path first. If there is a die in the way then it is not valid.
        occupied = False
        if self.startCol < self.endCol:
            for i in range(self.startCol + 1, self.endCol + 1):
                if str(a_board[9 - self.startRow][i]) != "0":
                    occupied = True
        else:
            for i in range(self.startCol - 1, self.endCol - 1, -1):
                if str(a_board[9 - self.startRow][i]) != "0":
                    occupied = True
        if self.startRow < self.endRow:
            for i in range(self.startRow + 1, self.endRow):
                if str(a_board[9 - i][self.endCol]) != "0":
                    occupied = True
        else:
            for i in range(self.startRow - 1, self.endRow, -1):
                if str(a_board[9 - i][self.endCol]) != "0":
                    occupied = True
        if occupied:
            return False
        return True

    ''' *********************************************************************
 Function Name: getAllCoordsInBlockingPath
 Purpose: To get all the blocking paths and all the coordinates in the blocking paths
 Parameters:
 a_coords, the array of coordinate pairs passed by reference. It holds all the empty squares in the blocking paths.
 a_board, the current board passed by reference. It holds the all the computer and human dice.
 Algorithm:
 1) Get the frontal and lateral distance.
 2) If they both are not zero, then check if the paths are valid. Populate the coordinate array with all empty squares in all valid paths.
 3) If frontal is zero, check the lateral path, and vice versa. Populate the path with all empty squares.
 4) Set the reference parameter, a_count, equal to the number of empty squares found so far for the next call of the function.
 Assistance Received: none
 ********************************************************************* '''
    def getAllCoordsInBlockingPath(self, a_board, a_coords):
        self.front = abs(self.endRow - self.startRow)
        self.lat = abs(self.endCol - self.startCol)
        count = self.numFound
        if (self.front != 0 and self.lat != 0): #There is a 90 degree turn. Get coordinates in all empty front/lat or lat/front paths
            if self.isValidFrontLatPath(a_board) and self.isValidLatFrontPath(a_board):
                count = self.numFound
                occupied = False
                if (self.startRow < self.endRow):
                    for i in range(self.startRow + 1, self.endRow + 1):
                        a_coords.append((i, self.startCol))
                        count += 1
                else:
                    for i in range(self.startRow - 1, self.endRow - 1, -1):
                        a_coords.append((i, self.startCol))
                        count += 1
                if (self.startCol < self.endCol):
                    for i in range(self.startCol + 1, self.endCol):
                        a_coords.append(self.endRow, i)
                        count += 1
                else:
                    for i in range(self.startCol - 1, self.endCol, -1):
                        a_coords.append(self.endRow, i)
                        count += 1
                if (self.startCol < self.endCol):
                    for i in range(self.startCol + 1, self.endCol + 1, + 1):
                        a_coords.append((self.startRow, i))
                        count += 1
                else:
                    for i in range(self.startCol - 1,self.endCol - 1, -1):
                        a_coords.append((self.startRow, i))
                        count += 1
                if (self.startRow < self.endRow):
                    for i in range(self.startRow + 1, self.endRow ):
                        a_coords.append((i, self.endCol))
                        count += 1
                else:
                    for i in range(self.startRow - 1, self.endRow, -1):
                        a_coords.append((i, self.endCol))
                        count += 1
            elif (self.isValidFrontLatPath(a_board)):
                count = self.numFound
                occupied = False
                if (self.startRow < self.endRow):
                    for i in range(self.startRow + 1, self.endRow + 1):
                        a_coords.append((i, self.startCol))
                        count += 1
                else:
                    for i in range(self.startRow - 1, self.endRow - 1, -1):
                        a_coords.append((i, self.startCol))
                        count += 1
                if (self.startCol < self.endCol):
                    for i in (self.startCol + 1, self.endCol ):
                        a_coords.append((self.endRow, i))
                        count += 1
                else:
                    for i in range(self.startCol - 1, self.endCol, -1):
                        a_coords.append((self.endRow, i))
                        count += 1
            elif (self.isValidLatFrontPath(a_board)):
                count = self.numFound
                occupied = False
                if (self.startCol < self.endCol):
                    for i in (self.startCol + 1, self.endCol + 1):
                        a_coords.append((self.startRow, i))
                        count += 1
                else:
                    for i in range(self.startCol - 1, self.endCol - 1, -1):
                        a_coords.append((self.startRow, i))
                        count += 1
                if (self.startRow < self.endRow):
                    for i in range(self.startRow + 1, self.endRow):
                        a_coords.append((i, self.endCol))
                        count += 1
                else:
                    for i in range(self.startRow - 1, self.endRow, -1):
                        a_coords.append((i, self.endCol))
                        count += 1
        elif (self.lat != 0): #Then it is completely lateral. Get coordinates between the two dice in the row.
            count = self.numFound
            occupied = False
            if (self.startCol < self.endCol):
                for i in range(self.startCol + 1, self.endCol):
                    a_coords.append((self.startRow, i))
                    count += 1
            else:
                for i in range(self.startCol - 1, self.endCol, -1):
                    a_coords.append((self.startRow, i))
                    count += 1
        elif (self.front != 0): #Then it is completely lateral. Get coordinates between the two dice in the row.
            count = self.numFound
            occupied = False
            print str(self.startRow) + " " + str(self.endRow)
            if (self.startRow < self.endRow):
                for i in range(self.startRow + 1, self.endRow):
                    a_coords.append((i, self.startCol))
                    count += 1
            else:
                for i in range(self.startRow - 1, self.endRow, -1):
                    a_coords.append((i, self.startCol))
                    count += 1
        self.numFound = count
        self.pairs = list(a_coords)
    ''' *********************************************************************
Function Name: makeBlockingMove
Purpose: To perform the move to block the human from winning.
Parameters:
a_game, the board object passed by reference.
a_coords, the array of coordinate pairs passed by reference. It holds all the empty squares in the blocking paths.
a_board, the current board passed by reference. It holds the all the computer and human dice.
a_numFound, an integer. It refers to the number of empty squares in the blocking paths.
a_player, the character referring to whether the computer or the human is playing.
a_view. the boardView object passed by reference.
Returns: False if no blocking path was found or no die can arrive in the blocking path, True otherwise.
Algorithm:
1) For each die on the board, get the distance to the blocking path.
2) If it can move into the blocking path and it is not the key die, make the move if the computer is playing, and suggest the move if the human is playing.
Assistance Received: none
********************************************************************* '''
    def makeBlockingMove(self, a_game, a_coords, a_board, a_numFound, a_player, a_view):
        allowedDist = 0
        dist = 0
        dieToRoll = ""
        player = ""
        if (self.numFound == 0): #If the only winning move was a die with a 1 on top adjacent to the enemy key die, then there are no paths, so just move the key piece at random later on.
            return False
        self.numFound = a_numFound
        #For each coordinate in the blocking paths, and for each die on the board, check that it can get to the path to block.
        for i in range(0, self.numFound):
            for j in range(8, 0, -1):
                for k in range(9, 0, -1):
                    if str(a_board[9 - j][k]).startswith(a_player):
                        col = k
                        row = j
                        allowedDist = ord(str(a_board[9 - j][k])[1]) - 48
                        dist = abs(row - a_coords[i][0]) + abs(col - a_coords[i][1])
                        #If this is not the key die and the die can get to the path, check if the path is valid
                        if dist == allowedDist:
                            self.startCol = col
                            self.startRow = row
                            self.endRow = a_coords[i][0]
                            self.endCol = a_coords[i][1]
                            dieToRoll = str(a_board[9 - j][k])
                            if not self.isValidPath(a_board):
                                #Invalid path. Move on.
                                continue
                            if (a_player == "C"):
                                player = "Computer"
                            else:
                                player = "Garen"
                            #If the computer is playing, make the move, if the human is playing, then the human is asking for help.
                            if player == "Computer":
                                msg = "The computer chose to move " + dieToRoll + " located at (" + str(self.startRow) + ", " + str(self.startCol) + ") "
                                if self.firstDirection == "frontally":
                                    msg += " frontally by " + str(self.front) + " and laterally by " + str(self.lat) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") "
                                else:
                                    msg += " laterally by " + str(self.lat) + " and frontally by " + str(self.front) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") "
                                msg += " to block Garen's path to win the game!"
                                print msg,
                                a_game.updateComputerMove(a_board, self.firstDirection, self.secondDirection, self.startRow, self.startCol, self.endRow, self.endCol)
                                a_view.printBoard(a_game)
                                print " The die is now " + str(a_board[9 - self.endRow][self.endCol]) + " at (" + str(self.endRow) + ", " + str(self.endCol) + ")!"
                            else:
                                msg = "move " + dieToRoll + " located at (" + str(self.startRow) + ", " + str(self.startCol) + ") to block "
                                move = ""
                                if self.firstDirection == "frontally":
                                    move = msg + " with a frontal move by " + str(self.front) + " squares followed by a lateral move by " + str(self.lat) + " squares to land at square (" + str(self.endRow) + ", " + str(self.endCol) + ") to block the computer's path to win the game. "
                                else:
                                    move = msg + " with a lateral move by " + str(self.lat) + " squares followed by a frontal path by " + str(self.front) + " squares to land at square (" + str(self.endRow) + ", " + str(self.endCol) + ") to block the computer's path to win the game. "
                                print move,
                            return True
        return False #If we get here then there are no dice the computer can move besides its key die to block.
    '''*********************************************************************
Function Name: play
Purpose: To get the input from the human player and make a move
Parameters:
a_board, the current board passed by reference. It holds the all the computer and human dice.
a_turn, an integer. It refers to the current turn number
Local Variables:
currentBoard, a 2D array of strings (2D array containing the board)
Algorithm:
1) Access the board using the getter function of a_board.
2) Ask the user if they want help. If they say yes (y), display the strategy on the screen. If the user took the computer's suggestion, update the board with that recommended move
3) Otherwise ask the user for start coordinates
4) Validate start coordinates. Report error if the coordinates are invalid or don't correspond to a human die
5) Ask the user for end coordinates. Validate these end coordinates. Report error if the coordinates are out of range or they don't correspond to an empty square or an opponent's dice.
6) If both x coordinates and both y coordinates are not equal then there is a 90 degree turn. Have the user specify frontally or laterally as the first direction if at least one of the paths is not blocked. Otherwise start over.
7) Check the path of the die that no other dice are in the way. Report error if the path is occupied.
8) Update the board and the faces of the dice by calling a_board::UpdateBoard, then Die::Rotate.
Assistance Received: none
********************************************************************* '''
    def play(self, a_board, a_view):
        currentBoard = a_board.getBoard()
        top = 0
        help = ''
        self.firstDirection = ""
        while True:
            #If the user does not say Y or N continue asking the user for input.
            help = raw_input("Do you want to ask the computer for help (Y or N, not case sensitive)?")
            if help.upper() == 'Y':
                print "The computer suggested to ",
                if (self.helpHumanPlayer(a_board, a_view)):
                    return
            elif help.upper() != 'N':
                print "Invalid character for help. Try again."
                continue
            #If the start row or column are invalid or not integers start over
            try:
                self.startRow = int(input("Enter the starting row to move the die (1 - 8)."))
            except:
                print "Can only enter integer for start row. Try again"
                continue
            if self.startRow < 1 or self.startRow > 8:
                print "Row must be between 1 and 8. Try again"
                continue
            try:
                self.startCol = int(input("Enter the starting column for the die (1 - 9)."))
            except:
                print "Can only enter integer for start column. Try again"
                continue
            if self.startCol < 1 or self.startCol > 9:
                print "Column must be between 1 and 9. Try again"
                continue
                #Must be own die
            if not str(currentBoard[9 - self.startRow][self.startCol]).startswith("H"):
                print "You must pick your own die to move! Try again."
                continue
            print "The die at (" + str(self.startRow) + ", " + str(self.startCol) + ") is " + str(currentBoard[9 - self.startRow][self.startCol]) + ". ",
            # If the end row or column are invalid or not integers start over
            try:
                self.endRow = int(input("Enter the destination row for the die (1 - 8)."))
            except:
                print "Can only enter integer for end row. Try again"
                continue
            if self.endRow < 1 or self.endRow > 8:
                print "End Row must be between 1 and 8. Try again"
                continue
            try:
                self.endCol = int(input("Enter the destination column for the die (1 - 9)"))
            except:
                print "Can only enter integer for end column. Try again."
                continue
            if self.endCol < 1 or self.endCol > 9:
                print "End Column must be between 1 and 9. Try again."
                continue
                #Cannot land on own die
            if str(currentBoard[9 - self.endRow][self.endCol]).startswith("H"):
                print "You must land on an empty square or your opponent's dice! Try again."
                continue
            topFace = str(currentBoard[9 - self.startRow][self.startCol])[1]
            top = ord(topFace) - 48
            #Must cover exactly the number of squares as the number on top
            if abs(self.endRow - self.startRow) + abs(self.endCol - self.startCol) != top:
                print "Must move exactly " + str(top),
                if top == 1:
                    print "square. ",
                else:
                    print "squares. ",
                print "Try again."
                continue
                #Determine movement and update the board and validate paths that they are not blocked.
                #Then there is a 90 degree turn
            if self.startRow != self.endRow and self.startCol != self.endCol:
                #If both paths are invalid then don't ask user for first direction.
                if not self.isValidLatFrontPath(currentBoard) and not self.isValidFrontLatPath(currentBoard):
                    print "Both paths are blocked. Try again."
                    continue
                self.firstDirection = raw_input("Do you first want to move frontally or laterally (frontally/laterally, case sensitive)? ")
                if self.firstDirection == "frontally":
                    self.secondDirection = "laterally"
                    #If the frontal first is invalid start over
                    if not self.isValidFrontLatPath(currentBoard):
                        print "Frontal then lateral path is blocked. You may want to try this move with lateral path first. Try again."
                        continue
                elif self.firstDirection == "laterally":
                    self.secondDirection = "frontally"
                    #If the lateral first in invalid start over.
                    if not self.isValidLatFrontPath(currentBoard):
                        print "Lateral then frontal path is blocked. You may want to try this move with frontal path first. Try again."
                        continue
                else: #Continue asking until a valid choice is given.
                    print "Invalid direction choice. Try again."
                    continue
            #then this is a vertical path.
            elif self.startRow != self.endRow:
                self.firstDirection = "frontally"
                self.secondDirection = "laterally"
                if not self.isValidFrontPath(currentBoard):
                    print "Path is blocked. Try again."
                    continue
            else:
                #then this is a horizontal path
                self.firstDirection = "laterally"
                self.secondDirection = "frontally"
                if not self.isValidLatPath(currentBoard):
                    print "Path is blocked. Try again."
                    continue
            self.front = abs(self.endRow - self.startRow)
            self.lat = abs(self.endCol - self.startCol)
            print "Garen has decided to move " + str(currentBoard[9 - self.startRow][self.startCol]) + " located at (" + str(self.startRow) + " , " + str(self.startCol) + ") " + str(self.firstDirection) + " by ",
            if self.firstDirection == "laterally":
                print str(self.lat) + " and frontally by " + str(self.front) + " ",
            else:
                print str(self.front) + " and laterally by " + str(self.lat) + " ",
            print "to square (" + str(self.endRow) + ", " + str(self.endCol) + ")! ",
            a_board.updateBoard(currentBoard, self.firstDirection, self.secondDirection, self.startRow, self.startCol, self.endRow, self.endCol)
            a_view.printBoard(a_board)
            return
    ''' *********************************************************************
Function Name: helpHumanPlayer
Purpose: To allow the computer player to suggest a move to the human if it asks for help.
Returns: True if the human took the suggestion, false otherwise.
Parameters:
a_board, the current board passed by reference. It holds the all the computer and human dice.
a_view, the boardView object passed by reference
Local Variables:
currentBoard, a 2d array of strings (2D array containing the board)
coords, a array of (x, y) pairs containing all dice in a blocking path on the board
Algorithm:
1) Access the board using the getter function of a_board.
2) Get the row and column of the human and computer key dice.
3) For each space on the board, check if there is a die that will lead to a win. If there is, suggest that move.
4) For each computer die on the board, see if it can get to the human key die right away. If it can, determine all possible paths that be invaded.
5) If none of them result in a blocking move or if the key die is adjacent to a die with 1 on the top, suggest moving the key piece. Otherwise, suggest the piece that blocks the human from winning the game. This prevents the computer from winning even if they had many moves to win though does not fit with certain cases.
6) If 3, 4, and 5 don't result in a successful move made by the human, and there are no other non key die that can be captured, suggest the die which is the minimum of the distance to the key piece minus the number at the top of the die before the move.
7) If 6 is what results in a reasonable move, choose the directions at random until the computer chooses a valid path.
8) If the human took the suggestion, update the board and the faces of the dice by calling a_board::UpdateBoard, then Die::Rotate.
********************************************************************* '''
    def helpHumanPlayer(self, a_board, a_view):
        self.pairs = []
        self.numFound = 0
        currentBoard = a_board.getBoard()
        dieToRoll = ""
        #Get the row and column of all key dice
        rowOfHumanKeyPiece = a_board.findRowHumanKeyPiece()
        colOfHumanKeyPiece = a_board.findColHumanKeyPiece()
        rowOfCompKeyPiece = a_board.findRowCompKeyPiece()
        colOfCompKeyPiece = a_board.findColCompKeyPiece()
        getsToKeySquare = False
        min = 25
        dist = 0
        allowedDist = 0
        distToOtherKeySquare = 0
        currentRow = 0
        currentCol = 0
        humanRow = 0
        humanCol = 0
        distToOpposingKeyDie = 0
        allowedBlockingDist = 0
        #check if the human wins the game
        for i in range(1, 9):
            for j in range(1, 10):
                currentRow = i
                currentCol = j
                if (str(currentBoard[9 - i][j]) == "0"):
                    continue
                if str(currentBoard[9 - i][j]).startswith("H"):
                    dist = abs(currentRow - rowOfCompKeyPiece) + abs(currentCol - colOfCompKeyPiece)
                    allowedDist = ord(str(currentBoard[9 - i][j])[1]) - 48
                    distToOtherKeySquare = abs(currentRow - 8) + abs(currentCol - 5)
                    getsToKeySquare = (distToOtherKeySquare == allowedDist and str(currentBoard[9 - i][j]).endswith("11"))
                    if (dist == allowedDist or getsToKeySquare):
                        self.startRow = currentRow
                        self.startCol = currentCol
                        dieToRoll = str(currentBoard[9 - i][j])
                        if dist == allowedDist:
                            self.endCol = colOfCompKeyPiece
                            self.endRow = rowOfCompKeyPiece
                        elif getsToKeySquare:
                            self.endCol = 5
                            self.endRow = 8
                        if not self.isValidPath(currentBoard):
                            #Path to win is blocked. Human cannot win the game. Move on
                            continue
                        if not self.isValidHumanDestinationSquare(currentBoard, allowedDist):
                            #Destination square has an ally die on it. Move on.
                            continue
                        #Yes, the human can win! Suggest the move.
                        print "move " + dieToRoll + " located at (" + str(self.startRow) + ", " + str(self.startCol) + ") ",
                        if self.firstDirection == "frontally":
                            print "frontally by " + str(self.front) + " and laterally by " + str(self.lat) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") to win the round! "
                        else:
                            print "laterally by " + str(self.lat) + " and frontally by " + str(self.front) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") to win the round! "
                        if self.usedSuggestedMove():
                            #Then the human took the suggestion. Update the board accordingly.
                            self.front = abs(self.endRow - self.startRow)
                            self.lat = abs(self.endCol - self.startCol)
                            print "Garen has decided to move " + str(currentBoard[9 - self.startRow][self.startCol]) + " located at (" + str(self.startRow) + " , " + str(self.startCol) + ") " + str(self.firstDirection) + " by ",
                            if self.firstDirection == "laterally":
                                print str(self.lat) + " and frontally by " + str(self.front) + " ",
                            else:
                                print str(self.front) + " and laterally by " + str(self.lat) + " ",
                            print "to square (" + str(self.endRow) + ", " + str(self.endCol) + ")! ",
                            a_board.updateBoard(currentBoard, self.firstDirection, self.secondDirection, self.startRow, self.startCol, self.endRow, self.endCol)
                            a_view.printBoard(a_board)
                            return True
                        return False
                    if dist - allowedDist < min:
                        min = dist - allowedDist
        blocking = 0
        coords = []
        for i in range(1, 9):
            for j in range(1, 10):
                humanRow = i
                humanCol = j
                if str(currentBoard[9 - i][j]).startswith("C"):
                    distToOpposingKeyDie = abs(humanRow - rowOfHumanKeyPiece) + abs(humanCol - colOfHumanKeyPiece)
                    allowedBlockingDist = ord(str(currentBoard[9 - i][j])[1]) - 48
                    if allowedBlockingDist == distToOpposingKeyDie:
                        #Then a computer die is allowedDist squares away from the key die.
                        self.startRow = humanRow
                        self.startCol = humanCol
                        self.endRow = rowOfHumanKeyPiece
                        self.endCol = colOfHumanKeyPiece
                        if not self.isValidPath(currentBoard):
                            #threatened path is blocked. move on
                            continue
                        blocking += 1
                        if (distToOpposingKeyDie < 2):
                            #Then the die is adjacent so move on.
                            continue
                        #Get all the coordinates in the blocking paths.
                        self.getAllCoordsInBlockingPath(currentBoard, coords)
        if self.makeBlockingMove(a_board, self.pairs, currentBoard, self.numFound, "H", a_view):
            if self.usedSuggestedMove():
                #If the human took the suggestion automatically use the move and update the board accordingly.
                self.front = abs(self.endRow - self.startRow)
                self.lat = abs(self.endCol - self.startCol)
                print "Garen has decided to move " + str(
                    currentBoard[9 - self.startRow][self.startCol]) + " located at (" + str(
                    self.startRow) + " , " + str(self.startCol) + ") " + str(self.firstDirection) + " by ",
                if self.firstDirection == "laterally":
                    print str(self.lat) + " and frontally by " + str(self.front) + " ",
                else:
                    print str(self.front) + " and laterally by " + str(self.lat) + " ",
                print "to square (" + str(self.endRow) + ", " + str(self.endCol) + ")! ",
                a_board.updateBoard(currentBoard, self.firstDirection, self.secondDirection, self.startRow,
                                    self.startCol, self.endRow, self.endCol)
                a_view.printBoard(a_board)
                return True
            return False
        elif blocking >= 1:
            #Otherwise if there were at least one blocking move, move the key piece in a random direction by one while the destination is not the player's own dice.
            self.startRow = rowOfHumanKeyPiece
            self.startCol = colOfHumanKeyPiece
            dieToRoll = currentBoard[9 - self.startRow][self.startCol]
            print "move " + dieToRoll + " located at (" + str(self.startRow) + ", " + str(self.startCol) + ") ",
            while True:
                flag = random.randint(0, 3)
                if (flag == 0):
                    self.endCol = self.startCol
                    self.endRow = self.startRow - 1
                elif (flag == 1):
                    self.endCol = self.startCol + 1
                    self.endRow = self.startRow
                elif (flag == 2):
                    self.endCol = self.startCol
                    self.endRow = self.startRow + 1
                else:
                    self.endCol = self.startCol - 1
                    self.endRow = self.startRow
                if (self.isValidHumanDestinationSquare(currentBoard, 1)):
                    break
            self.front = abs(self.endRow - self.startRow)
            self.lat = abs(self.endCol - self.startCol)
            self.firstDirection = "frontally"
            self.secondDirection = "laterally"
            print "frontally by " + str(self.front) + " and laterally by " + str(self.lat) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") to defend the special die! ",
            if self.usedSuggestedMove():
                #Then the human took the suggestion. Automatically use the move and update the board.
                self.front = abs(self.endRow - self.startRow)
                self.lat = abs(self.endCol - self.startCol)
                print "Garen has decided to move " + str(
                    currentBoard[9 - self.startRow][self.startCol]) + " located at (" + str(
                    self.startRow) + " , " + str(self.startCol) + ") " + str(self.firstDirection) + " by ",
                if self.firstDirection == "laterally":
                    print str(self.lat) + " and frontally by " + str(self.front) + " ",
                else:
                    print str(self.front) + " and laterally by " + str(self.lat) + " ",
                print "to square (" + str(self.endRow) + ", " + str(self.endCol) + ")! ",
                a_board.updateBoard(currentBoard, self.firstDirection, self.secondDirection, self.startRow,
                                    self.startCol, self.endRow, self.endCol)
                a_view.printBoard(a_board)
                return True
            return False
            #Again, update and display the board and then get out of the function.
        pieces = dict()
        for i in range(8, 0, -1):
            for j in range(9, 0, -1):
                #place all computer dice in the dictionary. Coordinate pair is key and die is value
                if str(currentBoard[i][j]).startswith("C"):
                    pieces[(9 - i, j)] = currentBoard[i][j]
        for key in pieces.keys():
            for i in range(1, 9):
                for j in range(1, 10):
                    currentRow = i
                    currentCol = j
                    if str(currentBoard[9 - i][j]).startswith("H"):
                        #Check if a human die can reach the key piece.
                        dist = abs(currentRow - key[0]) + abs(currentCol - key[1])
                        allowedDist = ord(str(currentBoard[9 - i][j])[1]) - 48
                        if (dist == allowedDist):
                            self.startRow = currentRow
                            self.startCol = currentCol
                            dieToRoll = str(currentBoard[9 - i][j])
                            self.endCol = key[1]
                            self.endRow = key[0]
                            if not self.isValidPath(currentBoard):
                            #Path to win is blocked. Move on
                                continue
                            if not self.isValidHumanDestinationSquare(currentBoard, allowedDist):
                            #Destination square has an ally die on it. Move on.
                                continue
                            print "move " + dieToRoll + " located at (" + str(self.startRow) + ", " + str(self.startCol) + ") ",
                            if self.firstDirection == "frontally":
                                print "frontally by " + str(self.front) + " and laterally by " + str(self.lat) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") to capture one of its non-key dice! ",
                            else:
                                print "laterally by " + str(self.lat) + " and frontally by " + str(self.front) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") to capture one of its non-key dice! ",
                        #Update and display the board if the user took the suggestion
                            if self.usedSuggestedMove():
                                self.front = abs(self.endRow - self.startRow)
                                self.lat = abs(self.endCol - self.startCol)
                                print "Garen has decided to move " + str(
                                    currentBoard[9 - self.startRow][self.startCol]) + " located at (" + str(
                                    self.startRow) + " , " + str(self.startCol) + ") " + str(
                                    self.firstDirection) + " by ",
                                if self.firstDirection == "laterally":
                                    print str(self.lat) + " and frontally by " + str(self.front) + " ",
                                else:
                                    print str(self.front) + " and laterally by " + str(self.lat) + " ",
                                print "to square (" + str(self.endRow) + ", " + str(self.endCol) + ")! ",
                                a_board.updateBoard(currentBoard, self.firstDirection, self.secondDirection,
                                                    self.startRow, self.startCol, self.endRow, self.endCol)
                                a_view.printBoard(a_board)
                                return True
                            return False
        for i in range(1, 9):
            for j in range(1, 10):
                currentRow = i
                currentCol = j
                dist = abs(currentRow - rowOfCompKeyPiece) + abs(currentCol - colOfCompKeyPiece)
                if str(currentBoard[9 - i][j]).startswith("H"):
                    allowedDist = ord(str(currentBoard[9 - i][j])[1]) - 48
                if str(currentBoard[9 - i][j]).startswith("H") and dist - allowedDist == min:
                    self.startRow = currentRow
                    self.startCol = currentCol
                    dieToRoll = currentBoard[9 - self.startRow][self.startCol]
                    while True: #Get values randomly until a valid move is made.
                        firstMove = (random.randint(1, allowedDist))
                        flag = (random.randint(0, 1))
                        secondMove = allowedDist - firstMove
                        secondflag = (random.randint(0, 1))
                        if (flag == 0):
                            firstMove *= -1
                        if (secondflag == 0):
                            secondMove *= -1
                        self.endCol = self.startCol + firstMove
                        self.endRow = self.startRow + secondMove
                        self.front = abs(self.endRow - self.startRow)
                        self.lat = abs(self.startCol - self.startCol)
                        if self.isValidHumanDestinationSquare(currentBoard, allowedDist) and self.isValidPath(currentBoard):
                            break
                    print "move " + dieToRoll + " located at (" + str(self.startRow) + ", " + str(self.startCol) + ") ",
                    if self.firstDirection == "frontally":
                        print "frontally by " + str(self.front) + " and laterally by " + str(self.lat) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") because there are no moves that will threaten it! ",
                    else:
                        print "laterally by " + str(self.lat) + " and frontally by " + str(self.front) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") because there are no moves that will threaten it! ",
                        #Update and display the board if the user took the suggestion.
                    if self.usedSuggestedMove():
                        self.front = abs(self.endRow - self.startRow)
                        self.lat = abs(self.endCol - self.startCol)
                        print "Garen has decided to move " + str(
                            currentBoard[9 - self.startRow][self.startCol]) + " located at (" + str(
                            self.startRow) + " , " + str(self.startCol) + ") " + str(self.firstDirection) + " by ",
                        if self.firstDirection == "laterally":
                            print str(self.lat) + " and frontally by " + str(self.front) + " ",
                        else:
                            print str(self.front) + " and laterally by " + str(self.lat) + " ",
                        print "to square (" + str(self.endRow) + ", " + str(self.endCol) + ")! ",
                        a_board.updateBoard(currentBoard, self.firstDirection, self.secondDirection, self.startRow,
                                            self.startCol, self.endRow, self.endCol)
                        a_view.printBoard(a_board)
                        return True
                    return False
