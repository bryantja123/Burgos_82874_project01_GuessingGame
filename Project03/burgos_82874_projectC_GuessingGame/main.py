from graphics import *
from random import randrange


class GuessingGame:

    def __init__(self):

        self.v1 = Line(Point(0, 100), Point(400, 100))
        self.v2 = Line(Point(0, 200), Point(400, 200))
        self.v3 = Line(Point(0, 300), Point(400, 300))
        self.v4 = Line(Point(0, 400), Point(400, 400))
        self.h1 = Line(Point(100, 400), Point(100, 0))
        self.h2 = Line(Point(200, 400), Point(200, 0))
        self.h3 = Line(Point(300, 400), Point(300, 0))
        self.h4 = Line(Point(400, 400), Point(400, 0))
        self.v1.setOutline("black")
        self.v2.setOutline("black")
        self.v3.setOutline("black")
        self.v4.setOutline("black")
        self.h1.setOutline("black")
        self.h2.setOutline("black")
        self.h3.setOutline("black")
        self.h4.setOutline("black")
        self.v1.draw(win)
        self.v2.draw(win)
        self.v3.draw(win)
        self.v4.draw(win)
        self.h1.draw(win)
        self.h2.draw(win)
        self.h3.draw(win)
        self.h4.draw(win)


class RandomLosingSquares:

    def __init__(self):
        self.num1 = randrange(0, 16)
        self.rand = randrange(0, 16)
        self.num2 = self.rand if self.rand != self.num1 else self.rand % 15 + 1
        self.rand = randrange(0, 16)
        self.num3 = self.rand if self.rand != self.num1 and self.rand != self.num2 else self.rand % 14 + 2
        print(self.num1, self.num2, self.num3)


class GameSquares:

    def __init__(self):

        self.game_win = False
        self.canvas = []

    def gameLoop(self, ran):

        for i in range(5):
            player = win.getMouse()
            px = player.getX()
            py = player.getY()

            if (px > 0 and px <= 100 and py > 0 and py <= 100):
                pos = 0
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(0, 0), Point(100, 100))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(0, 0), Point(100, 100))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            elif (px > 100 and px <= 200 and py > 0 and py <= 100):
                pos = 1
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(100, 0), Point(200, 100))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(100, 0), Point(200, 100))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            elif (px > 200 and px <= 300 and py > 0 and py <= 100):
                pos = 2
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(200, 0), Point(300, 100))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(200, 0), Point(300, 100))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            elif (px > 300 and px <= 400 and py > 0 and py <= 100):
                pos = 3
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(300, 0), Point(400, 100))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(300, 0), Point(400, 100))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            elif (px > 0 and px <= 100 and py > 100 and py <= 200):
                pos = 4
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(0, 100), Point(100, 200))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(0, 100), Point(100, 200))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            elif (px > 100 and px <= 200 and py > 100 and py <= 200):
                pos = 5
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(100, 100), Point(200, 200))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(100, 100), Point(200, 200))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            elif (px > 200 and px <= 300 and py > 100 and py <= 200):
                pos = 6
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(200, 100), Point(300, 200))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(200, 100), Point(300, 200))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            elif (px > 300 and px <= 400 and py > 100 and py <= 200):
                pos = 7
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(300, 100), Point(400, 200))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(300, 100), Point(400, 200))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            elif (px > 0 and px <= 100 and py > 200 and py <= 300):
                pos = 8
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(0, 200), Point(100, 300))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(0, 200), Point(100, 300))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            elif (px > 100 and px <= 200 and py > 200 and py <= 300):
                pos = 9
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(100, 200), Point(200, 300))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(100, 200), Point(200, 300))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            elif (px > 200 and px <= 300 and py > 200 and py <= 300):
                pos = 10
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(200, 200), Point(300, 300))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(200, 200), Point(300, 300))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            elif (px > 300 and px <= 400 and py > 200 and py <= 300):
                pos = 11
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(300, 200), Point(400, 300))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(300, 200), Point(400, 300))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            elif (px > 0 and px <= 100 and py > 300 and py <= 400):
                pos = 12
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(0, 300), Point(100, 400))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(0, 300), Point(100, 400))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            elif (px > 100 and px <= 200 and py > 300 and py <= 400):
                pos = 13
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(100, 300), Point(200, 400))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(100, 300), Point(200, 400))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            elif (px > 200 and px <= 300 and py > 300 and py <= 400):
                pos = 14
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(200, 300), Point(300, 400))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(200, 300), Point(300, 400))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            elif (px > 300 and px <= 400 and py > 300 and py <= 400):
                pos = 15
                if (ran.num3 == pos or ran.num2 == pos or ran.num1 == pos):
                    r = Rectangle(Point(300, 300), Point(400, 400))
                    r.setFill('red')
                    r.setOutline('black')
                    r.draw(win)
                    self.canvas.append(r)
                    self.game_win = False
                    break

                else:
                    r1 = Rectangle(Point(300, 300), Point(400, 400))
                    r1.setFill('green')
                    r1.setOutline('black')
                    r1.draw(win)
                    self.canvas.append(r1)

            if i == 4:
                self.game_win = True

    def unDraw(self, grid):

        grid.v1.undraw()
        grid.v2.undraw()
        grid.v3.undraw()
        grid.v4.undraw()
        grid.h1.undraw()
        grid.h2.undraw()
        grid.h3.undraw()
        grid.h4.undraw()
        for r in self.canvas:
            r.undraw()

    def message(self):

        message = Text(Point(200, 200), 'G O O D   G A M E' if self.game_win else 'G A M E   O V E R')
        message.setSize(32)
        message.setFace('times roman')
        message.draw(win)



def main():

    global win
    window_size = 400

    win = GraphWin("Burgos_82874, GAME!", window_size, window_size)

    grid = GuessingGame()
    random_numbers = RandomLosingSquares()
    player_input = GameSquares()
    player_input.gameLoop(random_numbers)
    player_input.unDraw(grid)
    player_input.message()

    win.getMouse()


main()
