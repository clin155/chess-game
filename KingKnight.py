# File: KingKnight.py
# Created By: Christopher Lin
# Date: 02/11/20
# creates king and knight classes

from Piece import *

#knight class
class Knight(Piece):
	#inherits from piece constructor
	def __init__(self,coord, board,color, imgStr):
		super().__init__(coord,board,color, imgStr)

	#gets all possible moves without checking if they put king in check
	def getPossibleMovesNoCheck(self):
		#gets all moves in L shape based on piece's coords
		possibleMoves = [(self.coord[0]-2,self.coord[1]+1),\
			(self.coord[0]-2, self.coord[1]-1),(self.coord[0]+2,self.coord[1]+1),\
			(self.coord[0]+2,self.coord[1]-1),(self.coord[0]-1,self.coord[1]-2),\
			(self.coord[0]-1,self.coord[1]+2),(self.coord[0]+1,self.coord[1]-2),\
			(self.coord[0]+1,self.coord[1]+2)]
		legalMoves = []
		#adds tuple to legal moves if self.isLegalmove returns True
		for move in possibleMoves:
			if self.isLegalMove(move):
					legalMoves.append(move)
		return legalMoves
	
	#checks if a tuple is a legal move
	def isLegalMove(self,move):
		row = move[0]
		col = move[1]
		try:
			#makes sure row and col are in range
			if row >= 0 and row <= 7:
				if col >= 0 and col <= 7:
					#checks if space is unoccupied
					if self.board.getBoardList()[row][col] == None or self.board.getBoardList()[row][col].getColor() != self.getColor():
						return True
			return False
		#in case row or col is not an int
		except IndexError:
			return False

#King class
class King(Piece):
	#inherits from piece constructor
	def __init__(self,coord, board,color,imgStr):
		super().__init__(coord,board,color,imgStr)
	
	#gets all possible moves without checking if they put king in check
	def getPossibleMoves(self):
		possibleMoves = self.getPossibleMovesNoCheck()
		legalMoves = []
		for move in possibleMoves:
				if not self.board.check(move,move,self):
					legalMoves.append(move)

		if self.hasMoved == False:
			legalMoves += self.board.getCastleMoves(self)
		return legalMoves


	def getPossibleMovesNoCheck(self):
		#all possible moves are 1 away from self.coord in every direction
		possibleMoves = [(self.coord[0]-1,self.coord[1]),\
			(self.coord[0]-1,self.coord[1]+1),(self.coord[0]-1,self.coord[1]-1),\
			(self.coord[0],self.coord[1]-1),(self.coord[0],self.coord[1]+1),\
			(self.coord[0]+1,self.coord[1]-1),(self.coord[0]+1,self.coord[1]+1),\
			(self.coord[0]+1,self.coord[1])]
		legalMoves = []
		#same as Knight
		for move in possibleMoves:
			if self.isLegalMove(move):
					legalMoves.append(move)
		return legalMoves

	#checks if a tuple is a legal move
	def isLegalMove(self,move):
		row = move[0]
		col = move[1]
		try:
			#makes sure row and col are in range
			if row >= 0 and row <= 7:
				if col >= 0 and col <= 7:
					#checks if space is unoccupied
					if self.board.getBoardList()[row][col] == None or self.board.getBoardList()[row][col].getColor() != self.getColor():
						return True
			return False

		#in case row or col is not an int
		except IndexError:
			return False
	