import random
from player import player
from collections import namedtuple
class computer(player):
    def __init__(self, front = 1, lat = 1, firstDirection = "", secondDirection= "", startRow = 1, startCol = 1, endRow = 1, endCol = 1, found = 0):
        self.firstDirection = firstDirection
        self.secondDirection = secondDirection
        self.front = front
        self.lat = lat
        self.startRow = startRow
        self.startCol = startCol
        self.endRow = endRow
        self.endCol = endCol
        self.numFound = found
        self.pairs = []
    '''
    Function name: isValidLatPath
    Purpose: To check if a horizontal path is valid.
    Parameters: a_board, the 2d array of human and computer dice passed by value
    Returns: True if valid, false otherwise.
    '''
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
    '''
    Function name: isValidFrontalPath
    Purpose: To check if a vertical path is valid.
    Parameters: a_board, the 2d array of human and computer dice passed by value
    Returns: True if valid, false otherwise.
    '''
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
    '''
    Function name: isValidFrontLatPath
    Purpose: To check if a frontal/lateral path is valid.
    Parameters: a_board, the 2d array of human and computer dice passed by value
    Returns: True if valid, false otherwise.
    '''
    def isValidFrontLatPath(self, a_board):
        #Check frontal path first. If there is a die in the way then it is invalid.
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
    '''
    Function name: isValidLatFrontPath
    Purpose: To check if a horizontal then vertical path is valid.
    Parameters: a_board, the 2d array of human and computer dice passed by value
    Returns: True if valid, false otherwise.
    '''
    def isValidLatFrontPath(self, a_board):
        #Check lateral path first. if there is a die in the way then it is invalid.
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
    '''
    Function name: isValidComputerDestinationSquare
    Purpose: To check if the destination square does not have a computer die on it.
    Parameters:
    a_board, the 2d array containing the human and computer dice.
    a_top, an integer. It contains the number at the top of the die.
    Returns: True if the move does not land on an ally die or go out of bounds of the board, false otherwise.
    '''
    def isValidComputerDestinationSquare(self, a_board, a_top):
        #Report error if the user attempts to capture his own dice or tries to move out of bounds of the board.
        if self.endRow < 1 or self.endRow > 8 or self.endCol < 1 or self.endCol > 9:
            return False
        if str(a_board[9 - self.endRow][self.endCol]).startswith("C"):
            return False
        #Report error if the number of spaces covered is not equal to the number on the top of the die
        # Must use Math.absolute value because the user can move their dice in the following directions.
        #Up, down, left, and right
        if abs(abs(self.endRow - self.startRow) + abs(self.endCol - self.startCol)) != abs(a_top):
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
        if self.front != 0 and self.lat != 0: #There is a 90 degree turn so fill every valid path.
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
        elif (self.lat != 0): #Fill lateral path.
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
        elif (self.front != 0): #Fill frontal path
            count = self.numFound
            occupied = False
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
                                msg = "move " + dieToRoll + " located at (" + str(self.endRow) + ", " + str(self.endCol) + ")"
                                move = ""
                                if self.firstDirection == "frontally":
                                    move = msg + " frontally by " + str(self.front) + " and laterally by " + str(self.lat) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") to block the computer's path to win the game. "
                                else:
                                    move = msg + " laterally by " + str(self.lat) + " and frontally by " + str(self.front) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") to block the computer's path to win the game. "
                                print msg,
                            return True
        return False #If we get here then there are no dice the computer can move besides its key die to block.
    '''*********************************************************************
Function Name: Play
Purpose: To allow the computer player to make a move
Parameters:
a_board, the current board passed by reference. It holds the all the computer and human dice.
a_turn, an integer. It refers to the current turn number
a_first, a string passed by value to get the first player
a_player, a string passed by value to get the current player
Local Variables:
currentBoard, a pointer to a pointer to an array of strings (2D array containing the board)
coords, a array of (x, y) pairs containing all dice in a blocking path on the board
Algorithm:
1) Access the board using the getter function of a_board.
2) Get the row and column of the human and computer key dice.
3) For each space on the board, check if there is a die that will lead to a win. If there is, use that move (call UpdateComputerDie then RotateComputerDie)
4) For each human die on the board, see if it can get to the computer key die right away. If it can, determine all possible paths that be invaded.
5) If none of them result in a blocking move or if the key die is adjacent to a die with 1 on the top, move the key piece. Otherwise, use the piece that blocks the human from winning the game. This prevents the human from winning even if they had many moves to win though does not fit with certain cases.
6) If 3, 4, and 5 don't result in a successful move made by the computer, and the computer cannot capture other non key dice, move the die which is the minimum of the distance to the key piece minus the number at the top of the die before the move.
7) If 6 is what results in a reasonable move, choose the directions at random until the computer chooses a valid path. If the computer made 10 incorrect paths it forfeits its turn.
8) Update the board and the faces of the dice by calling a_board::UpdateComputerDie, then Die::RotateComputerDie.
Assistance Received: none
Notes: The computer's strategy is by far the hardest part of the project.
However, we decided to use the following strategy:
If the computer does not have a direct move to the human's key die or it cannot block or capture non key dice it should move the die that:
Can be moved the most squares (has the highest number on top before the move) towards the human's key piece
and that would be the closest to the key piece after its turn has ended. The movement is chosen at random.
********************************************************************* '''
    def play(self, a_board, a_view):
        self.pairs = []
        self.numFound = 0
        currentBoard = a_board.getBoard()
        dieToRoll = ""
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
        for i in range(1, 9):
            for j in range(1, 10):
                currentRow = i
                currentCol = j
                if (str(currentBoard[9 - i][j]) == "0"):
                    continue
                if str(currentBoard[9 - i][j]).startswith("C"):
                    dist = abs(currentRow - rowOfHumanKeyPiece) + abs(currentCol - colOfHumanKeyPiece)
                    allowedDist = ord(str(currentBoard[9 - i][j])[1]) - 48
                    distToOtherKeySquare = abs(currentRow - 1) + abs(currentCol - 5)
                    getsToKeySquare = (distToOtherKeySquare == allowedDist and str(currentBoard[9 - i][j]).endswith("11"))
                    if (dist == allowedDist or getsToKeySquare):
                        self.startRow = currentRow
                        self.startCol = currentCol
                        dieToRoll = str(currentBoard[9 - i][j])
                        if dist == allowedDist:
                            self.endCol = colOfHumanKeyPiece
                            self.endRow = rowOfHumanKeyPiece
                        elif getsToKeySquare:
                            self.endCol = 5
                            self.endRow = 1
                        if not self.isValidPath(currentBoard):
                            #Path to win is blocked. Move on
                            continue
                        if not self.isValidComputerDestinationSquare(currentBoard, allowedDist):
                            #Destination square has an ally die on it. Move on.
                            continue
                        print "The computer chose to move " + dieToRoll + " located at (" + str(self.startRow) + ", " + str(self.startCol) + ") ",
                        if self.firstDirection == "frontally":
                            print "frontally by " + str(self.front) + " and laterally by " + str(self.lat) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") to win the round! "
                        else:
                            print "laterally by " + str(self.lat) + " and frontally by " + str(self.front) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") to win the round! "
                        #Update and display the board
                        a_board.updateComputerMove(currentBoard, self.firstDirection, self.secondDirection, self.startRow, self.startCol, self.endRow, self.endCol)
                        a_view.printBoard(a_board)
                        return
                    if dist - allowedDist < min:
                        min = dist - allowedDist
        blocking = 0
        coords = []
        for i in range(8, 0, -1):
            for j in range(9, 0, -1):
                humanRow = i
                humanCol = j
                if str(currentBoard[9 - i][j]).startswith("H"):
                    distToOpposingKeyDie = abs(humanRow - rowOfCompKeyPiece) + abs(humanCol - colOfCompKeyPiece)
                    allowedBlockingDist = ord(str(currentBoard[9 - i][j])[1]) - 48
                    if allowedBlockingDist == distToOpposingKeyDie:
                        self.startRow = humanRow
                        self.startCol = humanCol
                        self.endRow = rowOfCompKeyPiece
                        self.endCol = colOfCompKeyPiece
                        if not self.isValidPath(currentBoard):
                            continue
                        blocking += 1
                        if (distToOpposingKeyDie < 2):
                            continue
                        self.getAllCoordsInBlockingPath(currentBoard, coords)
        if self.makeBlockingMove(a_board, coords, currentBoard, self.numFound, "C", a_view):
            return
        elif blocking >= 1:
            #Otherwise if there were at least one blocking move, move the key piece in a random direction by one while the destination is not the player's own dice.
            self.startRow = rowOfCompKeyPiece
            self.startCol = colOfCompKeyPiece
            dieToRoll = currentBoard[9 - self.startRow][self.startCol]
            print "The computer chose to move " + dieToRoll + " located at (" + str(self.startRow) + ", " + str(self.startCol) + ") ",
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
                if (self.isValidComputerDestinationSquare(currentBoard, 1)):
                    break
            self.front = abs(self.endRow - self.startRow)
            self.lat = abs(self.endCol - self.startCol)
            self.firstDirection = "frontally"
            self.secondDirection = "laterally"
            print "frontally by " + str(self.front) + " and laterally by " + str(self.lat) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") to defend the special die! ",
            a_board.updateComputerMove(currentBoard, self.firstDirection, self.secondDirection, self.startRow, self.startCol, self.endRow, self.endCol)
            a_view.printBoard(a_board)
            return
            #Again, update and display the board and then get out of the function.
        pieces = dict()
        for i in range(1, 9):
            for j in range(1, 10):
                if str(currentBoard[i][j]).startswith("H"):
                    pieces[(9 - i, j)] = currentBoard[i][j]
        for key in pieces.keys():
            for i in range(1, 9):
                for j in range(1, 10):
                    currentRow = i
                    currentCol = j
                    if str(currentBoard[9 - i][j]).startswith("C"):
                        dist = abs(currentRow - key[0]) + abs(currentCol - key[1])
                        allowedDist = ord(str(currentBoard[9 - i][j])[1]) - 48
                        if (dist == allowedDist):
                            self.startRow = currentRow
                            self.startCol = currentCol
                            dieToRoll = str(currentBoard[9 - i][j])
                            self.endCol = key[1]
                            self.endRow = key[0]
                            if not self.isValidPath(currentBoard):
                            #Path to wcapture non key die is blocked. Move on
                                continue
                            if not self.isValidComputerDestinationSquare(currentBoard, allowedDist):
                            #Destination square has an ally die on it. Move on.
                                continue
                            print "The computer chose to move " + dieToRoll + " located at (" + str(self.startRow) + ", " + str(self.startCol) + ") ",
                            if self.firstDirection == "frontally":
                                print "frontally by " + str(self.front) + " and laterally by " + str(self.lat) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") to capture one of the human's non-key dice! ",
                            else:
                                print "laterally by " + str(self.lat) + " and frontally by " + str(self.front) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") to capture one of the human's non-key dice! ",
                        #Update and display the board
                            a_board.updateComputerMove(currentBoard, self.firstDirection, self.secondDirection, self.startRow, self.startCol, self.endRow, self.endCol)
                            a_view.printBoard(a_board)
                            return
        for i in range(1, 9):
            for j in range(1, 10):
                currentRow = i
                currentCol = j
                dist = abs(currentRow - rowOfHumanKeyPiece) + abs(currentCol - colOfHumanKeyPiece)
                if str(currentBoard[9 - i][j]).startswith("C"):
                    allowedDist = ord(str(currentBoard[9 - i][j])[1]) - 48
                if str(currentBoard[9 - i][j]).startswith("C") and dist - allowedDist == min:
                    self.startRow = currentRow
                    self.startCol = currentCol
                    dieToRoll = currentBoard[9 - self.startRow][self.startCol]
                    while True:
                        firstMove = (random.randint(1, allowedDist));
                        flag = (random.randint(0, 1));
                        secondMove = allowedDist - firstMove;
                        secondflag = (random.randint(0, 1));
                        if (flag == 0):
                            firstMove *= -1;
                        if (secondflag == 0):
                            secondMove *= -1;
                        self.endCol = self.startCol + firstMove;
                        self.endRow = self.startRow + secondMove;
                        self.front = abs(self.endRow - self.startRow);
                        self.lat = abs(self.startCol - self.startCol);
                        if self.isValidComputerDestinationSquare(currentBoard, allowedDist) and self.isValidPath(currentBoard):
                            break
                    print "The computer chose to move " + dieToRoll + " located at (" + str(self.startRow) + ", " + str(self.startCol) + ") ",
                    if self.firstDirection == "frontally":
                        print "frontally by " + str(self.front) + " and laterally by " + str(self.lat) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") because it could not threaten the human player! ",
                    else:
                        print "laterally by " + str(self.lat) + " and frontally by " + str(self.front) + " to square (" + str(self.endRow) + ", " + str(self.endCol) + ") because it could not threaten the human player! ",
                        #Update and display the board
                    a_board.updateComputerMove(currentBoard, self.firstDirection, self.secondDirection, self.startRow, self.startCol, self.endRow, self.endCol)
                    a_view.printBoard(a_board)
                    return
