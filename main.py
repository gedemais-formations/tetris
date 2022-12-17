from blocs import *
from plateaux import *
from ui import *

width = 0
height = 0
shape = 0
gamemode = 0

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
    global gamemode

    # Read user input for board parameters
    width = read_integer_input("Largeur du plateau :", 21, 26)
    height = read_integer_input("Hauteur du plateau :", 21, 26)
    shape = read_integer_input("Forme du plateau :\n1) Cercle\n2) Triangle\n3) Losange", 1, 3)
    gamemode = read_integer_input("Mode de jeu :\n1) Afficher à chaque tour de jeu l’ensemble des blocs disponibles et l’utilisateur en sélectionne un.\n2) Afficher uniquement 3 blocs sélectionnés aléatoirement.\n", 1, 2)


def setup():
    parse_user_arguments()

    # Generation of 2D matrix that will represent the board
    board = [[0 for x in range(width)] for x in range(height)]

    print(width, height, shape)
    print('-' * 80)
    board_functions[shape - 1](board, width, height)

    for x in range(width):
        board[12][x] = 2

    keep = True
    while keep:
        keep = pieces_menu(board, pieces_lists[shape - 1], shape, gamemode, width, height)


def rules():
    regles = '\nRegles :\n'
    regles += '---------------------------------------------------\n'
    regles += 'Deux modes de jeu sont possibles :\n'
    regles += '- Afficher à chaque tour de jeu l’ensemble des blocs disponibles et l’utilisateur en sélectionne un.\n'
    regles += '- Afficher uniquement 3 blocs sélectionnés aléatoirement.\n'
    regles += '---------------------------------------------------\n'
    print(regles)


def quit_program():
    exit(0)


menu_links = [
    setup,
    rules,
    quit_program
]

def menu():
    print("Welcome to tetris by Enzo & Karim !")
    choice = read_integer_input("1) Jouer\n2) Regles\n3) Quitter", 1, 3)
    menu_links[choice - 1]()


def main():
    while True:
        menu()



if __name__ == "__main__":
    main()
