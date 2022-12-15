from math import dist, floor, ceil


def draw_circle(board, map_width, map_height):
    """
        Draws a circle shape with 1 values in the map.
        @parameters :
        - board : 2D matrix that represents the game board.
        - map_width : Game board width in cells.
        - map_height : Game board height in cells.
    """
    # Iterates over every cell of board
    for y in range(map_height):
        for x in range(map_width):
            # Measuring the distance from center to the currently iterated cell.
            n_x = float(x / map_width)
            n_y = float(y / map_height)
            if dist([n_x, n_y], [0.5, 0.5]) <= 0.5:
                board[y][x] = 1

    return board


def draw_triangle(board, map_width, map_height):
    """
        Draws a triangle shape with 1 values in the map.
        @parameters :
        - board : 2D matrix that represents the game board.
        - map_width : Game board width in cells.
        - map_height : Game board height in cells.
    """
    # Iterateur permettant de remplir le plateau de bas en haut
    y = map_height - 1
    half_width = floor(float(map_width) / 2.0)
    line_size = floor(map_width / 2)
    # Tant que le debut et la fin de la ligne ne sont pas egaux, le triangle est incomplet
    while (line_size >= 0):
        # On itere sur la ligne pour placer la valeur 1
        #print('\n-------------------', half_width - line_size, half_width + line_size, '\n-------------------')
        for x in range(half_width - round(line_size), half_width + round(line_size)):
            #   print(y, x)
            board[y][x] = 1

        line_size -= (map_width / map_height) / 2.0
        y -= 1

    return board


def draw_losange(board, map_width, map_height):
    # Iterateur permettant de remplir le plateau de bas en haut
    y_up = 0
    y_down = map_height - 1
    half_width = float(map_width) / 2.0
    line_size = 0
    max_line_size = floor(map_width / 2)
    # Tant que le debut et la fin de la ligne ne sont pas egaux, le triangle est incomplet
    while (line_size <= max_line_size):
        # On itere sur la ligne pour placer la valeur 1
        print(floor(half_width - line_size), ceil(half_width + line_size))
        for x in range(floor(half_width - line_size), ceil(half_width + line_size)):
            board[y_up][x] = 1
            board[y_down][x] = 1

        line_size += (map_width / map_height)
        y_up += 1
        y_down -= 1


board_functions = [
        draw_circle,
        draw_triangle,
        draw_losange
        ]
