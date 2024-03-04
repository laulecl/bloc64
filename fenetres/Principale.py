from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from .Preferences import Preferences

class Principale(QtWidgets.QMainWindow):
    def __init__(self, jeu):
        super().__init__()
        self.setFocusPolicy(Qt.StrongFocus)

        self.jeu = jeu
        self.preferences = Preferences(self.jeu)

        uic.loadUi(self.jeu.path / 'ui' / 'Principale.ui', self)

        self.actionNouvelle.triggered.connect(self.nouvellePartie)
        self.actionPreferences.triggered.connect(self.afficherPreferences)


    def show(self):
        self.redimentionner()

        super().show()

    def redimentionner(self):
        margin = 10

        plateauWidth = self.jeu.plateau.largeur + 2
        plateauHeight = self.jeu.plateau.hauteur + 2

        suivantWidth = self.jeu.suivant.largeur + 2
        suivantHeight = self.jeu.suivant.hauteur + 2

        self.plateau.setGeometry(margin, margin, plateauWidth, plateauHeight)
        self.suivant.setGeometry(margin + plateauWidth + margin, margin, suivantWidth, suivantHeight)

        windowWidth = margin + plateauWidth + margin + suivantWidth + margin
        windowHeight = margin + plateauHeight + margin + 23

        self.setFixedSize(windowWidth, windowHeight)


    def nouvellePartie(self):
        self.jeu.demarrer()


    def afficherPreferences(self):
        if not self.jeu.pause:
            self.jeu.togglePause()

        self.preferences.exec_()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F2:
            self.jeu.demarrer()
            super().keyPressEvent(event)
            return

        if event.key() == Qt.Key_P:
            self.jeu.togglePause()
            super().keyPressEvent(event)
            return

        if self.jeu.pause:
            return
        else:
            if event.key() == Qt.Key_Up:
                self.jeu.piece.tourner()

            elif event.key() == Qt.Key_Down:
                self.jeu.piece.precipiter()

            elif event.key() == Qt.Key_Space:
                self.jeu.piece.precipiter()

            elif event.key() == Qt.Key_Left:
                self.jeu.piece.gauche()

            elif event.key() == Qt.Key_Right:
                self.jeu.piece.droite()

            elif event.key() == Qt.Key_5:
                self.jeu.piece.tourner()

            elif event.key() == Qt.Key_4:
                for i in range(1,4):
                    self.jeu.piece.gauche()

            elif event.key() == Qt.Key_6:
                for i in range(1,4):
                    self.jeu.piece.droite()

            super().keyPressEvent(event)