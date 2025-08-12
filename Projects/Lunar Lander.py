from graphics import *
import time
import random

# Setup window
win = GraphWin('Lunar Lander', width=1000, height=500)
win.setBackground("black")

# Initial velocities and gravity
vx = 0
vy = 0
gravity = 0.15

# Draw the moon surface
moon = Rectangle(Point(0, 400), Point(1000, 500))
moon.setFill('grey')
moon.draw(win)

# Draw stars randomly
for _ in range(35):
    x = random.randrange(20, 980)
    y = random.randrange(20, 350)
    star = Circle(Point(x, y), radius=4)
    star.setFill(color_rgb(255, 255, 255))
    star.draw(win)

# Draw capsule (the lander)
capsule = Rectangle(Point(100, 100), Point(200, 200))
capsule.setFill('red')
capsule.draw(win)

# Explosion graphic (hidden until needed)
explosion = Circle(Point(150, 150), radius=200)
explosion.setFill("orange")

flame = False
flames = None  # We'll create this dynamically

while True:
    vy += gravity
    time.sleep(0.05)
    key = win.checkKey()

    # Controls and flame management
    if key == "w":
        vy -= 0.3

        # Remove old flame if exists
        if flame and flames:
            flames.undraw()

        # Recreate and draw flame anchored to capsule bottom
        capsule_center = capsule.getCenter()
        capsule_p1 = capsule.getP1()
        capsule_p2 = capsule.getP2()

        flame_base_y = capsule_p2.getY()
        flame_width = capsule_p2.getX() - capsule_p1.getX()

        flames = Polygon(
            Point(capsule_center.getX() - flame_width / 2, flame_base_y),
            Point(capsule_center.getX(), flame_base_y + 100),
            Point(capsule_center.getX() + flame_width / 2, flame_base_y)
        )
        flames.setFill("orange")
        flames.draw(win)
        flame = True

    else:
        if flame and flames:
            flames.undraw()
            flame = False

    if key == "a":
        vx -= 1
    elif key == "d":
        vx += 1

    # Move capsule and explosion
    capsule.move(vx, vy)
    explosion.move(vx, vy)

    # Boundaries - left edge
    if capsule.getP1().getX() <= 0:
        capsule.move(1, 0)
        vx = 0
        crash_text = Text(Point(100, 100), "The rocket has Crashed")
        crash_text.setTextColor("white")
        explosion.draw(win)
        crash_text.draw(win)
        break

    # Boundaries - right edge
    if capsule.getP2().getX() >= win.getWidth():
        capsule.move(-1, 0)
        vx = 0
        crash_text = Text(Point(100, 100), "The rocket has Crashed")
        crash_text.setTextColor("white")
        explosion.draw(win)
        crash_text.draw(win)
        break

    # Landing zone Y boundary correction
    if capsule.getCenter().getY() >= 350:
        capsule.move(0, -(capsule.getCenter().getY() - 350))

        landing_velocity = abs(vy)

        # Check landing conditions
        if landing_velocity > 5:
            crash_text = Text(Point(100, 100), "The rocket has Crashed")
            crash_text.setTextColor("white")
            explosion.draw(win)
            crash_text.draw(win)
            break
        else:
            land_text = Text(Point(100, 100), "The rocket has landed")
            land_text.setTextColor("white")
            land_text.draw(win)
            vy = 0
            vx = 0
            if flame and flames:
                flames.undraw()
                flame = False
            break

win.getMouse()
win.close()
