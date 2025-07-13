from PyQt6.QtCore import QSettings


class Config():

    def __init__(self, jeu):
        self.jeu = jeu

        self.settings = QSettings("LorenzoDPM", "Bloc64")

        self.jeuMode = self.jeu.MODE_HEXA
        self.jeuLevel = 1

        self.plateauLignes = 23
        self.plateauColonnes = 13

        self.themeName = 'default'
        self.themeTaille = 20
        self.themeFond = 'background.png'


    def appliquer(self):
        # Application des paramètres de configuration
        self.jeu.mode = self.jeuMode
        self.jeu.level = self.jeuLevel

        self.jeu.plateau.lignes = self.plateauLignes
        self.jeu.plateau.colonnes = self.plateauColonnes

        self.jeu.theme.name = self.themeName
        self.jeu.theme.taille = self.themeTaille
        self.jeu.theme.fond = self.themeFond

        # Chargement des différents éléments
        self.jeu.theme.charger()
        self.jeu.plateau.preparer()
        self.jeu.suivant.preparer()
        self.jeu.fenetrePrincipale.redimentionner()


    def charger(self):
        self.jeuMode = self.settings.value("jeu/mode", defaultValue=self.jeu.MODE_HEXA)
        self.jeuLevel = int(self.settings.value("jeu/level", 1))

        self.plateauLignes = int(self.settings.value("plateau/lignes", 23))
        self.plateauColonnes = int(self.settings.value("plateau/colonnes", 13))

        self.themeName = self.settings.value("theme/name", 'default')
        self.themeTaille = int(self.settings.value("theme/taille", 20))
        self.themeFond = self.settings.value("theme/fond", 'background.png')

    def sauvegarder(self):
        self.settings.setValue("jeu/mode", self.jeuMode)
        self.settings.setValue("jeu/level", self.jeuLevel)

        self.settings.setValue("plateau/lignes", self.plateauLignes)
        self.settings.setValue("plateau/colonnes", self.plateauColonnes)

        self.settings.setValue("theme/name", self.themeName)
        self.settings.setValue("theme/taille", self.themeTaille)
        self.settings.setValue("theme/fond", self.themeFond)