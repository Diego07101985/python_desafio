import math
import numpy as np


def somadiag(matriz_quadrada):
    diagonal1 = 0
    diagonal2 = 0
    for i in range(0, 3):
        diagonal1 = diagonal1 + matriz_quadrada[i][i]
        diagonal2 = diagonal2 + matriz_quadrada[len(matriz_quadrada)-i-1][i]
    return abs(diagonal1 - diagonal2)
                                        s


if __name__ == '__main__':
    matriz_quadrada = [[11, 2, 4],
                       [4, 5, 6],
                       [10, 8, -12]]

    print('Soma das diagonais: %s ', somadiag(matriz_quadrada))
