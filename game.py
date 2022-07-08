import numpy as np


def test1(d, i, j): #détecte 4 pions alignés en diagonale croissante
    x = 1
    y = 2
    if ((d[i][j] == x) and (d[i - 1][j + 1] == x) and (d[i - 2][j + 2] == x) and (d[i - 3][j + 3] == x)):
        return 1
    elif ((d[i][j] == y) and (d[i - 1][j + 1] == y) and (d[i - 2][j + 2] == y) and (d[i - 3][j + 3] == y)):
        return 2
    else:
        return 0


def test2(d, i, j): #détecte 4 pions alignés en diagonale décroissante
    x = 1
    y = 2
    if ((d[i][j] == x) and (d[i + 1][j + 1] == x) and (d[i + 2][j + 2] == x) and (d[i + 3][j + 3] == x)):
        return 1
    elif ((d[i][j] == y) and (d[i + 1][j + 1] == y) and (d[i + 2][j + 2] == y) and (d[i + 3][j + 3] == y)):
        return 2
    else:
        return 0


def test4(d, i, j): #détecte 4 pions alignés verticalement
    x = 1
    y = 2
    if ((d[i][j] == x) and (d[i + 1][j] == x) and (d[i + 2][j] == x) and (d[i + 3][j] == x)):
        return 1
    elif ((d[i][j] == y) and (d[i + 1][j] == y) and (d[i + 2][j] == y) and (d[i + 3][j] == y)):
        return 2
    else:
        return 0


def test3(d, i, j): #détecte 4 pions  alignés horizontalement
    x = 1
    y = 2
    if ((d[i][j] == x) and (d[i][j + 1] == x) and (d[i][j + 2] == x) and (d[i][j + 3] == x)):
        return 1
    elif ((d[i][j] == y) and (d[i][j + 1] == y) and (d[i][j + 2] == y) and (d[i][j + 3] == y)):
        return 2
    else:
        return 0


def available(d, x): # d:matrice , x:col 0->6
    if (x == 10):
        return -2 #reset
    if (x == 11):
        return -3 #quit
    else:

        i = 5
        while (i >= 0):
            if (d[i][x] == 0.0): #  according to the col x that u clicked on ,he will go through every line to check if its full or nah
                return i
            else:
                i = i - 1
        return -1


def position(a): #pos (x, y)
    x = a[0]
    y = a[1]

    if (x in range(287, 354)) and (y in range(120, 595)):
        return 0
    if (x in range(366, 431)) and (y in range(120, 595)):
        return 1
    if (x in range(442, 505)) and (y in range(120, 595)):
        return 2
    if (x in range(519, 580)) and (y in range(120, 595)):
        return 3
    if (x in range(596, 658)) and (y in range(120, 595)):
        return 4
    if (x in range(671, 732)) and (y in range(120, 595)):
        return 5
    if (x in range(749, 809)) and (y in range(120, 595)):
        return 6

    if (x in range(871, 971)) and (y in range(36, 136)): #reset button
        return 10 #reset
    if (x in range(980, 1082)) and (y in range(36, 136)): #quit button
        return 11 #quit


def change(p):
    if (p == 1):
        return 2
    if (p == 2):
        return 1


class the_game:
    d = np.zeros((6, 7))
    game_end = 0

    def __init__(self):
        print("COMMENCER")
        self.reset()

    def reset(self):
        for i in range(6):
            for j in range(7):
                self.d[i][j] = 0

    def check_win(self):
        for i in range(3, 6):
            for j in range(0, 4):
                w = test1(self.d, i, j)
                if (w != 0):
                    return w
        for i in range(0, 3):
            for j in range(0, 4):
                w = test2(self.d, i, j)
                if (w != 0):
                    return w
        for i in range(0, 6):
            for j in range(0, 4):
                w = test3(self.d, i, j)
                if (w != 0):
                    return w

        for i in range(0, 3):
            for j in range(0, 7):
                w = test4(self.d, i, j)
                if (w != 0):
                    return w

        return 0

    def play(self, player, col):
        t = available(self.d, col)

        if (col in range(7)):

            if (player == 1):
                self.d[t][col] = 1
            if (player == 2):
                self.d[t][col] = 2

            return t
        if (col == 10):
            self.reset()
        return t

    def get_d(self):
        return self.d

    def get_game_end(self):
        return self.game_end





