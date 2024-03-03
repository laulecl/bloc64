from typing import Dict
from .Bloc import Bloc


class Piece:

    def __init__(self, plateau):
        self.plateau = plateau
        self.blocs = {}
        self.precipite = False

        self.__modeles = {
            # hexa
            1: {
                1: { 'r': 1, 'a': 0 },
                2: { 'r': 0, 'a': 0 },
                3: { 'r': 1, 'a': 3 },
                4: { 'r': 2, 'a': 6 },
                'rotations': 6
            },
            2: {
                1: {'r': 1, 'a': 0},
                2: {'r': 0, 'a': 0},
                3: {'r': 1, 'a': 3},
                4: {'r': 2, 'a': 7},
                'rotations': 6
            },
            3: {
                1: {'r': 1, 'a': 0},
                2: {'r': 0, 'a': 0},
                3: {'r': 1, 'a': 3},
                4: {'r': 2, 'a': 5},
                'rotations': 6
            },
            4: {
                1: {'r': 1, 'a': 0},
                2: {'r': 0, 'a': 0},
                3: {'r': 1, 'a': 4},
                4: {'r': 2, 'a': 7},
                'rotations': 6
            },
            5: {
                1: {'r': 1, 'a': 0},
                2: {'r': 0, 'a': 0},
                3: {'r': 1, 'a': 2},
                4: {'r': 2, 'a': 5},
                'rotations': 6
            },
            6: {
                1: {'r': 1, 'a': 0},
                2: {'r': 0, 'a': 0},
                3: {'r': 1, 'a': 2},
                4: {'r': 1, 'a': 3},
                'rotations': 6
            },
            7: {
                1: {'r': 1, 'a': 0},
                2: {'r': 0, 'a': 0},
                3: {'r': 1, 'a': 2},
                4: {'r': 1, 'a': 3},
                'rotations': 6
            },
            8: {
                1: {'r': 1, 'a': 0},
                2: {'r': 0, 'a': 0},
                3: {'r': 1, 'a': 2},
                4: {'r': 1, 'a': 4},
                'rotations': 6
            },
            9: {
                1: {'r': 0, 'a': 0},
                2: {'r': 1, 'a': 2},
                3: {'r': 1, 'a': 3},
                4: {'r': 1, 'a': 4},
                'rotations': 6
            },
            10: {
                1: {'r': 1, 'a': 3},
                2: {'r': 1, 'a': 4},
                3: {'r': 1, 'a': 5},
                4: {'r': 1, 'a': 0},
                'rotations': 6
            },

            # quad
            11: {
                1: {'r': 0, 'a': 0},
                2: {'r': 1, 'a': 0},
                3: {'r': 1, 'a': 4},
                4: {'r': 2, 'a': 8},
                'rotations': 4
            },
            12: {
                1: {'r': 0, 'a': 0},
                2: {'r': 1, 'a': 2},
                3: {'r': 1, 'a': 3},
                4: {'r': 1, 'a': 6},
                'rotations': 4
            },
            13: {
                1: {'r': 0, 'a': 0},
                2: {'r': 1, 'a': 2},
                3: {'r': 1, 'a': 5},
                4: {'r': 1, 'a': 6},
                'rotations': 4
            },
            14: {
                1: {'r': 0, 'a': 0},
                2: {'r': 1, 'a': 3},
                3: {'r': 1, 'a': 4},
                4: {'r': 1, 'a': 6},
                'rotations': 4
            },
            15: {
                1: {'r': 0, 'a': 0},
                2: {'r': 1, 'a': 2},
                3: {'r': 1, 'a': 3},
                4: {'r': 1, 'a': 4},
                'rotations': 1
            },
            16: {
                1: {'r': 0, 'a': 0},
                2: {'r': 1, 'a': 0},
                3: {'r': 1, 'a': 2},
                4: {'r': 1, 'a': 4},
                'rotations': 4
            },
            17: {
                1: {'r': 0, 'a': 0},
                2: {'r': 1, 'a': 2},
                3: {'r': 1, 'a': 4},
                4: {'r': 1, 'a': 5},
                'rotations': 4
            },
        }

        self.__raVersPos = {
            0: {
                0: {'x':  0, 'y':  0}
            },

            # 1 et 2 = rayons 1 et 2 en mode hexa
            1: {
                0: {'x':  0, 'y': -1},
                1: {'x':  1, 'y': -1},
                2: {'x':  1, 'y':  0},
                3: {'x':  0, 'y':  1},
                4: {'x': -1, 'y':  0},
                5: {'x': -1, 'y': -1},
            },
            2: {
                0: {'x':  0, 'y': -2},
                1: {'x':  1, 'y': -2},
                2: {'x':  2, 'y': -1},
                3: {'x':  2, 'y':  0},
                4: {'x':  2, 'y':  1},
                5: {'x':  1, 'y':  1},
                6: {'x':  0, 'y':  2},
                7: {'x': -1, 'y':  1},
                8: {'x': -2, 'y':  1},
                9: {'x': -2, 'y':  0},
               10: {'x': -2, 'y': -1},
               11: {'x': -1, 'y': -2},
            },

            # 11 = 1, 12 = 2 en mode quad
            11: {
                0: {'x':  0, 'y': -1},
                1: {'x':  1, 'y': -1},
                2: {'x':  1, 'y':  0},
                3: {'x':  1, 'y':  1},
                4: {'x':  0, 'y':  1},
                5: {'x': -1, 'y':  1},
                6: {'x': -1, 'y':  0},
                7: {'x': -1, 'y': -1},
            },
            12: {
                 0: {'x':  0, 'y': -2},
                 1: {'x':  1, 'y': -2},
                 2: {'x':  2, 'y': -2},
                 3: {'x':  2, 'y': -1},
                 4: {'x':  2, 'y':  0},
                 5: {'x':  2, 'y':  1},
                 6: {'x':  2, 'y':  2},
                 7: {'x':  1, 'y':  2},
                 8: {'x':  0, 'y':  2},
                 9: {'x': -1, 'y':  2},
                10: {'x': -2, 'y':  2},
                11: {'x': -2, 'y':  1},
                12: {'x': -2, 'y':  0},
                13: {'x': -2, 'y': -1},
                14: {'x': -2, 'y': -2},
                15: {'x': -1, 'y': -2},
            },
        }


    def nouvelle(self, index: int=1, x: int=0, y: int=-2, r: int=0):
        self.index = index
        self.x = x
        self.y = y
        self.r = r
        self.precipite = False

        if self.x == 0:
            self.x = round(self.plateau.colonnes / 2)

        if self.y == -2 and index > 5:
            self.y = -1

        for c in range(1, 5):
            self.blocs[c] = self.plateau.nouvelleCase(self.index, 1, -1)

        self.bouger(0,0,0)


    def __definirCasePos(self, bloc: int, xDiff: int, yDiff: int, rDiff: int) -> Dict[str, int]:
        ra = self.__modeles[self.index][bloc]

        rotationsPossibles = self.__modeles[self.index]['rotations']

        rotation = (self.r + rDiff) % rotationsPossibles

        a = ra['a']
        r = ra['r']

        if self.plateau.jeu.mode == self.plateau.jeu.MODE_HEXA:
            if r == 1 and rotation != 0:
                a = (a + rotation) % rotationsPossibles

            if r == 2 and rotation != 0:
                a = (a + rotation*2) % (6 * 2)

        elif self.plateau.jeu.mode == self.plateau.jeu.MODE_QUAD:
            rotation *= 2

            if r == 1 and rotation != 0:
                a = (a + rotation * 1) % (4 * 2)

            if r == 2 and rotation != 0:
                a = (a + rotation * 2) % (4 * 4)

            if r > 0:
                r += 10

        pos = self.__raVersPos[r][a]

        x = self.x + xDiff + pos['x']
        y = self.y + yDiff + pos['y']

        if self.plateau.jeu.mode == self.plateau.jeu.MODE_HEXA and (self.x + xDiff) % 2 == 0 and pos['x'] % 2 == 0:
            y -= 1

        return {'x': x, 'y': y}


    def __canBougerCase(self, bloc: int, xDiff: int, yDiff: int, rDiff: int) -> bool:
        pos = self.__definirCasePos(bloc, xDiff, yDiff, rDiff)

        for c in range(1, 5):
            if self.blocs[c].x == pos['x'] and self.blocs[c].y == pos['y']:
                # Si la nouvelle position correspond à une des cases de la pièce => c'est OK
                return True

        # Sinon, le plateau doit être libre à ce niveau
        return self.plateau.libre(pos['x'], pos['y'])


    def canBougerPiece(self, xDiff: int, yDiff: int, rDiff: int) -> bool:
        if self.precipite:
            return False

        for c in range(1, 5):
            if not self.__canBougerCase(c, xDiff, yDiff, rDiff):
                return False

        return True


    def bouger(self, xDiff: int, yDiff: int, rDiff: int) -> bool:
        if not self.canBougerPiece(xDiff, yDiff, rDiff):
            return False

        for c in range(1, 5):
            pos = self.__definirCasePos(c, xDiff, yDiff, rDiff)
            self.blocs[c].placer(pos['x'], pos['y'])

        self.r = (self.r + rDiff) % self.__modeles[self.index]['rotations']
        self.x += xDiff
        self.y += yDiff

        return True


    def placer(self):
        for c in range(1, 5):
            pos = self.__definirCasePos(c, 0, 0, 0)
            self.blocs[c].placer(pos['x'], pos['y'])


    def precipiter(self):
        while self.canBougerPiece(0,1,0):
            self.bouger(0,1,0)

        self.precipite = True

    def droite(self):
        self.bouger(1, 0, 0)


    def gauche(self):
        self.bouger(-1, 0, 0)


    def bas(self):
        self.bouger(0, 1, 0)


    def haut(self):
        self.bouger(0, -1, 0)


    def tourner(self):
        self.bouger(0, 0, -1)