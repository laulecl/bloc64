from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QGraphicsPixmapItem, QGraphicsView
from PyQt6.QtCore import QTimer
from .Bloc import Bloc


class Plateau:

    def __init__(self, jeu, widget: QGraphicsView):
        self.jeu = jeu
        self.widget = widget

        self.lignes = 22
        self.colonnes = 13

        self.perdu = None
        self.pause = None


    def preparer(self):
        self.grille = [[None for _ in range(self.colonnes+1)] for _ in range(-5,self.lignes+2)]

        self.largeur = self.colonnes * self.jeu.theme.stepWidth + self.jeu.theme.decalageWidth
        self.hauteur = self.lignes * self.jeu.theme.stepHeight + self.jeu.theme.decalageHeight

        if self.jeu.mode == self.jeu.MODE_HEXA:
            self.largeur += round(self.jeu.theme.stepWidth / 3)
            self.hauteur += round(self.jeu.theme.stepHeight * 0.95)

        self.scene = QtWidgets.QGraphicsScene(self.widget)
        self.scene.setSceneRect(0, 0, self.largeur, self.hauteur)
        self.widget.setScene(self.scene)

        self.fond = QGraphicsPixmapItem(self.jeu.theme.fond)
        self.fond.setZValue(0)
        self.scene.addItem(self.fond)

        if self.jeu.mode == self.jeu.MODE_HEXA:
            for y in range(-5,self.lignes+2):
                self.nouvelleCase(0,0,y)
                self.nouvelleCase(0, self.colonnes+1, y)

            for x in range(1,self.colonnes+1):
                self.nouvelleCase(0, x, self.lignes + 1)


    def nouvelleCase(self, index: int, x: int, y: int) -> Bloc:
        bloc = Bloc(self, index, x, y)
        self.scene.addItem(bloc.pixmap)
        self.placerCase(bloc)

        return bloc


    def libre(self, x: int, y: int) -> bool:
        if x < 1:
            return False

        if x > self.colonnes:
            return False

        if y < -5:
            return False

        if y > self.lignes:
            return False

        return self.grille[y][x] == None


    def placerCase(self, bloc: Bloc):
        posX = (bloc.x-1) * self.jeu.theme.stepWidth - self.jeu.theme.decalageX
        posY = (bloc.y-1) * self.jeu.theme.stepHeight - self.jeu.theme.decalageY

        if self.jeu.mode == self.jeu.MODE_HEXA:
            posX += round(self.jeu.theme.stepWidth / 6)

        if bloc.x % 2 == 0:
            posY += self.jeu.theme.decalageHeight

        if bloc.index > 0:
            if self.grille[bloc.lastY][bloc.lastX] == bloc:
                self.grille[bloc.lastY][bloc.lastX] = None

            self.grille[bloc.y][bloc.x] = bloc

        bloc.pixmap.setPos(posX, posY)


    def viderCase(self, x, y):
        if self.grille[y][x] != None:
            self.scene.removeItem(self.grille[y][x].pixmap)
            self.grille[y][x] = None


    def vider(self):
        if self.perdu != None:
            self.scene.removeItem(self.perdu)

        for y in range(-5,self.lignes+1):
            for x in range(1,self.colonnes+1):
                self.viderCase(x, y)


    def printGrille(self):

        for y in range(0, self.lignes+1):
            print("|", end='')
            for x in range(1,self.colonnes+1):
                if self.grille[y][x] == None:
                    print('.', end=' ')
                else:
                    print(str(self.grille[y][x].index), end=' ')
            print("|")

        print('.')


    def afficherPerdu(self):
        self.perdu = QGraphicsPixmapItem(self.jeu.theme.perdu)
        perduX = int((self.largeur - self.perdu.boundingRect().width())/2)
        perduY = int((self.hauteur - self.perdu.boundingRect().height())/2)
        self.perdu.setPos(perduX, perduY)
        self.perdu.setZValue(9999)
        self.scene.addItem(self.perdu)


    def afficherPause(self):
        self.pause = QGraphicsPixmapItem(self.jeu.theme.pause)
        pauseX = int((self.largeur - self.pause.boundingRect().width())/2)
        pauseY = int((self.hauteur - self.pause.boundingRect().height())/2)
        self.pause.setPos(pauseX, pauseY)
        self.pause.setZValue(9999)
        self.scene.addItem(self.pause)


    def masquerPause(self):
        self.scene.removeItem(self.pause)


    def supprimerLignesPleines(self) -> int:
        y = self.lignes
        deleted = 0
        while y >= 0:
            pleine = True
            for x in range(1, self.colonnes+1):
                if self.grille[y][x] == None:
                    pleine = False
                    break

            if pleine:
                deleted += 1
                for x in range(1, self.colonnes+1):
                    self.viderCase(x, y)
                    for y2 in range( y-1, -1, -1 ):
                        if self.grille[y2][x] != None:
                            self.grille[y2+1][x] = self.grille[y2][x]
                            self.grille[y2][x].placer(self.grille[y2][x].x, self.grille[y2][x].y + 1)
                            self.grille[y2][x] = None

            else:
                y -= 1

        return deleted