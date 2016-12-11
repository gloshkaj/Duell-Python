from die import die
class board:
    #initializer
    def __init__(self):
        self.list = []
        for i in range(0, 9):
            line = []
            for j in range(0, 10):
                line.append("0")
            self.list.append(line)
        self.top = 1
        self.right = 1
        self.row = 1
        self.column = 8
        self.die = die()
    #Access the board
    def getBoard(self):
        return self.list
    '''
    Function name: getStartingPiece
    Purpose: To determine the starting die in the home row when a round begins.
    Parameters:
    a_index, an integer. It represents the nth column in the 1st or the 8th row-> the human or the computer's home row.
    a_player, the string representing the owner of the die-> human or computer
    Returns: The die to place at the initial location.
    Algorithm:
    1) If the index is 5, this is the key die, so top and right are both 1.
    2) If the index is 1 or 9, then this is a 5/6 die so set the top to 5 and the right to 6.
    2a) To make the sum of opposite pieces add to seven, set top to 2 and right to 1 when index is 3 or 7.
    3) If the index is 2 or 8, then this is a 1/5 die so set the top to 1 and the right to 5.
    3a) To make the sum of opposite pieces add to seven, set top to 6 and right to 2 when index is 4 or 6.
    4) Concatenate the owner of the die, the top of the die, and the right of the die into a string and return the resulting string.
    '''
    def getStartingPiece(self, a_index, a_player):
        #Human or computer
        piece = a_player
        if (a_index == 5):
            #Then this is the key piece
            self.top = 1
            self.right = 1
        elif (a_index == 1 or a_index == 9):
            #Then this is a 5/6 piece
            self.top = 5
            self.right = 6
        elif (a_index == 2 or a_index == 8):
            #Then this is a 1/5 piece
            self.top = 1
            self.right = 5
        elif (a_index == 4 or a_index == 6):
            #Then this is a 6/2 piece
            self.top = 6
            self.right = 2
        elif (a_index == 3 or a_index == 7):
            #If we get here then this is a 2/1 piece
            self.top = 2
            self.right = 1
        #Update the top and right faces and return the concatenated string
        die.setRight(self.die, self.right)
        die.setTop(self.die, self.top)
        return piece + self.die.toString()
    '''
    Function name: fillBoard
    Purpose: To repopulate the board from the saved state row by row.
    Parameters:
    a_lines, the array of lines from the file passed by value. It contains the lines from the file that we are restoring from.
    a_index, an integer. It contains the nth row to restore from the saved state
    '''
    def fillBoard(self, a_lines, a_index):
        for piece in range(0, len(a_lines)):
            if a_index == 0:
                #Then we are filling the column coordinates so make the top left column an empty string and populate starting at the second column
                self.list[a_index][piece + 1] = a_lines[piece]
            else:
                #Then this is a row in the board so populate each column accordingly
                self.list[a_index][piece] = a_lines[piece]
    '''
    Function name: drawInitialBoard
    Purpose: To draw the initial board when a round begins.
    Parameters:
    None
    Algorithm:
    1) If the index is 0, set the column coordinates accordingly.
    2) If the index is 1, then this is the computer's home row, so populate the computer's home row.
    3) If the index is 8, then this is the human's home row, so populate the human's home row.
    '''
    def drawInitialBoard(self):
        for i in range(0, 9):
            if (i == 0):
                #Then this is the column coordinate row. Place the coordinate numbers at the top
                for j in range(0, 10):
                    if (j == 0):
                        self.list[i][j] = ""
                    else:
                        self.list[i][j] = str(j)
            elif (i == 1):
                #Then this is the computer's home row. Populate this row.
                for j in range(0, 10):
                    if (j == 0):
                        self.list[i][j] = str(self.column)
                        self.column = self.column - 1
                    else:
                        self.list[i][j] = self.getStartingPiece(j, 'C')
            elif (i == 8):
                #Then this is the human's home row. Populate this row.
                for j in range(0, 10):
                    if (j == 0):
                        self.list[i][j] = str(self.column)
                        self.column = self.column - 1
                    else:
                        self.list[i][j] = self.getStartingPiece(j, 'H')
            else:
                #If we get here we are in the middle of the board. Put 0's for empty squares.
                self.list[i][0] = self.column
                self.column = self.column - 1
                for j in range(1, 10):
                    if (self.list[i][j] != 0):
                        self.list[i][j] = 0
    '''
    Function name: updateBoard
    Purpose: To update the board from a user's move.
    Parameters:
    a_board, the 2D list containing the board passed by value. It contains the dice on the board.
    a_firstDirection, the string containing the first direction to move the die.
    a_secondDirection, the string containing the second direction to move the die.
    a_NextRow, an integer containing the starting row
    a_NextCol, an integer containing the starting column
    a_DestRow, an integer containing the ending row
    a_DestCol, an integer containing the ending column
    Algorithm:
    1) Call rotate in the die class to get the new top and right faces after the move.
    2) Empty the starting square.
    3) If the ending square had an enemy die in it, tell the user that they captured the enemy die.
    4) Put the new die in the ending square.
    '''
    def updateBoard(self, a_board, a_firstDirection, a_secondDirection, a_NextRow, a_NextCol, a_DestRow, a_DestCol):
        #Get the new top and right faces after the move.
        newDie = str(self.die.rotate(a_board, a_firstDirection, a_secondDirection, a_NextRow, a_NextCol, a_DestRow, a_DestCol))
        #Empty the starting square.
        self.list[9 - a_NextRow][a_NextCol] = "0"
        print "The die is now " + newDie + " at (" + str(a_DestRow) + ", " + str(a_DestCol) + ")! ",
        #If the ending square had an enemy die in it, tell the user they captured it.
        if str(self.list[9 - a_DestRow][a_DestCol]) != "0":
            print ("You captured " + str(self.list[9 - a_DestRow][a_DestCol]) + " which was previously located at (" + str(a_DestRow) + ", " + str(a_DestCol) + ")!")
        else:
            print ""
        #Update the ending square with the new die
        self.list[9 - a_DestRow][a_DestCol] = newDie
    '''
    Function name: updateComputerMove
    Purpose: To update the board from the computer's move.
    Parameters:
    a_board, the 2D list containing the board passed by value. It contains the dice on the board.
    a_firstDirection, the string containing the first direction to move the die.
    a_secondDirection, the string containing the second direction to move the die.
    a_NextRow, an integer containing the starting row
    a_NextCol, an integer containing the starting column
    a_DestRow, an integer containing the ending row
    a_DestCol, an integer containing the ending column
    Algorithm:
    1) Call rotateComputerDie in the die class to get the new top and right faces after the move.
    2) Empty the starting square.
    3) If the ending square had an enemy die in it, tell the user that they captured the enemy die.
    4) Put the new die in the ending square.
    '''
    def updateComputerMove(self, a_board, a_firstDirection, a_secondDirection, a_NextRow, a_NextCol, a_DestRow, a_DestCol):
        #Get the new top and right faces after the move.
        newDie = str(self.die.rotateComputerDie(a_board, a_firstDirection, a_secondDirection, a_NextRow, a_NextCol, a_DestRow, a_DestCol))
        #Empty the stating square
        self.list[9 - a_NextRow][a_NextCol] = "0"
        print "The die is now " + newDie + " at (" + str(a_DestRow) + ", " + str(a_DestCol) + ")! ",
        #If there was an enemy die at the destination, tell the computer it captured the enemy die.
        if str(self.list[9 - a_DestRow][a_DestCol]) != "0":
            print ("The computer captured " + str(self.list[9 - a_DestRow][a_DestCol]) + " which was previously located at (" + str(a_DestRow) + ", " + str(a_DestCol) + ")!")
        else:
            print ""
        #Update the ending square with the new die.
        self.list[9 - a_DestRow][a_DestCol] = newDie
    #getters and setters
    def getTopPiece(self):
        return self.top
    def getRightPiece(self):
        return self.right
    def getXCoord(self):
        return self.row
    def getYCoord(self):
        return self.column
    def setTopPiece(self, a_top):
        self.top = a_top
    def setRightPiece(self, a_right):
        self.right = a_right
    def setXCoord(self, a_row):
        self.row = a_row
    def setYCoord(self, a_col):
        self.column = a_col
    '''
    Function name: findKeyPiece
    Purpose: To check if the die exists on the board.
    Parameters:
    a_key, the string containing the die to search for.
    Returns: True if found, false if not found.
    '''
    def findKeyPiece(self, a_key):
        for i in range(0, 9):
            for j in range(0, 10):
                if (self.list[i][j] == a_key):
                    return True
        #If we get here it was not found and the game would be over.
        return False
    '''
    Function name: findRowCompKeyPiece
    Purpose: To get the row of the computer's key die.
    Parameters:
    None
    Returns: The row if found, -1 if not found.
    '''
    def findRowCompKeyPiece(self):
        for i in range(0, 9):
            for j in range(0, 10):
                if (self.list[i][j] == "C11"):
                    return 9 - i
        #If we get here it was not found.
        return -1
    '''
    Function name: findColCompKeyPiece
    Purpose: To get the row of the computer's key die.
    Parameters:
    None
    Returns: The column if found, -1 if not found.
    '''
    def findColCompKeyPiece(self):
        for i in range(0, 9):
            for j in range(0, 10):
                if (self.list[i][j] == "C11"):
                    return j
        #If we get here it was not found
        return -1
    '''
    Function name: findRowHumanKeyPiece
    Purpose: To get the row of the human's key die.
    Parameters:
    None
    Returns: The row if found, -1 if not found.
    '''
    def findRowHumanKeyPiece(self):
        for i in range(0, 9):
            for j in range(0, 10):
                if (self.list[i][j] == "H11"):
                    return 9 - i
        #If we get here it was not found
        return -1
    '''
    Function name: findColHumanKeyPiece
    Purpose: To get the column of the humans's key die.
    Parameters:
    None
    Returns: The column if found, -1 if not found.
    '''
    def findColHumanKeyPiece(self):
        for i in range(0, 9):
            for j in range(0, 10):
                if (self.list[i][j] == "H11"):
                    return j
        #If we get here it was not found.
        return -1