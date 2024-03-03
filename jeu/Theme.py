import math
from PyQt5.QtSvg import QGraphicsSvgItem, QSvgRenderer
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QSize

class Theme:

    def __init__(self, jeu):
        self.jeu = jeu
        self.name = 'default'
        self.taille = 20


    def charger(self):
        if self.jeu.mode == self.jeu.MODE_HEXA:
            self.blocWidth = self.taille * 2
            self.blocHeight = round(self.taille * math.sqrt(3))

            self.stepWidth = self.blocWidth - round(self.taille / 2)
            self.stepHeight = self.blocHeight

            self.decalageX = 0
            self.decalageY = round(self.stepHeight / 2) - self.stepHeight
            self.decalageWidth = round(self.taille / 2)
            self.decalageHeight = round(self.stepHeight / 2)

        elif self.jeu.mode == self.jeu.MODE_QUAD:
            self.blocWidth = self.taille * 2
            self.blocHeight = self.taille * 2

            self.stepWidth = round(self.taille * 1.57)
            self.stepHeight = round(self.taille * 1.57)

            self.decalageX = round(self.taille * 0.2)
            self.decalageY = round(self.taille * 0.2)
            self.decalageWidth = 0
            self.decalageHeight = 0

        self.fond = QPixmap(str(self.jeu.path / 'theme' / self.name / 'background.png'))
        self.perdu = self._creerPerdu()
        self.pause = self._creerPause()

        self.blocs = {}
        for i in range(0,18):
            self._creerBloc(i)


    def _creerBloc(self, index):
        svgFileName = str(self.jeu.path / 'theme' / self.name / f"{index}.svg")

        pixmap = QPixmap(QSize(self.blocWidth, self.blocHeight))
        pixmap.fill(Qt.transparent)
        peintre = QPainter(pixmap)
        renderer = QSvgRenderer(svgFileName)
        renderer.render(peintre)  # Rendre le SVG sur le QPixmap
        peintre.end()

        self.blocs[index] = pixmap


    def _creerPerdu(self) -> QPixmap:
        svgFileName = str(self.jeu.path / 'theme' / self.name / "perdu.svg")

        renderer = QSvgRenderer(svgFileName)

        x = int((self.jeu.plateau.colonnes * self.stepWidth + self.decalageWidth) * 80 / 100)
        y = int(x * renderer.defaultSize().height() / renderer.defaultSize().width())

        pixmap = QPixmap(QSize(x, y))
        pixmap.fill(Qt.transparent)
        peintre = QPainter(pixmap)
        renderer.render(peintre)  # Rendre le SVG sur le QPixmap
        peintre.end()

        return pixmap


    def _creerPause(self) -> QPixmap:
        svgFileName = str(self.jeu.path / 'theme' / self.name / "pause.svg")

        renderer = QSvgRenderer(svgFileName)

        x = int((self.jeu.plateau.colonnes * self.stepWidth + self.decalageWidth) * 70 / 100)
        y = int(x * renderer.defaultSize().height() / renderer.defaultSize().width())

        pixmap = QPixmap(QSize(x, y))
        pixmap.fill(Qt.transparent)
        peintre = QPainter(pixmap)
        renderer.render(peintre)  # Rendre le SVG sur le QPixmap
        peintre.end()

        return pixmap