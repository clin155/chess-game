# File: RookBishopQueen.py
# By: Christopher Luey
# Date: 2/10/20
# Rook, Bishop, Queen classes

from Piece import *

class Rook(Piece):
    def __init__(self, coord, board, color, img):
        # Call superclass constructor
        super().__init__(coord, board, color, img)

    def getPossibleMovesNoCheck(self):
        # Change the x and y values to check which squares rook has available to move to
        # List: the list of possible moves for the rook
        x, y, list, board = 1, 1, [], self.board.getBoardList()
        # Check whether the coord is within the board, if it is empty or occupied by an opponent piece, continue to increment x and y until the checking coord is off the board or occupied by same color piece
        for i in [-1, 1]:
            while (0 <= (self.coord[1] + i*x) <= 7) and (board[self.coord[0]][self.coord[1] + i*x] == None or board[self.coord[0]][self.coord[1] + i*x].getColor() != self.color):
                list.append((self.coord[0],self.coord[1]+i*x))
                # Exit loop if checking tile with piece on it
                if board[self.coord[0]][self.coord[1] + i*x] != None: break
                x+=1
            x=1
        for i in [-1,1]:
            while (0<= (self.coord[0] + i*y) <= 7) and (board[self.coord[0] + i*y][self.coord[1]] == None or board[self.coord[0] + i*y][self.coord[1]].getColor() != self.color):
                list.append((self.coord[0] + i*y, self.coord[1]))
                if board[self.coord[0] + i*y][self.coord[1]]!= None: break
                y+=1
            y = 1
        return list


class Bishop(Piece):
    def __init__(self, coord, board, color, img):
        # Call superclass constructor
        super().__init__(coord, board, color, img)

    def getPossibleMovesNoCheck(self):
        x, y, board, list = 1, 1, self.board.getBoardList(), []
        # Check all 4 diagonals by adjusting the x, y directions
        for i in [-1, 1]:
            for j in [-1, 1]:
                # Check whether the tile is not off the grid, and is empty or occupied by opponent piece
                while (0<=self.coord[1] + i*x <= 7) and (0 <=self.coord[0] + j*y <= 7) and (board[self.coord[0] + j*y][self.coord[1] + i*x] == None or board[self.coord[0] + j*y][self.coord[1] + i*x].getColor() != self.color):
                    list.append((self.coord[0]+j*y,self.coord[1]+i*x))
                    # Exit loop if hitting piece
                    if board[self.coord[0] + j*y][self.coord[1] + i*x] != None: break
                    x, y = x+1, y+1
                x, y = 1,1
        return list


class Queen(Rook, Bishop):
    def __init__(self, coord, board, color,img):
        # Call the superclass constructor
        super().__init__(coord, board, color,img)

    def getPossibleMovesNoCheck(self):
        # Get the possible moves list by calling superclasses
        rookMoves = super().getPossibleMovesNoCheck()
        # By passing Rook, it looks for function getPossibleMovesNoCheck() in Bishop class
        bishopMoves = super(Rook, self).getPossibleMovesNoCheck()
        return rookMoves+bishopMoves
