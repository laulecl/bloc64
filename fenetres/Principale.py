from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from .Preferences import Preferences

class Principale(QtWidgets.QMainWindow):
    def __init__(self, jeu):
        super().__init__()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.jeu = jeu
        self.preferences = Preferences(self.jeu)

        uic.loadUi(self.jeu.path / 'ui' / 'Principale.ui', self)

        # Désactiver le focus sur les enfants
        self.plateau.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.suivant.setFocusPolicy(Qt.FocusPolicy.NoFocus)

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
        self.preferences.exec_()


    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key.Key_F2:
            self.jeu.demarrer()
            super().keyPressEvent(event)
            return

        if key == Qt.Key.Key_P:
            self.jeu.togglePause()
            super().keyPressEvent(event)
            return

        if self.jeu.pause:
            return
        else:
            if key == Qt.Key.Key_Up:
                self.jeu.piece.tourner()

            elif key == Qt.Key.Key_Down:
                self.jeu.piece.precipiter()

            elif key == Qt.Key.Key_Space:
                self.jeu.piece.precipiter()

            elif key == Qt.Key.Key_Left:
                self.jeu.piece.gauche()

            elif key == Qt.Key.Key_Right:
                self.jeu.piece.droite()

            elif key == Qt.Key.Key_2:
                self.jeu.piece.bas()

            elif key == Qt.Key.Key_5:
                self.jeu.piece.tourner()

            elif key == Qt.Key.Key_4:
                for i in range(1,4):
                    self.jeu.piece.gauche()

            elif key == Qt.Key.Key_6:
                for i in range(1,4):
                    self.jeu.piece.droite()
                
            super().keyPressEvent(event)