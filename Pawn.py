#File: Pawn.py
# Written By: Christopher Luey
# Date: 2/29/20
# Pawn class

from Piece import *

class Pawn(Piece):
	def __init__(self, coord, board, color, img):
		# Call superclass constructor
		super().__init__(coord, board, color, img)
		self.turn, self.state = True, 0


	def getPossibleMovesNoCheck(self):
		# board: 2d array of board
		# x: variable to switch direction whether it is a black or white pawn
		# list: list of pawn's possible moves

		board, x, list = self.board.getBoardList(), -1, []
		# Set value of x to determine which direction to look for possible moves
		if self.color == 'black': x=1
		# Check whether pawn is not at edge of board, and the square in front of it is empty
		if 0<= (self.coord[0]+x) <= 7 and board[self.coord[0]+x][self.coord[1]] == None:
			list.append((self.coord[0]+x, self.coord[1]))
			# Check whether it is the pawn's first turn and two squares in front of it are empty
			if self.turn and board[self.coord[0]+x*2][self.coord[1]] == None: list.append((self.coord[0]+x*2, self.coord[1]))

		# Check whether the squares diagonally to pawn are available for capture
		for i in [1,-1]:
			if 0<=(self.coord[1] + i) <=7 and 0 <= (self.coord[0]+x) <= 7 and board[self.coord[0] + x][self.coord[1] + i] != None and board[self.coord[0] + x][self.coord[1] + i].getColor() != self.color: list.append((self.coord[0] + x, self.coord[1] + i))
		return list


	def move(self, coord):
		super().move(coord)
		self.turn = False
		# If pawn is at edge of board
		if (self.coord[0] == 0 or self.coord[0] == 7):
			# Initiate promotion sequence
			self.promotion()
			# Tell runner that pawn has promoted
			return True


	def promotion(self):
		# Promote the pawn
		self.board.promotion(self)
