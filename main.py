from blocs import *
from plateaux import *
from ui import *
import validate

# General global variables
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

    # Read user input for board and game parameters
    width = read_integer_input("Largeur du plateau :", 21, 26)
    height = read_integer_input("Hauteur du plateau :", 21, 26)
    shape = read_integer_input("Forme du plateau :\n1) Cercle\n2) Triangle\n3) Losange", 1, 3)
    gamemode = read_integer_input("Mode de jeu :\n1) Afficher à chaque tour de jeu l’ensemble des blocs disponibles et l’utilisateur en sélectionne un.\n2) Afficher uniquement 3 blocs sélectionnés aléatoirement.\n", 1, 2)


def rules():
    """
        Displays game's rules.
    """
    regles = '\nRegles :\n'
    regles += '---------------------------------------------------\n'
    regles += 'Deux modes de jeu sont possibles :\n'
    regles += '- Afficher à chaque tour de jeu l’ensemble des blocs disponibles et l’utilisateur en sélectionne un.\n'
    regles += '- Afficher uniquement 3 blocs sélectionnés aléatoirement.\n'
    regles += '---------------------------------------------------\n'
    print(regles)


def quit_program():
    """
        Quits game.
    """
    exit(0)


def setup():
    """
        Greets the user, and ask him informations to build the game for him.
    """
    global width
    global height
    global shape
    global gamemode

    start_choice = read_integer_input('1) Creer une partie\n2) Charger une sauvegarde', 1, 2)
    if start_choice == 1:
        # Ask informations about map and gamemode
        parse_user_arguments()

        # Generation of 2D matrix that will represent the board
        board = [[0 for x in range(width)] for x in range(height)]

        # Build a board of desired shape
        height, board = board_functions[shape - 1](board, width, height)
    else:
        board, width, height, shape, gamemode, validate.score = load_save()

    # Clear screen and draw the empty shaped board
    os.system('clear')
    print(len(board))
    draw_board(board, width, height, shape)

    # Game infinite loop condition
    keep = True
    while keep:
        # Main loop fonction running the game
        keep = loop(board, pieces_lists[shape - 1], shape, gamemode, width, height)


# Array of functions allawing us to call any of them with an index chosen by the user.
menu_links = [
    setup,
    rules,
    quit_program
]

def menu():
    # Main menu
    choice = read_integer_input("Welcome to tetris by Enzo & Karim !\n1) Jouer\n2) Regles\n3) Quitter", 1, 3)
    menu_links[choice - 1]()


def main():
    # Main loop
    while True:
        menu()


if __name__ == "__main__":
    main()
