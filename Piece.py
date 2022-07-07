# File: Piece.py
# By: Christopher Lin
# Date: 2/10/20
# piece superclass

from graphics import *

#Piece class
class Piece():
	#constructor
	def __init__(self, coord, board, color, imgStr):
		#self.board is board object
		self.coord, self.board, self.color = coord, board, color
		self.prevCoord = None
		#moves piece into 2D array
		self.board.movePiece(self)
		self.imgStr = imgStr
		self.isEaten = False
		self.image = Image(Point(-100,-100),"pieces/"+self.imgStr)
		self.undrawn = False
		self.reset = coord
		self.hasMoved = False

	#getters
	def getCoord(self):
		return self.coord
	
	def getHasMoved(self):
		return self.hasMoved

	def getPrevCoord(self):
		return self.prevCoord

	def getColor(self):
		return self.color
	
	def getImageObj(self):
		return self.image
	
	def getIsEaten(self):
		return self.isEaten
		
	def getImageStr(self):
		return self.imgStr

	#sets boolean and returns obj
	def kill(self):
		self.isEaten = True
		return self

	#moves piece
	def move(self, coord):
		self.prevCoord = self.coord
		self.coord = coord
		#moves piece in 2d array
		self.board.movePiece(self)
		self.hasMoved = True
	
	#gets possible moves (king check included)
	def getPossibleMoves(self): 
		#gets own color's king coords
		kingCoords = self.board.getKingCoord(self.color)
		#each piece has its own getPossibleMovesNoCheck
		possibleMoves = self.getPossibleMovesNoCheck()
		legalMoves = []
		for move in possibleMoves:
			#checks if move puts king in check
				if not self.board.check(kingCoords,move,self):
					legalMoves.append(move)
		
		return legalMoves

	#raises exception if subclass doesnt have method
	def getPossibleMovesNoCheck(self): raise Exception("Undefined")

	#undraws image obj
	def undraw(self):
		if not self.undrawn:
			self.image.undraw()
			self.undrawn = True
