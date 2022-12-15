from blocs import *
from plateaux import *
from ui import *

width = 0
height = 0
shape = 0

def read_integer_input(input_phrase, mini, maxi):
    """
        This function will force the user to input a valid integer
        in the console, in order to get informations from him.

        @parameters :
        - input_phrase (string) : Sentence displayed in console to ask data from user.
        - mini (integer) : The minimum valid value to input
        - maxi (integer) : The maximum valid value to input
    """

    # Infinite loop forcing user to input a correct value
    while True:
        # Input phrase that hints user for the data to input
        print('\n' + input_phrase)
        try:
            tmp = int(input('-> '))
        except:
            print("\nFormat invalide. Essayez encore :")
            continue # Back to start

        if tmp >= mini and tmp <= maxi:
            break # tmp value is ok, we can return it

        # If it is a range problem, we display the adapted error message :
        print("\nMerci d'entrer un nombre entre {0} et {1} :".format(mini, maxi))

    return tmp


def parse_user_arguments():
    """
        Parses user arguments :
        - board width
        - board height
        - board shape
    """
    # Allow write access to global variables
    global width
    global height
    global shape

    # Read user input for board parameters
    width = read_integer_input("Largeur du plateau :", 21, 26)
    height = read_integer_input("Hauteur du plateau :", 21, 26)
    shape = read_integer_input("Forme du plateau :\n1) Cercle\n2) Triangle\n3) Losange", 1, 3)


def main():
    print("Welcome to tetris by Enzo & Karim !")
    parse_user_arguments()

    # Generation of 2D matrix that will represent the board
    board = [[0 for x in range(width)] for x in range(height)]

    print(width, height, shape)
    print('-' * 80)
    board_functions[shape - 1](board, width, height)
    draw_board(board, width, height, shape)


if __name__ == "__main__":
    main()
