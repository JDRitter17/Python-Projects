from graphics import *

win = GraphWin('Balley', width=1000, height=500)
ball = Image(Point(100, 100), "C:\\Users\\jritter\\Desktop\\tennis-tennis-ball.gif")
dogg = Image(Point(500, 250), "C:\\Users\\jritter\\Desktop\\dogg.gif")
ball.draw(win)
dogg.draw(win)


win.setBackground("White")

win.getMouse()