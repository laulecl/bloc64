import sys
import random
from pathlib import Path
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from fenetres.Principale import Principale
from .Plateau import Plateau
from .Theme import Theme
from .Piece import Piece
from .Suivant import Suivant
from .Config import Config

class Jeu:
    def __init__(self):
        self.MODE_HEXA = 'hexa'
        self.MODE_QUAD = 'quad'

        self.path = Path(__file__).parent.parent
        self.application = QtWidgets.QApplication(sys.argv)

        self.config = Config(self)

        self.fenetrePrincipale = Principale(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.chutePiece)
        self.pause = False
        self.level = 1
        self.mode = self.MODE_HEXA
        self.score = 0
        self.lignes = 0
        self.pieces = 0

        self.theme = Theme(self)
        self.plateau = Plateau(self, self.fenetrePrincipale.plateau)
        self.suivant = Suivant(self, self.fenetrePrincipale.suivant)



    def charger(self):
        self.theme.charger()
        self.plateau.preparer()
        self.suivant.preparer()
        self.config.charger()
        self.fenetrePrincipale.show()
        sys.exit(self.application.exec_())


    def chutePiece(self):
        if not self.piece.canBougerPiece(0,1,0):
            if (self.piece.y < 0):
                self.perdu()
            else:
                self.nouvellePiece()
        else:
            self.piece.bouger(0,1,0)


    def demarrer(self):
        self.plateau.vider()
        self.piece = Piece(self.plateau)
        self.choisirProchainePiece()
        self.nouvellePiece()
        self.timer.start(self._speed())


    def nouvellePiece(self):
        self.pieces += 1
        self.lignes += self.plateau.supprimerLignesPleines()
        self.pieceIndex = self.nextPieceIndex
        self.choisirProchainePiece()
        self.piece.nouvelle(self.pieceIndex)
        self.suivant.nouvellePiece(self.nextPieceIndex)


    def choisirProchainePiece(self):
        if self.mode == self.MODE_HEXA:
            self.nextPieceIndex = random.randint(1, 10)

        elif self.mode == self.MODE_QUAD:
            self.nextPieceIndex = random.randint(11, 17)


    def perdu(self):
        self.timer.stop()
        self.plateau.afficherPerdu()


    def togglePause(self):
        if self.pause:
            self.plateau.masquerPause()
            self.timer.start(self._speed())
        else:
            self.plateau.afficherPause()
            self.timer.stop()

        self.pause = not self.pause


    def _speed(self) -> int:
        speed = -38 * (self.level-1) + 600

        return speed