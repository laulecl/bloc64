

class Config():

    def __init__(self, jeu):
        self.jeu = jeu

        self.jeuMode = self.jeu.MODE_HEXA
        self.jeuLevel = 11


        self.themeName = 'default'
        self.themeTaille = 20


    def charger(self):
        # Application des paramètres de ocnfiguration
        self.jeu.mode = self.jeuMode
        self.jeu.level = self.jeuLevel
        self.jeu.theme.name = self.themeName
        self.jeu.theme.taille = self.themeTaille

        # Chargement des différents éléments
        self.jeu.theme.charger()
        self.jeu.plateau.preparer()
        self.jeu.suivant.preparer()