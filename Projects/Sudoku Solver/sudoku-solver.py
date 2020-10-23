# The matrix
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

# Prints the matrix
def print_board(board):
    for i in range(len(board)):

        # Horizontal seperator
        if i % 3 == 0 and i != 0:
            print('- ' * 11, end = '\n')

        for j in range(len(board[i])):

            # Vertical seperator
            if j % 3 == 0 and j != 0:
                print('| ', end = '')
                
            print(board[i][j], '', end = '')
        print()

# Gets an empty cell
def get_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
