from graphics import *
import random
win = GraphWin(width = 1000,height = 800)
cir = Circle(Point(500, 400), radius = 100)
cir.setFill(color_rgb(210, 180,140))
cir.draw(win)
cir2 = Circle(Point(500, 400), radius = 85)
cir2.setFill(color_rgb(255, 255, 0))
cir2.draw(win)

for i in range(15):
    x = random.randrange(450, 550)
    y = random.randrange(340, 450)
    pep=Circle(Point(x, y), radius =10)
    pep.setFill(color_rgb(255, 0, 0))
    pep.draw(win)

win.getMouse()