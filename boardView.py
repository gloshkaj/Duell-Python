from board import board
class boardView:
    #initializer
    def __init__(self, board):
        self.pieces = []
        self.board = board
    '''
    Function name: printBoard
    Purpose: To display the new, updated board on the screen.
    Parameters:
    a_board: The board object passed by value. It contains the human and computer dice.
    '''
    def printBoard(self, a_board):
        self.pieces = self.board.getBoard(a_board)
        #Access the board and write each row on the board to the console and format it appropriately.
        for row in range(0, 9):
            for column in self.pieces[row]:
                if (row == 0):
                    if (str(column) == ""):
                        print "   ",
                    else :
                        print str(column) + "  ",
                elif(len(str(column)) == 3):
                    print str(column),
                else:
                    print str(column) + "  ",
            print ""
    '''
    Function name: printBoard
    Purpose: To display the board in the file.
    Parameters:
    a_board: The board object passed by value. It contains the human and computer dice.
    a_file: The file object passed by reference. It holds the file to write the serialized game to.
    '''
    def writeBoardToFile(self, a_board, a_file):
        self.pieces = self.board.getBoard(a_board)
        #Access the board and write each row on the board to "a_file" and format it appropriately
        for row in range(0, 9):
            for column in self.pieces[row]:
                if (row == 0):
                    if (str(column) == ""):
                        a_file.write(str("       ").rjust(7)),
                    else :
                        a_file.write(str(column) + "   "),
                else:
                    a_file.write(str(column).rjust(4)),
            #Write a new line when it is time to go to the next row.
            a_file.write("\n")