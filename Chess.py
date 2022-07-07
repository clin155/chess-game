# File: Chess.py
# By: Christopher Lin
# Date: 2/10/20
# main runner function

from graphics import *
from BoardGUI import *
from RookBishopQueen import *
from ChessGUI import *
from KingKnight import *
from Pawn import *


#main function
def main():
	chessGUI = ChessGUI()
	#board - board obj, boardList - 2d array
	board = chessGUI.getBoard()
	boardList = chessGUI.getBoard().getBoardList()
	checkMate = False
	playing = True
	while playing:
		initPieces(chessGUI)
		#game starts on white
		turnColor = "white"
		while not checkMate:
			#clickedcoord is tile user clicked
			clickedCoord = chessGUI.turn()
			#only -1,-1 if quit clicked
			if clickedCoord != (-1,-1):
				pieceClicked = boardList[clickedCoord[0]][clickedCoord[1]]
				moveList = pieceClicked.getPossibleMoves()
				#only passes if moveList != []
				if moveList:
					clickedCoord = chessGUI.drawMove(moveList)
					#if quit clicked
					if clickedCoord == (-1,-1):
						playing = False
						break
					#if user clicked outside possible moves
					elif clickedCoord == None:
						pass
					else:
						#if user clicked opposing piece or castling move
						if boardList[clickedCoord[0]][clickedCoord[1]] != None:
							if boardList[clickedCoord[0]][clickedCoord[1]].getColor() == turnColor:
								castlingMove(board, pieceClicked, chessGUI,clickedCoord, turnColor)
							else:
								killedPiece = boardList[clickedCoord[0]][clickedCoord[1]].kill()
								#playAgain: boolean if user wants to play again
								playAgain = updateAndCheckPromotion([pieceClicked, killedPiece], pieceClicked, clickedCoord, chessGUI, turnColor, board,"captured")
								if playAgain == False:
									playing = False
									break
								elif playAgain == True: break
						else:
							playAgain = updateAndCheckPromotion([pieceClicked], pieceClicked, clickedCoord, chessGUI, turnColor, board, "move")
							if playAgain == False:
								playing = False
								break
							elif playAgain == True: break
						#toggles color
						turnColor = toggleColor(turnColor)
				else:
					#update with message of no possible moves
					chessGUI.update([],"", 2, None)
			#if user clicked quit button
			else:
				playing = False
				break


#inits pieces
def initPieces(chessGUI):
	board = chessGUI.getBoard()
	initNonPawns(0,board,"black")
	initPawns(1,board,"black")
	initNonPawns(7,board, "white")
	initPawns(6,board,"white")
	#updates gui/draws pieces from array
	chessGUI.reset()

#creates 8 pawn objs
def initPawns(row,board,color):
	for i in range(8):
		Pawn((row,i),board, color,"pawn_"+color+".gif")

#adds all non pawn pieces
def initNonPawns(row,board,color):
	Rook((row,0),board,color,"rook_"+color+".gif")
	Knight((row,1),board,color,"horse_"+color+".gif")
	Bishop((row,2),board, color,"bishop_"+color+".gif")
	Queen((row,3),board,color,"queen_"+color+".gif")
	King((row,4),board,color,"king_"+color+".gif")
	Bishop((row,5),board, color, "bishop_"+color+".gif")
	Knight((row,6),board, color, "horse_"+color+".gif")
	Rook((row,7),board, color, "rook_"+color+".gif")

#returns int depending on check, checkmate, or none
def checkForCheck(turnColor, board, piece):
	checking = 2
	if isCheck(turnColor, board, piece): checking = 0
	if isCheckMate(toggleColor(turnColor), board.getBoardList()): checking = 1
	return checking

#returns boolean if checkmate
def isCheckMate(color,board):
	for row in range(len(board)):
		for col in range(len(board[0])):
			if board[row][col] != None and board[row][col].getColor() == color:
				piece = board[row][col]
				#gets possible moves for every piece and checks if list is empty
				if piece.getPossibleMoves() != []:
					return False
	return True

#checks if piece puts king in check 
def isCheck(color, board, piece):
	for i in piece.getPossibleMovesNoCheck():
		if i == board.getKingCoord(toggleColor(color)):
			return True
	return False

#toggles color
def toggleColor(color):
	if color == "white": return "black"
	else: return "white"

#handles castle moves
def castlingMove(board, pieceClicked, chessGUI, clickedCoord, turnColor):
	rook = board.getBoardList()[clickedCoord[0]][clickedCoord[1]]
	rookCoord = rook.getCoord()
	kingCoord = pieceClicked.getCoord()
	#if left side castle
	if rookCoord[1] < kingCoord[1]:
		pieceClicked.move((kingCoord[0],kingCoord[1]-2))
		rook.move((kingCoord[0],kingCoord[1]-1))
	else:
		#right side castle
		pieceClicked.move((kingCoord[0],kingCoord[1]+2))
		rook.move((kingCoord[0],kingCoord[1]+1))
	#updates gui
	chessGUI.update([pieceClicked,rook], "castled", checkForCheck(turnColor, board, pieceClicked), None)

#checks if piece promoted and updates gui
def updateAndCheckPromotion(changedPieces, pieceClicked, clickedCoord, chessGUI, turnColor, board, typee):
	promotion = pieceClicked.move(clickedCoord)
	playAgain = chessGUI.update(changedPieces, typee, checkForCheck(turnColor, board, pieceClicked), promotion)
	return playAgain
	
main()