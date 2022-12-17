
def check_columns(board, width, height):
    for x in range(width):
        column = []
        for y in range(height):
            column.append(board[y][x])

        if 1 in column:
            return -1

        elif 2 in column:
            return x


def check_rows(board, width, height):
    for y in range(height):
        row = []
        for x in range(width):
            row.append(board[y][x])

        if 1 in row:
            return -1

        elif 2 in row:
            return y


def delete_column(board, height, col):
    for y in range(height):
        if board[y][col] == 2:
            board[y][col] = 1;

    return board


def delete_completes(board, width, height):

    col = check_columns(board, width, height)
    if col >= 0 :
        board = delete_column(board, height, col)

    row = check_rows(board, width, height)
    if row >= 0 :
        board[row] = board[row].replace(2, 1)

    return board

def validate_and_place(board, column, row, piece, fails):
    
    piece_size = len(piece[0])
    piece_x = column
    piece_y = row - piece_size + 1

    print(piece_x, piece_y)
    for y in range(piece_size):
        for x in range(piece_size):
            if piece[y][x] == 1 and board[piece_y + y][piece_x + x] != 1:
                if fails + 1 == 3:
                    print("Too many errors. Goodbye !")
                    exit(1)
                else:
                    print("Can not place piece. {} try left !".format(2 - fails))
                return False, fails + 1

    for y in range(piece_size):
        for x in range(piece_size):
            if piece[y][x] == 1:
                board[piece_y + y][piece_x + x] = 2

    return True, 0
