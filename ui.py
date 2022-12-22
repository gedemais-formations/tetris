from blocs import *
from display import *
from random import randint
from validate import validate_and_place, delete_completes
from input import read_integer_input, read_alphachar_input
from rotate import *
from save import *
import os

matrix_sizes = [
    5,
    3,
    5
]


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
    """
        This function will create the 3 random pieces list to be chosen by user in random gamemode.
        parameters:
        - pieces_list : Containes all available pieces for shape.
        - shape : Shape of the game board. Defines available pieces in a game.
    """
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
