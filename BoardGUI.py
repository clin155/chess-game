# File: Piece.py
# By: Christopher Lin
# Date: 2/10/20
# board class, also draws board to screen

from Button import *
from KingKnight import *
from Piece import *
from RookBishopQueen import *

#board class
class Board():
	def __init__(self, window, winWidth,winHeight):
		self.nSquares = 8
		self.buttonList = []
		self.window = window
		self.winWidth = winWidth
		self.winHeight = winHeight
		self.vertMargin = 40
		self.hortMargin = 40
		self.boardList = None
		self.createBoardList()
		self.draw()
		self.moveTiles = []

	#returns row, col of the square clicked
	def getSquareClicked(self,click):
		for row in range(len(self.buttonList)):
			for col in range(len(self.buttonList[0])):
				if self.buttonList[row][col].isClicked(click):
					return row, col
		return -1,-1
	
	#getters
	def getButtonList(self):
		return self.buttonList
	
	def getBoardList(self):
		return self.boardList

	#creates 2d array for pieces
	def createBoardList(self):
		self.boardList = []
		bigList = []
		#creates nSquares x nSquares 2d list
		for i in range(self.nSquares):
			listt = []
			for i in range(self.nSquares):
				listt.append(None)
			bigList.append(listt)
		self.boardList = bigList

	#sets tile color of coord
	def setTileColor(self,coord):
		#adds tile and current color to array
		self.moveTiles.append((self.buttonList[coord[0]][coord[1]], self.buttonList[coord[0]][coord[1]].getBackgroundColor()))
		if self.boardList[coord[0]][coord[1]] != None:
			#castle or eating a piece turns tile pink
			self.buttonList[coord[0]][coord[1]].setBackgroundColor('pink')
		else:
			#all other possible moves have circle
			self.buttonList[coord[0]][coord[1]].drawCircleInMiddle('slategray')

	#resets all tiles to green and white
	def resetTileColors(self):
		color = color_rgb(119,149,86)
		for row in range(len(self.buttonList)):
			for col in range(len(self.buttonList[0])):
				self.buttonList[row][col].setBackgroundColor(color)
				self.buttonList[row][col].setOutlineWidth(0)
				color = self.toggleColor(color)
			color = self.toggleColor(color)

	#resets move tiles to green and white
	def resetMoveTiles(self):
		for i in self.moveTiles:
			i[0].setBackgroundColor(i[1])
			i[0].undrawCircleInMiddle()
		self.moveTiles = []

	#inits tiles
	def draw(self):
		sqLength = (self.winHeight - (2*self.vertMargin))//self.nSquares
		color = color_rgb(119,149,86)
		for i in range(self.nSquares):
			listt = []
			for j in range(self.nSquares):
				#converts row,col (i,j) to coords
				x = self.hortMargin + (j*sqLength)
				y = self.vertMargin + (i*sqLength)
				button = Button(Point(x+sqLength//2,y+sqLength//2),sqLength,sqLength,"",10,self.window,color)
				button.activate()
				button.setOutlineWidth(0)
				#adds circle for drawing possible moves
				button.circle()
				listt.append(button)
				color = self.toggleColor(color)
			self.buttonList.append(listt)
			#toggles after each row to alternate colors
			color = self.toggleColor(color)
	
	#gets king's coords with color parameter
	def getKingCoord(self,color):
		for row in range(len(self.boardList)):
			for col in range(len(self.boardList[0])):
				if type(self.boardList[row][col]) == King and self.boardList[row][col].getColor() == color:
					return row, col
		#returns -1,-1 if no king
		return -1,-1

	#moves piece in board list
	def movePiece(self,piece):
		self.boardList[piece.getCoord()[0]][piece.getCoord()[1]] = piece
		#sets piece's prev coords
		if piece.getPrevCoord() != None:
			self.boardList[piece.getPrevCoord()[0]][piece.getPrevCoord()[1]] = None

	#promotes pawn
	def promotion(self, pawn):
		#replaces pawn with queen at pawn's coords
		self.boardList[pawn.getCoord()[0]][pawn.getCoord()[1]] = Queen(pawn.getCoord(), self, pawn.getColor(), "queen_"+pawn.getColor()+".gif")
		pawn.kill()
		pawn.undraw()
		self.boardList[pawn.getCoord()[0]][pawn.getCoord()[1]].getImageObj().draw(self.window)

	#gets castling moves for king
	def getCastleMoves(self,king):
		castleMoves = []
		for row in range(len(self.boardList)):
			for col in range(len(self.boardList[0])):
				piece = self.boardList[row][col]
				#looks for a rook in boardlist with king's color that hasn't moved
				if type(piece) == Rook and piece.getColor() == king.getColor() and piece.getHasMoved() == False:
					rookCoord = piece.getCoord()
					kingCoord = king.getCoord()
					canCastle = True
					#left side castle
					if rookCoord[1] < kingCoord[1]:
						#checks king's spaces aren't in check
						for i in range(kingCoord[1]-2,kingCoord[1]+1):
							if self.check((kingCoord[0],i),(kingCoord[0],i),king):
								canCastle = False
						#checks that spaces inbetween king and rook are empty
						for i in range(rookCoord[1],kingCoord[1]+1):
							if self.boardList[kingCoord[0]][i] != None:
								if self.boardList[kingCoord[0]][i] != king and self.boardList[kingCoord[0]][i] != piece:
									canCastle = False
					#right side castle
					else:
						#checks king's spaces aren't in check
						for i in range(kingCoord[1],kingCoord[1]+3):
							if self.check((kingCoord[0],i),(kingCoord[0],i),king):
								canCastle = False	
						#checks that spaces inbetween king and rook are empty			
						for i in range(kingCoord[1],rookCoord[1]+1):
							if self.check((kingCoord[0],i),(kingCoord[0],i),king):
								canCastle = False
							if self.boardList[kingCoord[0]][i] != None:
								if self.boardList[kingCoord[0]][i] != king and self.boardList[kingCoord[0]][i] != piece:
									canCastle  = False
					#adds rook's coords to array if can castle
					if canCastle:				
						castleMoves.append(rookCoord)
		return castleMoves

	#handles if king is in check if piece parameter were to go to move coord
	def check(self,kingCoord,move,piece):
		#gets piece at move location
		prevPiece = self.boardList[move[0]][move[1]]
		#moves piece in board
		self.boardList[move[0]][move[1]] = piece
		self.boardList[piece.getCoord()[0]][piece.getCoord()[1]] = None
		for row in range(len(self.boardList)):
			for col in range(len(self.boardList[0])):
				if self.boardList[row][col] != None:
					#goes through every piece not king's color
					if self.boardList[row][col].getColor() != piece.getColor():
						#checks if king's coord's in possible moves of piece, getPossibleMoves without check to prevent infinite loop
						moveList = self.boardList[row][col].getPossibleMovesNoCheck()
						for mov in moveList:
							if mov == kingCoord:
								#moves piece back to original location
								self.boardList[move[0]][move[1]] = prevPiece
								self.boardList[piece.getCoord()[0]][piece.getCoord()[1]] = piece
								return True
		#moves piece back to original location
		self.boardList[move[0]][move[1]] = prevPiece
		self.boardList[piece.getCoord()[0]][piece.getCoord()[1]] = piece
		return False

	#toggles color
	def toggleColor(self, color):
		if color == color_rgb(119,149,86):
			return color_rgb(235,236,208)
		else:
			return color_rgb(119,149,86)
