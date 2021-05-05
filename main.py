from graphics import *


def main():
    global win

    window_size = 400
    squares = 4

    win = GraphWin("Burgos_82874, GAME!", window_size, window_size)

    for i in range(squares - 1):
        h_line = Line(Point(0, (window_size / squares) * (i + 1)), Point(window_size, (window_size / squares) * (i + 1)))
        h_line.draw(win)
        v_line = Line(Point((window_size / squares) * (i + 1), 0), Point((window_size / squares) * (i + 1), window_size))
        v_line.draw(win)


    for i in range(5):
        player = win.getMouse()
        px = player.getX()
        py = player.getY()

        if (px > 0 and px <= 100 and py > 0 and py <= 100):
            r = Rectangle(Point(0, 0), Point(100, 100))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)

        elif (px > 100 and px <= 200 and py > 0 and py <= 100):
            r = Rectangle(Point(100, 0), Point(200, 100))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)

        elif (px > 200 and px <= 300 and py > 0 and py <= 100):
            r = Rectangle(Point(200, 0), Point(300, 100))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)

        elif (px > 300 and px <= 400 and py > 0 and py <= 100):
            r = Rectangle(Point(300, 0), Point(400, 100))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)

        elif (px > 0 and px <= 100 and py > 100 and py <= 200):
            r = Rectangle(Point(0, 100), Point(100, 200))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)

        elif (px > 100 and px <= 200 and py > 100 and py <= 200):
            r = Rectangle(Point(100, 100), Point(200, 200))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)

        elif (px > 200 and px <= 300 and py > 100 and py <= 200):
            r = Rectangle(Point(200, 100), Point(300, 200))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)

        elif (px > 300 and px <= 400 and py > 100 and py <= 200):
            r = Rectangle(Point(300, 100), Point(400, 200))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)

        elif (px > 0 and px <= 100 and py > 200 and py <= 300):
            r = Rectangle(Point(0, 200), Point(100, 300))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)

        elif (px > 100 and px <= 200 and py > 200 and py <= 300):
            r = Rectangle(Point(100, 200), Point(200, 300))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)

        elif (px > 200 and px <= 300 and py > 200 and py <= 300):
            r = Rectangle(Point(200, 200), Point(300, 300))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)

        elif (px > 300 and px <= 400 and py > 200 and py <= 300):
            r = Rectangle(Point(300, 200), Point(400, 300))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)

        elif (px > 0 and px <= 100 and py > 300 and py <= 400):
            r = Rectangle(Point(0, 300), Point(100, 400))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)

        elif (px > 100 and px <= 200 and py > 300 and py <= 400):
            r = Rectangle(Point(100, 300), Point(200, 400))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)

        elif (px > 200 and px <= 300 and py > 300 and py <= 400):
            r = Rectangle(Point(200, 300), Point(300, 400))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)

        elif (px > 300 and px <= 400 and py > 300 and py <= 400):
            r = Rectangle(Point(300, 300), Point(400, 400))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)



main()
