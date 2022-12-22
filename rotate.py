import numpy as np
from input import read_integer_input

def replace_cases(piece):
    size = len(piece)
    lowest_x = size
    highest_y = 0

    for y in range(size):
        for x in range(size):
            if piece[y][x] == 1:
                if x < lowest_x :
                    lowest_x = x
                if y > highest_y :
                    highest_y = y

    for y in range(size - 1, -1, -1):
        for x in range(size):
            if piece[y][x] == 1:
                piece[y][x] = 0;
                piece[y + (size - 1 - highest_y)][x - lowest_x] = 1;

    return piece


def rotate_bloc(piece, direction, nb_rotations=1):
    if direction == True:
        piece = np.rot90(piece, nb_rotations, axes=(1, 0))
    else:
        piece = np.rot90(piece, nb_rotations)
    
    return piece.tolist()


def get_rotation(piece):

    choice = read_integer_input('Souhaitez vous faire pivoter la piece ?\n0) Quitter\n1) Non\n2) Gauche\n3) Droite:', 0, 3)

    if choice > 1:
        nb_rotations = read_integer_input('Combien de fois voulez vous pivoter la piece ?', 0, 3)

    if choice == 0:
        exit(0)
    elif choice == 1:
        return piece
    elif choice == 2:
        piece = rotate_bloc(piece, False, nb_rotations)
    elif choice == 3:
        piece = rotate_bloc(piece, True, nb_rotations)
    
    return replace_cases(piece)
