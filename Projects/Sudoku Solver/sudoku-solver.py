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
    return None

# Validation
def valid(baord, number, position):
    # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    
    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Check cube
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    
    return True

# Solves the problem (Recursive)
def solve(board):
    empty = get_empty(board = board)
    if not empty:
        return True
    else:
        row, column = empty

    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i

            if solve(board = board):
                return True
            board[row][column] = 0
    
    return False

# Main
print('Initial Board:')
print_board(board = board)

solve(board = board)

print('Solved Board:')
print_board(board = board)