# file name: Button.py
# written by: Christopher Lin
#date: 10/9/19
#button class for yahtzee and factory
from graphics import *

#button class
class Button:

	#constructor, draws button to screen
	def __init__(self, center, width, height, label, labelSize, window, backgroundColor):
		self.cx = center.getX()
		self.cy = center.getY()
		self.width = width
		self.height = height
		self.label = label
		self.isActivated = True
		self.labelSize = labelSize
		self.rect = Rectangle(Point(self.getCenterX()-self.getWidth()/2, self.getCenterY()-self.getHeight()/2),\
			Point(self.getCenterX()+self.getWidth()/2, self.getCenterY()+self.getHeight()/2))
		self.rect.setFill(backgroundColor)
		self.text = Text(Point(self.getCenterX(), self.getCenterY()), self.getLabel())
		self.text.setSize(self.getLabelSize())
		self.deactivate()
		self.fill = backgroundColor
		self.window = window

		self.rect.draw(window)
		self.text.draw(window)

	#getters

	#gets label font size
	def getLabelSize(self):
		return self.labelSize
		
	#gets button center x coord
	def getCenterX(self):
		return self.cx

	#gets button center y coord
	def getCenterY(self):
		return self.cy

	def getAnchor(self):
		return Point(self.cx, self.cy)

	#gets button width
	def getWidth(self):
		return self.width


	#gets button height
	def getHeight(self):
		return self.height

	#gets label
	def getLabel(self):
		return self.label

	#gets label color
	def getTextColor(self):
		return self.textColor

	#gets activated boolean
	def getIsActivated(self):
		return self.isActivated

	def getBackgroundColor(self):
		return self.fill

	
	#setters

	#sets border width
	def setOutlineWidth(self, width):
		self.rect.setWidth(width)


	def setOutlineColor(self, color):
		self.rect.setOutline(color)

	#sets label color
	def setTextColor(self, color):
		self.text.setTextColor(color)

	#sets activated boolean
	def setIsActivated(self, val):
		self.isActivated = val
	#sets button Color
	def setBackgroundColor(self,color):
		self.rect.setFill(color)
		self.fill = color
	#deactivates button
	def deactivate(self):
		self.setIsActivated(False)
		self.setOutlineWidth(1)
		self.setTextColor('gray')

	#activates button
	def activate(self):		
		self.setIsActivated(True)
		self.setOutlineWidth(2)
		self.setTextColor('black')

	#checks if button is clicked, returns true if clicked
	def isClicked(self, point):
		#checks if activated
		if self.getIsActivated():
			#checks if x coord is in between left most and right most pt on button and if y coord is in between highest and lowest pt on button
			if point.getX() >= self.getCenterX() - self.getWidth()/2 and point.getX() <= self.getCenterX() + self.getWidth()/2:
				if point.getY() >= self.getCenterY() - self.getHeight()/2 and point.getY() <= self.getCenterY() + self.getHeight()/2:
					return True

		return False

	def circle(self):
		self.c = Circle(self.getAnchor(), 15).draw(self.window)
		self.c.setFill(self.fill)
		self.c.setOutline(self.fill)


	def drawCircleInMiddle(self, color):
		self.c.setFill(color)
		self.c.setOutline(color)



	def undrawCircleInMiddle(self):
		self.c.setFill(self.fill)
		self.c.setOutline(self.fill)




