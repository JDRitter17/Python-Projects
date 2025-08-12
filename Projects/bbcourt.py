from graphics import *

win = GraphWin(width=1000, height=800)

for i in range(1, 4):
    x = i * 35
    for j in range(1, 5):
        y = j * 35
        print(x, y)
        body = Circle(Point(x, y), radius=10)
        body.draw(win)

win.getMouse()
win.close()
