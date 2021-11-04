from tkinter import *
import random

fen = Tk()


def plan() -> Canvas:

    x1 = 202;
    y1 = 252;
    x2 = 998;
    y2 = 698  # coord position rectangle

    largeurrectangle = 796  # pour le recangle
    hauteurrectangle = 446

    returnThisFond = Canvas(fen, width=1200, height=800, bg="grey")  # canvas qui fait tout l'ecran
    returnThisFond.grid(row=0, columnspan=1)
    returnThisFond.create_rectangle(x1, y1, x1 + largeurrectangle, y1 + hauteurrectangle, fill="black")  # taille du rectangle
    return returnThisFond


class creationprojectile:
    def __init__(self, xpos, ypos, dirx, vy):

        self.xpos = xpos
        self.ypos = ypos

        self.dirx = dirx
        self.vy = vy

        self.sprite = fond.create_oval(self.xpos, self.ypos, self.xpos + 10, self.ypos + 10,
                                       fill="Alice blue")  # on utilise sprite pour generaliser le terme sprite en tant que objet qui bouge(bullet et ligne dans limites)

    def mouvement(self):
        fond.move(self.sprite, self.dirx, self.vy)


class projectile:
    listeprojectile = []

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def tirer(self):
        b = creationprojectile(self.xpos, self.ypos, (random.randint(-1500, 1500) / 100), 5)
        projectile.listeprojectile.append(b)


class vaisseau:

    def __init__(self, xpos, ypos, largeur, hauteur, fill):
        self.listebullet = []
        self.xpos = xpos
        self.ypos = ypos
        self.largeur = largeur
        self.hauteur = hauteur
        self.fill = fill

        self.sprite = fond.create_polygon(*self.coordvaisseau(), fill=self.fill)
        # asteriks * sert à entendre le nombre d'arguemnts limites d'une classe (6) là on est à 7 *

    def coordvaisseau(
            self):  # ça utilise le top du triangle comme cord de ref(self.xpos,self.ypos) et ça calcule les auters à partir de ça
        coord = []  # we start with an empty array
        coord.append(self.xpos)
        coord.append(self.ypos)
        coord.append(
            self.xpos + (self.largeur))  # hateur et largeur dit en bas  quand on drée objet vaisseau avec 12 et 30
        coord.append(self.ypos + self.hauteur)
        coord.append(self.xpos - (self.largeur))
        coord.append(self.ypos + self.hauteur)

        return coord
        # return car on change des coords, on souhaite obtenir quelque chose après ce def : les nouvelles coord (+ ou -)

    def mouvementsprite(self, mouvementX, mouvementY):
        newx = self.xpos + mouvementX
        newy = self.ypos + mouvementY

        if fond.winfo_x() < newx < fond.winfo_width() and fond.winfo_y() < newy < fond.winfo_height():
            self.xpos += mouvementX  # c'est donné avec 0 et +15 au def  haut bas et tout
            self.ypos += mouvementY
            fond.coords(self.sprite, *self.coordvaisseau())

    def tirerbullet(self):
        l = tirvaisseau(self.xpos - 3, self.ypos, 1, 7 / 2)  # c'est un L par un 1
        l2 = tirvaisseau(self.xpos + 3, self.ypos, 1, 7 / 2)
        fond.lift(self.sprite)
        fond.lift(
            self.sprite)  # lift sert à mettre le ligne sau premier plan pour que ca soit sur le rectangle quand ça y arrive
        self.listebullet.append(l)
        self.listebullet.append(l2)


class tirvaisseau:
    def __init__(self, xpos, ypos, dirx, vy):
        self.xpos = xpos
        self.ypos = ypos
        self.dirx = dirx
        self.vy = vy
        self.sprite = fond.create_line(self.xpos, self.ypos - 15, self.xpos, self.ypos + 20,
                                       fill='brown1')  # on reetulise sprite pareil que pour les bullets voir en haut pour explication

    def mouvement(self):
        fond.move(self.sprite, 0, self.vy * -5 / 2)  # negatif car la ligne va vers le haut


def fontaine():
    proj1.tirer()
    proj2.tirer()
    proj3.tirer()
    fen.after(40, fontaine)  # toutes les 100ms ça refait des proj


def tirencontinu():
    objetvaisseau.tirerbullet()
    fen.after(180, tirencontinu)


def limitesobjets(listeobjet):
    for obj in listeobjet:
        if (fond.coords(obj.sprite)[0] > fond.winfo_width() - 223 or fond.coords(obj.sprite)[0] < 210) or (
        # ici on utilise sprite partout pour la ligne et la balle donc
                fond.coords(obj.sprite)[1] > fond.winfo_height() - 115 or fond.coords(obj.sprite)[
            1] < 255):  # ça nous permet de mettre sprite pour correspondre à tout, sinon on aurait du faire deux limites pour balles et
            fond.delete(obj.sprite)
            # winfo_width donne la largeur max du canvas donc il fautt faire ça moins la valeur du rectangle blanc pour avoir tout bon
            listeobjet.remove(obj)
            # [0] correspond à 0 dans la liste coord soit xpos car c'est un tablerau de coord et le [1] c'est ypos


def mouvementbullet():
    limitesobjets(objetvaisseau.listebullet)
    for bullet in objetvaisseau.listebullet:
        bullet.mouvement()  # mouvement ne correspong que aux bullets du vaisseaux car il est dans tirvaisseau
    fond.focus_set()
    fen.after(10, mouvementbullet)


def mouvementballe():
    limitesobjets(projectile.listeprojectile)
    for balle in projectile.listeprojectile:
        balle.mouvement()  # comme un else, apres avoir fait limite il fait le mouvement et c'est une boucle
    fond.focus_set()
    fen.after(16, mouvementballe)


# envent=None car quand on fait un truc bind pour deplacer un objet il peut y avoir un event mais la il n'y en a pas donc None
def haut(
        event=None):  # envent=None car quand on fait un truc bind pour deplacer un objet il peut y avoir un event mais la il n'y en a pas donc None
    if coord[1] > 260:
        objetvaisseau.mouvementsprite(0, -15)


def bas(event=None):
    if coord[3] < 690:
        objetvaisseau.mouvementsprite(0, +15)


def gauche(event=None):
    if coord[4] > 220:
        objetvaisseau.mouvementsprite(-15, 0)


def droite(event=None):
    if coord[2] < 985:
        objetvaisseau.mouvementsprite(+15, 0)


def robot():
    robot = fond.create_rectangle(560, 260, 640, 280, fill="dodgerblue3")


fond = plan()

robot()
objetvaisseau = vaisseau(600, 630, 12, 30, "firebrick3")  # creation du triangle (vaisseau)
fond.bind('<Up>', haut)
fond.bind('<Down>', bas)
fond.bind('<Left>', gauche)  # assignation des touches au mouvement
fond.bind('<Right>', droite)

proj1 = projectile(565, 280)
proj2 = projectile(595, 280)
proj3 = projectile(625, 280)

mouvementbullet()
mouvementballe()
fontaine()
tirencontinu()
fen.mainloop()