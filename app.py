board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - - - - - ')

        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print(' | ', end="")

            print(board[i][j], " ", end="")

            if j == 8:
                print("")


def find_zeros():
    zeros = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                zeros.append(((i, j), 1))
    return zeros


zeros = find_zeros()


def solved():
    # [((0, 2), 1), ((0, 4), 1), ....]

    for i in range(len(zeros)):
        backtrack(zeros[i][0], zeros[i][1])

    return board


def backtrack(pos, start):
    found_number = find_number(pos, start)
    if found_number != 0:
        board[pos[0]][pos[1]] = found_number
        zeros[pos[0]][1] = found_number
    else:
        backtrack(zeros[pos[0]-1][0], zeros[pos[0]-1][1])


def find_number(pos, start):
    for i in range(start, 9):
        if is_number_valid(i, pos):
            return i
    return 0


def is_number_valid(n, pos):
    if n in board[pos[0]]:
        return False

    for i in range(len(board)):
        if board[i][pos[1]] == n:
            return False

    square = get_square(pos)
    for i in range(square[0][1], square[1][1]):
        for j in range(square[0][0], square[1][0]):
            if n == board[i][j]:
                return False

    return True


def get_square(point):
    for j in range(0, len(board[0])-1, 3):
        for i in range(0, len(board[0])-1, 3):
            if (i, j) <= point and (i+2, j+2) >= point:
                return (i, j), (i+2, j+2)


print("Board :")
print_board(board)
print("\n")
print("Starting solving...")
print_board(solved())
