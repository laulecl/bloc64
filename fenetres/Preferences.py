from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QShowEvent


class Preferences(QtWidgets.QDialog):
    def __init__(self, jeu):
        super().__init__()
        self.setFocusPolicy(Qt.StrongFocus)

        self.jeu = jeu

        uic.loadUi(self.jeu.path / 'ui' / 'Preferences.ui', self)

        self.jeuMode.addItem('Hexagonal', self.jeu.MODE_HEXA)
        self.jeuMode.addItem('Traditionnel', self.jeu.MODE_QUAD)

        self.buttonBox.accepted.connect(self.enregistrer)


    def showEvent(self, event: QShowEvent):
        jeuModeIndex = self.jeuMode.findData(self.jeu.config.jeuMode)
        self.jeuMode.setCurrentIndex(jeuModeIndex)
        self.jeuLevel.setValue(self.jeu.config.jeuLevel)

        self.plateauColonnes.setValue(self.jeu.config.plateauColonnes)
        self.plateauLignes.setValue(self.jeu.config.plateauLignes)

        self.themeTaille.setValue(self.jeu.config.themeTaille)


    def enregistrer(self):
        self.jeu.config.jeuMode = self.jeuMode.currentData()
        self.jeu.config.jeuLevel = self.jeuLevel.value()

        self.jeu.config.plateauColonnes = self.plateauColonnes.value()
        self.jeu.config.plateauLignes = self.plateauLignes.value()

        self.jeu.config.themeTaille = self.themeTaille.value()

        self.jeu.config.appliquer()
        self.jeu.config.sauvegarder()
        self.accept()