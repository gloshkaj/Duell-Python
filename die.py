class die:
    #initializer, getters, and setters
    def __init__(self, top = 1, right = 1):
        self.top = top
        self.right = right
    def getTop(self):
        return self.top
    def getRight(self):
        return self.right
    def setTop(self, a_top):
        self.top = a_top
    def setRight(self, a_right):
        self.right = a_right
    #To get the die as a string
    def toString(self):
        return str(self.top) + str(self.right)
    ''' *********************************************************************
Function Name: determineLateralMovement
Purpose: To determine values from forward lateral movement of the die.
Parameters:
a_lateral: The array passed by reference holding values from lateral movement
a_frontal: The array passed by reference holding values from frontal movement
Algorithm:
1) If top and right are both 1 don't do anything with the arrays.
2) Otherwise make sure that opposite elements add up to 7.
********************************************************************* '''
    def determineLateralMovement(self, a_lateral, a_frontal):
        # For this and the next three functions, if the top and right are 1, set everything to 1, otherwise circulate the arrays and make sure everything adds up to 7.
        if self.top == 5 and self.right == 6:
            a_lateral.append(5)
            a_lateral.append(1)
            a_lateral.append(2)
            a_lateral.append(6)
        elif self.top == 5 and self.right == 3:
            a_lateral.append(5)
            a_lateral.append(4)
            a_lateral.append(2)
            a_lateral.append(3)
        elif self.top == 5 and self.right == 1:
            a_lateral.append(5)
            a_lateral.append(6)
            a_lateral.append(2)
            a_lateral.append(1)
        elif self.top == 5 and self.right == 4:
            a_lateral.append(5)
            a_lateral.append(3)
            a_lateral.append(2)
            a_lateral.append(4)
        elif self.top == 1 and self.right == 5:
            a_lateral.append(1)
            a_lateral.append(2)
            a_lateral.append(6)
            a_lateral.append(5)
        elif self.top == 1 and self.right == 3:
            a_lateral.append(1)
            a_lateral.append(4)
            a_lateral.append(6)
            a_lateral.append(3)
        elif self.top == 1 and self.right == 2:
            a_lateral.append(1)
            a_lateral.append(5)
            a_lateral.append(6)
            a_lateral.append(2)
        elif self.top == 1 and self.right == 4:
            a_lateral.append(1)
            a_lateral.append(3)
            a_lateral.append(6)
            a_lateral.append(4)
        elif self.top == 2 and self.right == 1:
            a_lateral.append(2)
            a_lateral.append(6)
            a_lateral.append(5)
            a_lateral.append(1)
        elif self.top == 2 and self.right == 3:
            a_lateral.append(2)
            a_lateral.append(4)
            a_lateral.append(5)
            a_lateral.append(3)
        elif self.top == 2 and self.right == 6:
            a_lateral.append(2)
            a_lateral.append(1)
            a_lateral.append(5)
            a_lateral.append(6)
        elif self.top == 2 and self.right == 4:
            a_lateral.append(2)
            a_lateral.append(3)
            a_lateral.append(5)
            a_lateral.append(4)
        elif self.top == 6 and self.right == 2:
            a_lateral.append(6)
            a_lateral.append(5)
            a_lateral.append(1)
            a_lateral.append(2)
        elif self.top == 6 and self.right == 3:
            a_lateral.append(6)
            a_lateral.append(4)
            a_lateral.append(1)
            a_lateral.append(3)
        elif self.top == 6 and self.right == 5:
            a_lateral.append(6)
            a_lateral.append(2)
            a_lateral.append(1)
            a_lateral.append(5)
        elif self.top == 6 and self.right == 4:
            a_lateral.append(6)
            a_lateral.append(3)
            a_lateral.append(1)
            a_lateral.append(4)
        elif self.top == 3 and self.right == 2:
            a_lateral.append(3)
            a_lateral.append(5)
            a_lateral.append(4)
            a_lateral.append(2)
        elif self.top == 3 and self.right == 1:
            a_lateral.append(3)
            a_lateral.append(6)
            a_lateral.append(4)
            a_lateral.append(1)
        elif self.top == 3 and self.right == 5:
            a_lateral.append(3)
            a_lateral.append(2)
            a_lateral.append(4)
            a_lateral.append(5)
        elif self.top == 3 and self.right == 6:
            a_lateral.append(3)
            a_lateral.append(1)
            a_lateral.append(4)
            a_lateral.append(6)
        elif self.top == 4 and self.right == 5:
            a_lateral.append(4)
            a_lateral.append(2)
            a_lateral.append(3)
            a_lateral.append(5)
        elif self.top == 4 and self.right == 1:
            a_lateral.append(4)
            a_lateral.append(6)
            a_lateral.append(3)
            a_lateral.append(1)
        elif self.top == 4 and self.right == 2:
            a_lateral.append(4)
            a_lateral.append(5)
            a_lateral.append(3)
            a_lateral.append(2)
        elif self.top == 4 and self.right == 6:
            a_lateral.append(4)
            a_lateral.append(1)
            a_lateral.append(3)
            a_lateral.append(6)
        elif self.top == 1 and self.right == 1:
            for i in range(0, 4):
                a_frontal.append(1)
                a_lateral.append(1)
    ''' *********************************************************************
Function Name: determineFrontalMovement
Purpose: To determine values from forward frontal movement of the die.
Parameters:
a_frontal: The array passed by reference holding values from frontal movement
a_lateral: The array passed by reference holding values from lateral movement
Algorithm:
1) If top and right are both 1 don't do anything with the arrays.
2) Otherwise make sure that opposite elements add up to 7.
********************************************************************* '''
    def determineFrontalMovement(self, a_frontal, a_lateral):
        if self.top == 5 and self.right == 6:
            a_frontal.append(5)
            a_frontal.append(3)
            a_frontal.append(2)
            a_frontal.append(4)

        elif self.top == 5 and self.right == 3:
            a_frontal.append(5)
            a_frontal.append(1)
            a_frontal.append(2)
            a_frontal.append(6)

        elif self.top == 5 and self.right == 1:
            a_frontal.append(5)
            a_frontal.append(4)
            a_frontal.append(2)
            a_frontal.append(3)

        elif self.top == 5 and self.right == 4:
            a_frontal.append(5)
            a_frontal.append(6)
            a_frontal.append(2)
            a_frontal.append(1)

        elif self.top == 1 and self.right == 5:
            a_frontal.append(1)
            a_frontal.append(3)
            a_frontal.append(6)
            a_frontal.append(4)

        elif self.top == 1 and self.right == 3:
            a_frontal.append(1)
            a_frontal.append(2)
            a_frontal.append(6)
            a_frontal.append(5)

        elif self.top == 1 and self.right == 2:
            a_frontal.append(1)
            a_frontal.append(4)
            a_frontal.append(6)
            a_frontal.append(3)

        elif self.top == 1 and self.right == 4:
            a_frontal.append(1)
            a_frontal.append(5)
            a_frontal.append(6)
            a_frontal.append(2)

        elif self.top == 2 and self.right == 1:
            a_frontal.append(2)
            a_frontal.append(3)
            a_frontal.append(5)
            a_frontal.append(4)

        elif self.top == 2 and self.right == 3:
            a_frontal.append(2)
            a_frontal.append(6)
            a_frontal.append(5)
            a_frontal.append(1)

        elif self.top == 2 and self.right == 6:
            a_frontal.append(2)
            a_frontal.append(4)
            a_frontal.append(5)
            a_frontal.append(3)

        elif self.top == 2 and self.right == 4:
            a_frontal.append(2)
            a_frontal.append(1)
            a_frontal.append(5)
            a_frontal.append(6)

        elif self.top == 6 and self.right == 2:
            a_frontal.append(6)
            a_frontal.append(3)
            a_frontal.append(1)
            a_frontal.append(4)

        elif self.top == 6 and self.right == 3:
            a_frontal.append(6)
            a_frontal.append(5)
            a_frontal.append(1)
            a_frontal.append(2)

        elif self.top == 6 and self.right == 5:
            a_frontal.append(6)
            a_frontal.append(4)
            a_frontal.append(1)
            a_frontal.append(3)

        elif self.top == 6 and self.right == 4:
            a_frontal.append(6)
            a_frontal.append(2)
            a_frontal.append(1)
            a_frontal.append(5)

        elif self.top == 3 and self.right == 2:
            a_frontal.append(3)
            a_frontal.append(1)
            a_frontal.append(4)
            a_frontal.append(6)

        elif self.top == 3 and self.right == 1:
            a_frontal.append(3)
            a_frontal.append(5)
            a_frontal.append(4)
            a_frontal.append(2)

        elif self.top == 3 and self.right == 5:
            a_frontal.append(3)
            a_frontal.append(6)
            a_frontal.append(4)
            a_frontal.append(1)

        elif self.top == 3 and self.right == 6:
            a_frontal.append(3)
            a_frontal.append(2)
            a_frontal.append(4)
            a_frontal.append(5)

        elif self.top == 4 and self.right == 5:
            a_frontal.append(4)
            a_frontal.append(1)
            a_frontal.append(3)
            a_frontal.append(6)

        elif self.top == 4 and self.right == 1:
            a_frontal.append(4)
            a_frontal.append(2)
            a_frontal.append(3)
            a_frontal.append(5)

        elif self.top == 4 and self.right == 2:
            a_frontal.append(4)
            a_frontal.append(6)
            a_frontal.append(3)
            a_frontal.append(1)

        elif self.top == 4 and self.right == 6:
            a_frontal.append(4)
            a_frontal.append(5)
            a_frontal.append(3)
            a_frontal.append(2)

        elif self.top == 1 and self.right == 1:
            for i in range(0, 4):
                a_frontal.append(1)
                a_lateral.append(1)
    ''' *********************************************************************
    Function Name: determineReverseFrontalMovement
    Purpose: To determine values from backward frontal movement of the die.
    Parameters:
    a_frontal: The array passed by reference holding values from frontal movement
    a_lateral: The array passed by reference holding values from lateral movement
    Algorithm:
    1) If top and right are both 1 don't do anything with the arrays.
    2) Otherwise make sure that opposite elements add up to 7.
    ********************************************************************* '''
    def determineReverseFrontalMovement(self, a_frontal, a_lateral):
        if self.top == 5 and self.right == 6:
            a_frontal.append(5)
            a_frontal.append(4)
            a_frontal.append(2)
            a_frontal.append(3)
        
        elif self.top == 5 and self.right == 3:
            a_frontal.append(5)
            a_frontal.append(6)
            a_frontal.append(2)
            a_frontal.append(1)
        
        elif self.top == 5 and self.right == 1:
            a_frontal.append(5)
            a_frontal.append(3)
            a_frontal.append(2)
            a_frontal.append(4)
        
        elif self.top == 5 and self.right == 4:
            a_frontal.append(5)
            a_frontal.append(1)
            a_frontal.append(2)
            a_frontal.append(6)
        
        elif self.top == 1 and self.right == 5:
            a_frontal.append(1)
            a_frontal.append(4)
            a_frontal.append(6)
            a_frontal.append(3)
        
        elif self.top == 1 and self.right == 3:
            a_frontal.append(1)
            a_frontal.append(5)
            a_frontal.append(6)
            a_frontal.append(2)
        
        elif self.top == 1 and self.right == 2:
            a_frontal.append(1)
            a_frontal.append(3)
            a_frontal.append(6)
            a_frontal.append(4)
        
        elif self.top == 1 and self.right == 4:
            a_frontal.append(1)
            a_frontal.append(2)
            a_frontal.append(6)
            a_frontal.append(5)
        
        elif self.top == 2 and self.right == 1:
            a_frontal.append(2)
            a_frontal.append(4)
            a_frontal.append(5)
            a_frontal.append(3)
        
        elif self.top == 2 and self.right == 3:
            a_frontal.append(2)
            a_frontal.append(1)
            a_frontal.append(5)
            a_frontal.append(6)
        
        elif self.top == 2 and self.right == 6:
            a_frontal.append(2)
            a_frontal.append(3)
            a_frontal.append(5)
            a_frontal.append(4)
        
        elif self.top == 2 and self.right == 4:
            a_frontal.append(2)
            a_frontal.append(6)
            a_frontal.append(5)
            a_frontal.append(1)
        
        elif self.top == 6 and self.right == 2:
            a_frontal.append(6)
            a_frontal.append(4)
            a_frontal.append(1)
            a_frontal.append(3)
        
        elif self.top == 6 and self.right == 3:
            a_frontal.append(6)
            a_frontal.append(2)
            a_frontal.append(1)
            a_frontal.append(5)
        
        elif self.top == 6 and self.right == 5:
            a_frontal.append(6)
            a_frontal.append(3)
            a_frontal.append(1)
            a_frontal.append(4)
        
        elif self.top == 6 and self.right == 4:
            a_frontal.append(6)
            a_frontal.append(5)
            a_frontal.append(1)
            a_frontal.append(2)
        
        elif self.top == 3 and self.right == 2:
            a_frontal.append(3)
            a_frontal.append(6)
            a_frontal.append(4)
            a_frontal.append(1)
        
        elif self.top == 3 and self.right == 1:
            a_frontal.append(3)
            a_frontal.append(2)
            a_frontal.append(4)
            a_frontal.append(5)
        
        elif self.top == 3 and self.right == 5:
            a_frontal.append(3)
            a_frontal.append(1)
            a_frontal.append(4)
            a_frontal.append(6)
        
        elif self.top == 3 and self.right == 6:
            a_frontal.append(3)
            a_frontal.append(5)
            a_frontal.append(4)
            a_frontal.append(2)
        
        elif self.top == 4 and self.right == 5:
            a_frontal.append(4)
            a_frontal.append(6)
            a_frontal.append(3)
            a_frontal.append(1)
        
        elif self.top == 4 and self.right == 1:
            a_frontal.append(4)
            a_frontal.append(5)
            a_frontal.append(3)
            a_frontal.append(2)
        
        elif self.top == 4 and self.right == 2:
            a_frontal.append(4)
            a_frontal.append(1)
            a_frontal.append(3)
            a_frontal.append(6)
        
        elif self.top == 4 and self.right == 6:
            a_frontal.append(4)
            a_frontal.append(2)
            a_frontal.append(3)
            a_frontal.append(5)
        
        elif self.top == 1 and self.right == 1:
            for i in range(0, 4):
                a_frontal.append(1)
                a_lateral.append(1)

    ''' *********************************************************************
    Function Name: determineReverseLateralMovement
    Purpose: To determine values from backward lateral movement of the die.
    Parameters:
    a_lateral: The array passed by reference holding values from lateral movement
    a_frontal: The array passed by reference holding values from frontal movement
    Algorithm:
    1) If top and right are both 1 don't do anything with the arrays.
    2) Otherwise make sure that opposite elements add up to 7.
    ********************************************************************* '''
    def determineReverseLateralMovement(self, a_lateral, a_frontal):
        if self.top == 5 and self.right == 6:
            a_lateral.append(5)
            a_lateral.append(6)
            a_lateral.append(2)
            a_lateral.append(1)
        elif self.top == 5 and self.right == 3:
            a_lateral.append(5)
            a_lateral.append(3)
            a_lateral.append(2)
            a_lateral.append(4)
        elif self.top == 5 and self.right == 1:
            a_lateral.append(5)
            a_lateral.append(1)
            a_lateral.append(2)
            a_lateral.append(6)
        elif self.top == 5 and self.right == 4:
            a_lateral.append(5)
            a_lateral.append(4)
            a_lateral.append(2)
            a_lateral.append(3)
        elif self.top == 1 and self.right == 5:
            a_lateral.append(1)
            a_lateral.append(5)
            a_lateral.append(6)
            a_lateral.append(2)
        elif self.top == 1 and self.right == 3:
            a_lateral.append(1)
            a_lateral.append(3)
            a_lateral.append(6)
            a_lateral.append(4)
        elif self.top == 1 and self.right == 2:
            a_lateral.append(1)
            a_lateral.append(2)
            a_lateral.append(6)
            a_lateral.append(5)
        elif self.top == 1 and self.right == 4:
            a_lateral.append(1)
            a_lateral.append(4)
            a_lateral.append(6)
            a_lateral.append(3)
        elif self.top == 2 and self.right == 1:
            a_lateral.append(2)
            a_lateral.append(1)
            a_lateral.append(5)
            a_lateral.append(6)
        elif self.top == 2 and self.right == 3:
            a_lateral.append(2)
            a_lateral.append(3)
            a_lateral.append(5)
            a_lateral.append(4)
        elif self.top == 2 and self.right == 6:
            a_lateral.append(2)
            a_lateral.append(6)
            a_lateral.append(5)
            a_lateral.append(1)
        elif self.top == 2 and self.right == 4:
            a_lateral.append(2)
            a_lateral.append(4)
            a_lateral.append(5)
            a_lateral.append(3)
        elif self.top == 6 and self.right == 2:
            a_lateral.append(6)
            a_lateral.append(2)
            a_lateral.append(1)
            a_lateral.append(5)
        elif self.top == 6 and self.right == 3:
            a_lateral.append(6)
            a_lateral.append(3)
            a_lateral.append(1)
            a_lateral.append(4)
        elif self.top == 6 and self.right == 5:
            a_lateral.append(6)
            a_lateral.append(5)
            a_lateral.append(1)
            a_lateral.append(2)
        elif self.top == 6 and self.right == 4:
            a_lateral.append(6)
            a_lateral.append(4)
            a_lateral.append(1)
            a_lateral.append(3)
        elif self.top == 3 and self.right == 2:
            a_lateral.append(3)
            a_lateral.append(2)
            a_lateral.append(4)
            a_lateral.append(5)
        elif self.top == 3 and self.right == 1:
            a_lateral.append(3)
            a_lateral.append(1)
            a_lateral.append(4)
            a_lateral.append(6)
        elif self.top == 3 and self.right == 5:
            a_lateral.append(3)
            a_lateral.append(5)
            a_lateral.append(4)
            a_lateral.append(2)
        elif self.top == 3 and self.right == 6:
            a_lateral.append(3)
            a_lateral.append(6)
            a_lateral.append(4)
            a_lateral.append(1)
        elif self.top == 4 and self.right == 5:
            a_lateral.append(4)
            a_lateral.append(5)
            a_lateral.append(3)
            a_lateral.append(2)
        elif self.top == 4 and self.right == 1:
            a_lateral.append(4)
            a_lateral.append(1)
            a_lateral.append(3)
            a_lateral.append(6)
        elif self.top == 4 and self.right == 2:
            a_lateral.append(4)
            a_lateral.append(2)
            a_lateral.append(3)
            a_lateral.append(5)
        elif self.top == 4 and self.right == 6:
            a_lateral.append(4)
            a_lateral.append(6)
            a_lateral.append(3)
            a_lateral.append(1)
        elif self.top == 1 and self.right == 1:
            for i in range(0, 4):
                a_frontal.append(1)
                a_lateral.append(1)
    ''' *********************************************************************
Function Name: rotate
Purpose: To determine values of new top and right faces after human's move
Returns: A new string with the new top and right faces after the move
Parameters:
a_board, the current board passed by reference. It contains the computer and human's dice
a_front, a string passed by reference containing the first direction
a_lat, a string passed by reference containing the second direction
a_NextRow, an integer containing the starting row
a_NextCol, an integer containing the starting column
a_DestRow, an integer referencing the ending row.
a_DestCol, an integer referencing the ending column.
Local Variables:
frontal, lateral: int arrays to populate for frontal and lateral movement
Algorithm:
1) If frontal movement is first, do frontal calculation first, otherwise, do lateral calculation first.
2) If start is less than end, do forward frontal and lateral movement, otherwise do backward frontal and lateral movement.
3) For each empty square in the path, calculate the new top and right face of the die at each roll.
4) Return the die at the destination coordinate.
********************************************************************* '''
    def rotate(self, a_board, a_front, a_lat, a_NextRow, a_NextCol, a_DestRow, a_DestCol):
        #This is similar to the computer's rotate function but with the semantics flipped. So we will only comment here.
        result = "H"
        die = a_board[9 - a_NextRow][a_NextCol]
        #Set initial top and right faces
        self.setTop(ord(str(die[1])) - 48)
        self.setRight(ord(str(die[2])) - 48)
        frontal = []
        lateral = []
        #Popluate frontal and lateral arrays
        if a_front == "frontally" and a_lat == "laterally":
            #If the start is greater than end, calculate values from reverse movement
            if a_NextRow <= a_DestRow:
                self.determineFrontalMovement(frontal, lateral)
            else:
                self.determineReverseFrontalMovement(frontal, lateral)
            for i in range(1, abs(a_DestRow - a_NextRow) + 1):
                self.setTop(frontal[i % 4])
            if a_NextCol <= a_DestCol:
                self.determineLateralMovement(lateral, frontal)
                for i in range(1, abs(a_DestCol - a_NextCol) + 1):
                    #Update right and top faces based on this movement. Algorithm is similar for the rest of this function.
                    top = self.top
                    self.setRight(top)
                    self.setTop(lateral[i % 4])
            else:
                self.determineReverseLateralMovement(lateral, frontal)
                for i in range(1, abs(a_DestCol - a_NextCol) + 1):
                    right = self.right
                    self.setTop(right)
                    self.setRight(lateral[((i + 1) % 4)])
        else:
            if a_NextCol <= a_DestCol:
                self.determineLateralMovement(lateral, frontal)
                for i in range(1, abs(a_DestCol - a_NextCol) + 1):
                    top = self.top
                    self.setRight(top)
                    self.setTop(lateral[i % 4])
            else:
                self.determineReverseLateralMovement(lateral, frontal)
                for i in range(1, abs(a_DestCol - a_NextCol) + 1):
                    right = self.right
                    self.setTop(right)
                    self.setRight(lateral[((i + 1)% 4)])
            if a_NextRow <= a_DestRow:
               self.determineFrontalMovement(frontal, lateral)
            else:
               self.determineReverseFrontalMovement(frontal, lateral)
            
            for i in range(1, abs(a_DestRow - a_NextRow) + 1):
                self.setTop(frontal[i % 4])
        result += self.toString()
        return result
    ''' *********************************************************************
Function Name: rotateComputerDie
Purpose: To determine values of new top and right faces after computer's move
Returns: A new string with the new top and right faces after the move
Parameters:
a_board, the current board passed by reference. It contains the computer and human's dice
a_front, a string passed by reference containing the first direction
a_lat, a string passed by reference containing the second direction
a_NextRow, an integer containing the starting row
a_NextCol, an integer containing the starting column
a_DestRow, an integer referencing the ending row.
a_DestCol, an integer referencing the ending column.
Local Variables:
frontal, lateral: int arrays to populate for frontal and lateral movement
Algorithm:
1) If frontal movement is first, do frontal calculation first, otherwise, do lateral calculation first.
2) If start is less than end, do forward frontal and lateral movement, otherwise do backward frontal and lateral movement.
3) For each empty square in the path, calculate the new top and right face of the die at each roll.
4) Return the die at the destination coordinate.
********************************************************************* '''
    def rotateComputerDie(self, a_board, a_front, a_lat, a_NextRow, a_NextCol, a_DestRow, a_DestCol):
        #This is very similar to the human's rotate function
        result = "C"
        die = a_board[9 - a_NextRow][a_NextCol]
        self.setTop(ord(str(die[1])) - 48)
        self.setRight(ord(str(die[2])) - 48)
        frontal = []
        lateral = []
        if a_front == "frontally" and a_lat == "laterally":
            if a_NextRow >= a_DestRow:
                self.determineFrontalMovement(frontal, lateral)
            else:
                self.determineReverseFrontalMovement(frontal, lateral)
            for i in range(1, abs(a_DestRow - a_NextRow) + 1):
                self.setTop(frontal[i % 4])
            if a_NextCol >= a_DestCol:
                self.determineLateralMovement(lateral, frontal)
                for i in range(1, abs(a_DestCol - a_NextCol) + 1):
                    top = self.top
                    self.setRight(top)
                    self.setTop(lateral[i % 4])
            else:
                self.determineReverseLateralMovement(lateral, frontal)
                for i in range(1, abs(a_DestCol - a_NextCol) + 1):
                    right = self.right
                    self.setTop(right)
                    self.setRight(lateral[((i + 1) % 4)])
        else:
            if a_NextCol >= a_DestCol:
                self.determineLateralMovement(lateral, frontal)
                for i in range(1, abs(a_DestCol - a_NextCol) + 1):
                    top = self.top
                    self.setRight(top)
                    self.setTop(lateral[i % 4])
            else:
                self.determineReverseLateralMovement(lateral, frontal)
                for i in range(1, abs(a_DestCol - a_NextCol) + 1):
                    right = self.right
                    self.setTop(right)
                    self.setRight(lateral[((i + 1) % 4)])
            if a_NextRow >= a_DestRow:
                self.determineFrontalMovement(frontal, lateral)
            else:
                self.determineReverseFrontalMovement(frontal, lateral)
            for i in range(1, abs(a_DestRow - a_NextRow) + 1):
                self.setTop(frontal[i % 4])
        result += self.toString()
        return result