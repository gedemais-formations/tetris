import json
import datetime
import os
from input import read_integer_input

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

    return data.values()


