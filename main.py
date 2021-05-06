from graphics import *
from random import randrange


def main():
    global win

    window_size = 400
    squares = 4
    game_loss = False


    win = GraphWin("Burgos_82874, GAME!", window_size, window_size)

    for i in range(squares - 1):
        h_line = Line(Point(0, (window_size / squares) * (i + 1)), Point(window_size, (window_size / squares) * (i + 1)))
        h_line.draw(win)
        v_line = Line(Point((window_size / squares) * (i + 1), 0), Point((window_size / squares) * (i + 1), window_size))
        v_line.draw(win)

    num1 = randrange(0, 16)
    rand = randrange(0, 16)
    num2 = rand if rand != num1 else rand % 15 + 1
    rand = randrange(0, 16)
    num3 = rand if rand != num1 and rand != num2 else rand % 14 + 2
    pos = 0

    print(num1, num2, num3)

    for i in range(5):
        player = win.getMouse()
        px = player.getX()
        py = player.getY()

        if (px > 0 and px <= 100 and py > 0 and py <= 100):
                pos = 0
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(0, 0), Point(100, 100))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(0, 0), Point(100, 100))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        elif (px > 100 and px <= 200 and py > 0 and py <= 100):
                pos = 1
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(100, 0), Point(200, 100))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(100, 0), Point(200, 100))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        elif (px > 200 and px <= 300 and py > 0 and py <= 100):
                pos = 2
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(200, 0), Point(300, 100))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(200, 0), Point(300, 100))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        elif (px > 300 and px <= 400 and py > 0 and py <= 100):
                pos = 3
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(300, 0), Point(400, 100))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(300, 0), Point(400, 100))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        elif (px > 0 and px <= 100 and py > 100 and py <= 200):
                pos = 4
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(0, 100), Point(100, 200))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(0, 100), Point(100, 200))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        elif (px > 100 and px <= 200 and py > 100 and py <= 200):
                pos = 5
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(100, 100), Point(200, 200))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(100, 100), Point(200, 200))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        elif (px > 200 and px <= 300 and py > 100 and py <= 200):
                pos = 6
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(200, 100), Point(300, 200))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(200, 100), Point(300, 200))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        elif (px > 300 and px <= 400 and py > 100 and py <= 200):
                pos = 7
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(300, 100), Point(400, 200))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(300, 100), Point(400, 200))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        elif (px > 0 and px <= 100 and py > 200 and py <= 300):
                pos = 8
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(0, 200), Point(100, 300))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(0, 200), Point(100, 300))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        elif (px > 100 and px <= 200 and py > 200 and py <= 300):
                pos = 9
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(100, 200), Point(200, 300))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(100, 200), Point(200, 300))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        elif (px > 200 and px <= 300 and py > 200 and py <= 300):
                pos = 10
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(200, 200), Point(300, 300))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(200, 200), Point(300, 300))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        elif (px > 300 and px <= 400 and py > 200 and py <= 300):
                pos = 11
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(300, 200), Point(400, 300))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(300, 200), Point(400, 300))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        elif (px > 0 and px <= 100 and py > 300 and py <= 400):
                pos = 12
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(0, 300), Point(100, 400))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(0, 300), Point(100, 400))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        elif (px > 100 and px <= 200 and py > 300 and py <= 400):
                pos = 13
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(100, 300), Point(200, 400))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(100, 300), Point(200, 400))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        elif (px > 200 and px <= 300 and py > 300 and py <= 400):
                pos = 14
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(200, 300), Point(300, 400))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(200, 300), Point(300, 400))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        elif (px > 300 and px <= 400 and py > 300 and py <= 400):
                pos = 15
                if(num3 == pos or num2 == pos or num1 == pos):
                    r = Rectangle(Point(300, 300), Point(400, 400))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    game_loss = True

                else:
                    r = Rectangle(Point(300, 300), Point(400, 400))
                    r.setFill('green')
                    r.setOutline('black')
                    r.draw(win)

        if game_loss:


            h_line.undraw()
            v_line.undraw()
            r.undraw()

    # win.close()

main()
