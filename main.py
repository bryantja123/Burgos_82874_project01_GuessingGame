from graphics import *


def main():
    global win
    win = GraphWin("Burgos_82874, GAME!", 600, 600)
    prepare_game()
    losing_squares()
    rectangle_entries()

#commit change test
#commit change test2


def rectangle_entries():

    for i in range(10):
        p = win.getMouse()
        x1 = p.getX() - 10
        y1 = p.getY() - 10
        x2 = p.getX() + 10
        y2 = p.getY() + 10
        r = Rectangle(Point(x1, y1), Point(x2, y2))
        r.setFill("red")
        r.setOutline("red")
        r.setWidth(0)
        r.draw(win)

def losing_squares():


    for i in range(10):
        r = Rectangle(Point(20, 20), Point(40, 40))
        r.setFill("red")
        r.setOutline("red")
        r.setWidth(0)
        r.draw(win)


def prepare_game():

    v1 = Line(Point(100, 100), Point(500, 100))
    v2 = Line(Point(100, 200), Point(500, 200))
    v3 = Line(Point(100, 300), Point(500, 300))
    v4 = Line(Point(100, 400), Point(500, 400))
    v5 = Line(Point(100, 500), Point(500, 500))


    h1 = Line(Point(100, 500), Point(100, 100))
    h2 = Line(Point(200, 500), Point(200, 100))
    h3 = Line(Point(300, 500), Point(300, 100))
    h4 = Line(Point(400, 500), Point(400, 100))
    h5 = Line(Point(500, 500), Point(500, 100))


    v1.setOutline("black")
    v2.setOutline("black")
    v3.setOutline("black")
    v4.setOutline("black")
    v5.setOutline("black")


    h1.setOutline("black")
    h2.setOutline("black")
    h3.setOutline("black")
    h4.setOutline("black")
    h5.setOutline("black")


    v1.draw(win)
    v2.draw(win)
    v3.draw(win)
    v4.draw(win)
    v5.draw(win)


    h1.draw(win)
    h2.draw(win)
    h3.draw(win)
    h4.draw(win)
    h5.draw(win)



main()
