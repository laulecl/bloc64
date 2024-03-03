from PyQt5.QtWidgets import QGraphicsPixmapItem


class Bloc :

    def __init__(self, plateau, index: int, x: int, y: int):
        self.plateau = plateau
        self.index = index
        self._x = x
        self._y = y
        self._lastX = x
        self._lastY = y

        self.pixmap = QGraphicsPixmapItem(self.plateau.jeu.theme.blocs[index])


    @property
    def x(self):
        return self._x


    @property
    def y(self):
        return self._y


    @property
    def lastX(self):
        return self._lastX


    @property
    def lastY(self):
        return self._lastY


    def placer(self, x: int, y: int):
        self._x = x
        self._y = y
        self.plateau.placerCase(self)
        self._lastX = self._x
        self._lastY = self._y