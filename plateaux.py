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

    return map_height, board


def draw_triangle(board, map_width, map_height):
    """
        Draws a triangle shape with 1 values in the map.
        @parameters :
        - board : 2D matrix that represents the game board.
        - map_width : Game board width in cells.
        - map_height : Game board height in cells.
    """
    # Iterator used to fill the matrix with lines that will form the triangle.
    y = map_height - 1
    half_width = floor(float(map_width) / 2.0)
    line_size = half_width
    # While the line is not over
    while (line_size >= 0):
        # We iterate on the line to fill the 1 value
        for x in range(half_width - round(line_size), half_width + round(line_size)):
            board[y][x] = 1

        # Line size decrease as we reach the top
        line_size -= 1.0
        y -= 1

    # Looping over the board matrix to remove any useless line
    i = 0
    while i < len(board):
        # If the line does not contain a single 1 value, it is useless
        if 1 not in board[i]:
            del board[i]
            continue
        i += 1

    return len(board), board


def draw_losange(board, map_width, map_height):
    """
        Draws a losange shape with 1 values in the map.
        @parameters :
        - board : 2D matrix that represents the game board.
        - map_width : Game board width in cells.
        - map_height : Game board height in cells.
    """
    # Iterators used to fill the matrix with lines that will form the losange.
    y_up = 0
    y_down = map_height - 1
    half_width = float(map_width) / 2.0
    line_size = 0
    max_line_size = floor(map_width / 2)
    while (line_size <= max_line_size):
        for x in range(floor(half_width - line_size), ceil(half_width + line_size)):
            board[y_up][x] = 1
            board[y_down][x] = 1

        line_size += (map_width / map_height)
        y_up += 1
        y_down -= 1

    return map_height, board


# Array of functions allawing us to call any of them with an index chosen by the user.
board_functions = [
        draw_circle,
        draw_triangle,
        draw_losange
        ]
