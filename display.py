import string
import validate
from math import ceil

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
                print('  ', end='')
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
