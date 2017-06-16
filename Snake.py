from p5 import *
import math

def setup():
    global window, grid, snake
    window = CreateWindow(630, 480,resizable=False)
    caption("hey!")
    background(51)
    grid = Grid(window)
    snake = Snake()

def draw():
    global grid,snake
    background(name="white")
    grid.draw()
    snake.update()


def KeyPressed():
    global snake
    if key == "LEFT":
        if not snake.direction == "EAST":
            snake.direction = "WEST"
    if key == "RIGHT":
        if not snake.direction == "WEST":
            snake.direction = "EAST"
    if key == "UP":
        if not snake.direction == "SOUTH":
            snake.direction = "NORTH"
    if key == "DOWN":
        if not snake.direction == "NORTH":
            snake.direction = "SOUTH"

class Grid:
    def __init__(self,window):
        self.width = window.width
        self.height = window.height
        self.squares = []
        r,c=0,0
        for x in range(0,self.width,30):
            r = 0
            c += 1
            for y in range(0,self.height,30):
                fill(255)
                self.squares.append(square(x,y,r,c))
                r += 1
        self.respawn()


    def draw(self):
        for i in self.squares:
            i.draw()

    def respawn(self):
        random(self.squares).apple = True

class square:
    def __init__(self,x,y,r,c):
        self.x = x
        self.y = y
        self.r = r
        self.c = c
        self.snake = False
        self.apple = False

    def draw(self):
        if self.snake:
            fill(name="limegreen")
        elif self.apple:
            fill(name="red")
        else:
            fill(51)
        rect(self.x,self.y,29,29)

class Snake:
    def __init__(self):
        self.headx = int(random(0,21))
        self.heady = int(random(0,16))
        self.direction = random(["NORTH","EAST","SOUTH","WEST"])
        self.coords = []
        self.length = 5

    def update(self):
        global grid

        if self.direction == "NORTH":
            self.heady += 1
        if self.direction == "SOUTH":
            self.heady -= 1            
        if self.direction == "EAST":
            self.headx += 1
        if self.direction == "WEST":
            self.headx -= 1    

        if self.headx > 21:
            self.headx = 1
        if self.headx < 1:
            self.headx = 21
        if self.heady > 15:
            self.heady = 0
        if self.heady < 0:
            self.heady = 15


        if [self.headx,self.heady] in self.coords:
            exit()

        self.coords.insert(0,[self.headx,self.heady])
        end = None
        if len(self.coords) > self.length:
            end = self.coords.pop()


        for i in grid.squares:
            if i.r == self.heady and i.c == self.headx:
                i.snake = True
            if end != None:
                if i.r == end[1] and i.c == end[0]:
                    i.snake = False
            if i.apple and i.r == self.heady and i.c == self.headx:
                i.apple = False
                grid.respawn()
                self.length += 1






        
