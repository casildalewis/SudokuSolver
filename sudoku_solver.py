
def solve_board (board):
    """
    Given a solvable state of the board, represented as a 2D list of integers with a 0 in the 
    empty space, this method finds the solution using backtracking.

    Args:
        board (list of lists): current state of the game

    returns: True if solved, False otherwise
    """

    # Find empty position
    pos = find_empty_pos(board)

    # If not found, board is solved
    if not pos:
        return True

    (row, col) = pos

    # Enter numbers from 1-9 in empty position until valid number is found
    for num in range(1, 10):
        # If num in position is valid,
        if validate_pos(board, pos, num):
            # enter it and solve recursively.
            board[row][col] = num
            if solve_board(board):
                return True

            # If board is unsolved at 9, return to zero to backtrack
            if num == 9:
                board[row][col] == 0

    # Board is unsolved.
    print_board(board)
    return False

def validate_pos(board, pos, num):
    """
    Given a state of the board, represented as a 2D list of integers with a 0 in the 
    empty space, this method finds out if a particular number is valid in the given position
    according to the rules of sudoku.

    Args:
        board (list of lists): current state of the game
        pos (tuple): given position to verify
        num (integer): given number

    returns: True if valid, False otherwise
    """
    (row, col) = pos

    # Verify column rule
    for i in range(0, 9):
        if board[i][col] == num and i!=row:
            return False

    # Verify row rule
    for j in range(0, 9):
        if board[row][j] == num and j!=col:
            return False

    # Verify box rule
    # TODO make this better

    if row%3 == 0:
        box_row = [row, row+1, row+2]
    elif row%3 == 1:
        box_row = [row-1, row, row+1]
    elif row%3 == 2:
        box_row = [row-2, row-1, row]

    if col%3 == 0:
        box_col = [col, col+1, col+2]
    elif col%3 == 1:
        box_col = [col-1, col, col+1]
    elif col%3 == 2:
        box_col = [col-2, col-1, col]

    for i in box_row:
        for j in box_col:
            if board[i][j] == num and (i!= row or j!=col):
                return False

    return True

def find_empty_pos (board):
    """
    Given a state of the board, represented as a 2D list of integers, this method 
    finds the first empty space (row major order) represented with a 0.

    Args:
        board (list of lists): current state of the game

    returns: position of empty space if found, None otherwise
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == 0):
                return (i, j)

    return None

def print_board(board):
    """
    This method prints out the board.

    Args:
        board (list of lists): current state of the game
    """
    print("    A  B  C   D  E  F   G  H  I")
    for i in range(len(board)):

        if(i%3 == 0):
            print("  -------------------------------")

        line = str(i+1) + " "
        for j in range(len(board[i])):
            if(j%3 == 0):
                line += "|"
            
            if(board[i][j] == 0):
                line += "   "
            else:
                line += " " + str(board[i][j]) + " "
        line += "|"
        print(line)

    print("  -------------------------------")

board1 = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

if __name__ == "__main__":
    print_board(board1)
    if solve_board(board1):
        print_board(board1)
    else:
        print("unsolved")
