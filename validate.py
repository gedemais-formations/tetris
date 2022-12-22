score = 0

def check_columns(board, width, height):
    for x in range(width):
        column = []
        for y in range(height):
            column.append(board[y][x])

        if 1 in column:
            continue

        elif 2 in column:
            board = delete_column(board, height, x)

    return board

def check_rows(board, width, height):

    for y in range(height):
        row = []
        for x in range(width):
            row.append(board[y][x])

        if 1 in row:
            continue
        elif 2 in row:
            board = delete_row(board, y)

    return board


def delete_row(board, row):

    global score
    for i, cell in enumerate(board[row]):
        if cell == 2:
            board[row][i] = 1
            score += 1

    return board


def delete_column(board, height, col):

    global score
    for y in range(height):
        if board[y][col] == 2:
            board[y][col] = 1;
            score += 1

    return board


def delete_completes(board, width, height):

    # Checks for completed columns and rows
    board = check_columns(board, width, height)
    board = check_rows(board, width, height)

    return board


def validate_and_place(board, width, height, shape, column, row, piece, fails):

    # Get the size of the matrix describing our piece
    piece_size = len(piece[0])
    # Coordinates of the origin (left - up) of the piece matrix
    piece_x = column
    piece_y = row - piece_size + 1

    # Iteration over every cell of the matrix
    for y in range(piece_size):
        for x in range(piece_size):
            # Collision check to avoid misplacements
            if piece[y][x] == 1 and board[piece_y + y][piece_x + x] != 1:
                # If the piece can not be placed, then it is a fail.
                if fails + 1 == 3:
                    # After 3 fails, we exit
                    print("Too many errors. Goodbye !")
                    exit(1)
                return False, fails + 1

    # If everything is fine, then we just place the piece on the board.
    for y in range(piece_size):
        for x in range(piece_size):
            if piece[y][x] == 1:
                board[piece_y + y][piece_x + x] = 2

    return True, 0
