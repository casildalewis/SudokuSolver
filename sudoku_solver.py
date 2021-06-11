
def print_board(board):
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