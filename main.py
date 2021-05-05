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

    # win.getMouse()

    for i in range(5):
        player = win.getMouse()
        px = player.getX()
        py = player.getY()

        if (px > 0 and px <= 100 and py > 0 and py <= 100):
            r = Rectangle(Point(0, 100), Point(100, 0))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)
        elif ():
            r = Rectangle(Point(0, 100), Point(100, 0))
            r.setFill('green')
            r.setOutline('black')
            r.draw(win)


main()
