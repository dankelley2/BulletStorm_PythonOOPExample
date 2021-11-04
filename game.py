from tkinter import *
import math
import random
from sprites import Sprite

particleList = [] #this keeps track of EVERY background particle (star) we have on the screen
bulletList = [] #this keeps track of every bullet line we have on the screen
BreakGame = False

class Bullet:   # Classes are used to make objects. This one bullet class is used for all of the "bullets". By using
                # this we avoid having to make "Bullet1","Bullet2","Bullet795" etc...
    def __init__(self, xpos, ypos, vx, vy):
        '''
            "__init__" is a special function built into python. Most programming languages have their own special word for
            this function. It's special, because EVERY time you create a *new* object (a new Bullet, in this example), this
            is the very first thing that runs. The word "init" stands for initiate (ou "initier" en francais, je pense). It
            is the UNIVERSAL "setup" function for every object, and it runs even if you don't type it you will see this in
            almost every python example.
        '''
        self.xpos = xpos
        self.ypos = ypos
        self.vx = vx
        self.vy = vy
        self.sprite = canvas.create_line(self.xpos, self.ypos, self.xpos + vx, self.ypos + 10, fill='red')

    def move(self):
        canvas.move(self.sprite, self.vx, self.vy)

class BackgroundParticle:
    def __init__(self, parentCanvas):
        self.v_speed = (random.random()*3)+1
        r = random.random()
        self.sprite = canvas.create_line(parentCanvas.winfo_width() * r, -2, parentCanvas.winfo_width() * r, 0, fill='grey')
        particleList.append(self)

    def move(self):
        canvas.move(self.sprite, 0, self.v_speed)

class playerShip:
    dx = 0
    dy = 0
    def __init__(self, xpos, ypos, sprite):
        self.xpos = xpos
        self.ypos = ypos

        self.sprite = canvas.create_image(self.xpos, self.ypos, image=sprite.img)

    def Shoot(self):
        random.Random()
        b = Bullet(self.xpos, self.ypos, (random.randint(-25, 25) / 100), min(-5 + self.dy,-2))
        bulletList.append(b)

    def MoveToTarget(self,x,y):
        self.dx = self.xpos - x
        self.dy = self.ypos - y
        
        self.dx = -self.dx / 10
        self.dy = -self.dy / 10

        self.xpos,self.ypos = self.xpos + self.dx, self.ypos + self.dy
        canvas.coords(self.sprite, self.xpos, self.ypos)


def motionCallback(event):
    x, y = event.x, event.y
    pShip.MoveToTarget(x, y)


def CreateSoManyBullets():
    pShip.Shoot()
    root.after(75, CreateSoManyBullets)

def AnimateBullets():
    for b in bulletList:
        if (canvas.coords(b.sprite)[0] > canvas.winfo_width() or canvas.coords(b.sprite)[0] < 0) or (
                canvas.coords(b.sprite)[1] > canvas.winfo_height() or canvas.coords(b.sprite)[1] < 25):
            canvas.delete(b.sprite)
            bulletList.remove(b)
        else:
            b.move()

def CreateStars():
    star = BackgroundParticle(canvas)

def AnimateStars():
    for s in particleList:
        if canvas.coords(s.sprite)[1] > canvas.winfo_height()-50:
            canvas.delete(s.sprite)
            particleList.remove(s)
        else:
            s.move()

def Animate():
    AnimateBullets()
    if random.randint(1,3) == 3:
        CreateStars()
    AnimateStars()
    canvas.focus_set()
    root.after(16, Animate)

def Break(event=None):
    global BreakGame
    BreakGame = True


root = Tk()
canvas = Canvas(root, width=400, height=800, bg='black')
pShipSprite = Sprite('img/ship1.png')
pShip = playerShip(50, 200, pShipSprite)


canvas.bind('<Motion>', motionCallback)
# canvas.bind('<Up>', haut)
# canvas.bind('<Down>', bas)
# canvas.bind('<Left>', gauche)  # assignation des touches au mouvement
# canvas.bind('<Right>', droite)
canvas.bind('<space>', Break)
root.config()
canvas.pack()

Animate()   #start animation loop
CreateSoManyBullets()
root.mainloop()