from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QGraphicsPixmapItem, QGraphicsView
from PyQt5.QtCore import QTimer
from .Piece import Piece
from .Bloc import Bloc


class Suivant:

    def __init__(self, jeu, widget: QGraphicsView):
        self.jeu = jeu
        self.widget = widget
        self.piece = Piece(self)

        self.lignes = 5
        self.colonnes = 5


    def preparer(self):
        self.largeur = self.colonnes * self.jeu.theme.stepWidth
        self.hauteur = self.largeur

        self.scene = QtWidgets.QGraphicsScene(self.widget)
        self.scene.setSceneRect(0, 0, self.largeur, self.hauteur)
        self.widget.setScene(self.scene)

        self.fond = QGraphicsPixmapItem(self.jeu.theme.fond)
        self.fond.setPos(0, 0)
        self.scene.addItem(self.fond)


    def nouvellePiece(self, pieceIndex):
        # on supprime les anciennes cases
        for item in self.scene.items():
            if item != self.fond:
                self.scene.removeItem(item)

        # on crée une nouvelle pièce
        self.piece.nouvelle(pieceIndex, 0, 0)

        # On cherche la bonne position pour la pièce
        minX = 9999999
        maxX = 0
        minY = 9999999
        maxY = 0

        for i, bloc in self.piece.blocs.items():
            pos = self.casePos(bloc)
            if pos['x'] < minX:
                minX = pos['x']

            if pos['x'] > maxX:
                maxX = pos['x']

            if pos['y'] < minY:
                minY = pos['y']

            if pos['y'] > maxY:
                maxY = pos['y']

        pieceWidth = maxX - minX + self.jeu.theme.stepWidth
        pieceHeight = maxY - minY + self.jeu.theme.stepHeight

        pieceX = int((self.largeur - pieceWidth) / 2)
        pieceY = int((self.hauteur - pieceHeight) / 2)

        # on affichage les cases
        for i, bloc in self.piece.blocs.items():
            pos = self.casePos(bloc)
            bloc.pixmap.setPos(pos['x'] + pieceX - minX - round(self.jeu.theme.decalageWidth / 2), pos['y'] + pieceY - minY)



    def nouvelleCase(self, index: int, x: int, y: int) -> Bloc:
        bloc = Bloc(self, index, x, y)
        self.scene.addItem(bloc.pixmap)

        return bloc


    def casePos(self, bloc: Bloc):
        posX = bloc.x * self.jeu.theme.stepWidth
        posY = bloc.y * self.jeu.theme.stepHeight - self.jeu.theme.decalageHeight

        if bloc.x % 2 == 0:
            posY += self.jeu.theme.decalageHeight

        return {'x': posX, 'y': posY}

    def placerCase(self, bloc: Bloc):
        pass

    def libre(self, x: int, y: int) -> bool:
        return True