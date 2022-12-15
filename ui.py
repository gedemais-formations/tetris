from blocs import losange_list, circle_list, triangle_list
import string


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

