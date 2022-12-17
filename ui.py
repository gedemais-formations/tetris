from math import ceil
import string
from blocs import *
from random import randint
from validate import validate_and_place, delete_completes
from input import read_integer_input, read_alphachar_input


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
        print('| ' + uppercase_letters[i])

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
                        print('  ', end='')
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


def get_user_input(pieces_list, shape, gamemode, width, height, random_list):
    maxi = len(pieces_list) if gamemode == 1 else 3
    piece_index = read_integer_input('Choisissez la piece que vous voulez placer (ou 0 pour quitter) :', 0, maxi)

    if piece_index == 0:
        print("Goodbye !")
        exit(0)

    if gamemode == 1:
        piece = pieces_list[piece_index - 1]
    else:
        piece = random_list[piece_index - 1]

    column = read_alphachar_input('Choisissez la colonne ou placer votre piece :', string.ascii_lowercase[width])
    row = read_alphachar_input('Choisissez la ligne ou placer votre piece :', string.ascii_lowercase[height])

    return  string.ascii_lowercase.index(column), string.ascii_lowercase.index(row), piece



def gamemode_random(pieces_list, shape):
    indices = [randint(1, len(pieces_list)) - 1 for i in range(3)]

    new_list = [pieces_list[x] for x in indices]

    index = 0
    index = draw_pieces([new_list[0]], len(new_list[0][0]), 1, index)
    index = draw_pieces([new_list[1]], len(new_list[1][0]), 1, index)
    index = draw_pieces([new_list[2]], len(new_list[2][0]), 1, index)
    return new_list


def pieces_menu(board, pieces_list, shape, gamemode, width, height):
    random_list = None

    valid = False
    fails = 0
    while not valid:
        index = 0
        draw_board(board, width, height, shape)

        if gamemode == 1:
            index = draw_pieces(pieces_list, 4, 20, index)
            draw_pieces(pieces_list[20:], matrix_sizes[shape - 1], len(pieces_list[20:]), index)

        if gamemode == 2:
            random_list = gamemode_random(pieces_list, shape)

        column, row, piece = get_user_input(pieces_list, shape, gamemode, width, height, random_list)
        valid, fails = validate_and_place(board, column, row, piece, fails)
        delete_completes(board, width, height)

    draw_board(board, width, height, shape)

    return True
