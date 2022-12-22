from blocs import *
from random import randint
import validate
from validate import validate_and_place, delete_completes
from input import read_integer_input, read_alphachar_input
import string
from math import ceil
import os
import numpy as np
import json
import datetime

score_y = 3

def print_score(index):
    strings = [
            '  ' + '-' * 20,
            '    Score : {}'.format(validate.score),
            '  ' + '-' * 20
            ]
    print(strings[index])


def print_equal_bar(width):
    print('   ', end='')
    for i in range(width):
        print('= ', end='')

    print('')


def print_lowercase_letter(width):
    lowercase_letters = string.ascii_lowercase[0:width]
    print('   ', end='')
    for letter in lowercase_letters:
        print(letter + ' ', end='')

    print('')


def draw_board(board, width, height, shape):
    print_lowercase_letter(width)
    print_equal_bar(width)

    uppercase_letters = string.ascii_uppercase[0:height]

    for i, line in enumerate(board):
        x = 0
        print('{} |'.format(uppercase_letters[i]), end='')
        for cell in line:
            x += 1
            if cell == 1:
                print('. ', end='')
            elif cell == 2:
                print(u'\u2588' + ' ', end='')
            else:
                print('  ', end='')

        print('  ' * (width - x), end='')
        print('| ' + uppercase_letters[i], end='')

        if i in range(score_y, score_y + 3):
            print_score(i - score_y)
        else:
            print('')

    print_equal_bar(width)
    print_lowercase_letter(width)


def draw_pieces(pieces_list, matrix_dim, n, index):
    col = 10
    for y in range(ceil(n / col)):
        start = y * col
        end = start + col
        for sub_y in range(matrix_dim):
            for piece in pieces_list[start:end]:
                for elem in piece[sub_y]:
                    if elem == 0:
                        print('. ', end='')
                    else:
                        print(u'\u2588' + ' ', end='')

                print(' ', end='')
            print('')

        for i, piece in enumerate(pieces_list[start:end]):
            print(index + 1, ' ' * (matrix_dim * 2 - len(str(index + 1))), end='')
            index += 1

        print('\n')

    return index


matrix_sizes = [
    5,
    3,
    5
]


def replace_cases(piece):
    size = len(piece)
    lowest_x = size
    highest_y = 0

    for line in piece:
        print(line)

    for y in range(size):
        for x in range(size):
            if piece[y][x] == 1:
                if x < lowest_x :
                    lowest_x = x
                if y > highest_y :
                    highest_y = y

    print(lowest_x, highest_y, size)
    print('-----------------------------')
    for y in range(size - 1, -1, -1):
        for x in range(size):
            print(x, y)
            if piece[y][x] == 1:
                piece[y][x] = 0;
                print('----')
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
    
    print('---------------')

    if choice == 0:
        exit(0)
    elif choice == 1:
        return piece
    elif choice == 2:
        piece = rotate_bloc(piece, False, nb_rotations)
    elif choice == 3:
        piece = rotate_bloc(piece, True, nb_rotations)

    
    return replace_cases(piece)


def save_game(board, width, height, shape, gamemode, score):
    data = {
            'board': board,
            'width': width,
            'height': height,
            'shape': shape,
            'gamemode': gamemode,
            'score': score
    }

    filename = str(datetime.datetime.now())
    filename = filename[:-7].replace(' ', '-')
    path = 'saves/' + filename + '.json'

    with open(path, 'w+') as file:
        json.dump(data, file)


def load_save():
    choice_index = 0
    saves_path = 'saves/'
    input_phrase = 'Choisissez un fichier de sauvegarde :\n0) Quitter\n'
    entries = os.listdir(saves_path)

    for filename in entries:
        choice_index += 1
        input_phrase += '{0}) {1}\n'.format(choice_index, filename)

    choice = read_integer_input(input_phrase, 0, choice_index)

    save_path = saves_path + entries[choice_index - 1]

    with open(save_path, 'r') as file:
        data = json.load(file)

    print(data)
    return data.values()



def get_user_input(board, pieces_list, shape, gamemode, width, height, random_list):
    # Defines the maximum index to be chosen by the player depending on gamemode
    maxi = len(pieces_list) if gamemode == 1 else 3

    # Reads the index selected by user
    piece_index = read_integer_input('Choisissez la piece que vous voulez placer (ou 0 pour quitter, -1 pour sauvegarder et quitter) :', -1, maxi)

    # 0 choice means exit the game
    if piece_index < 1:
        # -1 choice means save the board state
        if piece_index == -1:
            save_game(board, width, height, shape, gamemode, validate.score)

        print("Goodbye !")
        exit(0)

    # Get the selected piece
    if gamemode == 1:
        piece = pieces_list[piece_index - 1]
    else:
        piece = random_list[piece_index - 1]

    piece = get_rotation(piece)
    # Read user input for coordinates
    column = read_alphachar_input('Choisissez la colonne ou placer votre piece :', string.ascii_lowercase[width])
    row = read_alphachar_input('Choisissez la ligne ou placer votre piece :', string.ascii_lowercase[height])

    # Return the indices of letters describing coordinates, and the piece to place
    return  string.ascii_lowercase.index(column), string.ascii_lowercase.index(row), piece



def gamemode_random(pieces_list, shape):
    # Random selection of three pieces in the list of available pieces
    random_list = [pieces_list[randint(1, len(pieces_list)) - 1] for x in range(3)]

    index = 0
    index = draw_pieces([random_list[0]], len(random_list[0][0]), 1, index)
    index = draw_pieces([random_list[1]], len(random_list[1][0]), 1, index)
    index = draw_pieces([random_list[2]], len(random_list[2][0]), 1, index)
    return random_list


def loop(board, pieces_list, shape, gamemode, width, height):
    """

    """
    # In case this list does not exist when calling get_user_input, we declare it here.
    random_list = None
    # Condition of infinite loop forcing user to input valid data
    valid = False
    # Number of fails, reset at each round. If the user fails to input valid data 3 times, the program exits.
    fails = 0

    # Validation loop
    while not valid:

        # Piece index for menu choice display.
        index = 0

        # First gamemode : All pieces are available at every round.
        if gamemode == 1:
            index = draw_pieces(pieces_list, 4, 20, index)
            draw_pieces(pieces_list[20:], matrix_sizes[shape - 1], len(pieces_list[20:]), index)

        # Second : Only three randomly selected pieces are available for each round.
        if gamemode == 2:
            random_list = gamemode_random(pieces_list, shape)

        # The user tries to place a piece
        column, row, piece = get_user_input(board, pieces_list, shape, gamemode, width, height, random_list)

        # We check if the piece and its coordinates are ok with the board, and if it is then we place it.
        valid, fails = validate_and_place(board, width, height, shape, column, row, piece, fails)
        if not valid:
            os.system('clear')
            print("Can not place piece. {} try left !".format(3 - fails))
            draw_board(board, width, height, shape)

    # We check for complete row or column and delete them, incrementing the score for each cell deleted.
    board = delete_completes(board, width, height)
    # Screen clear and board display for next round
    os.system('clear')
    draw_board(board, width, height, shape)

    return True
