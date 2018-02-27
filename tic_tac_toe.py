import sys
import time
import getopt

def print_board(board):
    board = ''.join(board)
    if len(board) == 9:
        print ("                ")
        for line in range(3):
            line_str = ''
            line_bar = ['','|','|']
            for item in board[line*3+3]


if __name__ == "__main__":
    argv = sys.argv.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "hf:v:b",["first=", "board", "verbose"])
        for opt, arg in opts:
            if opt == '-h':
                print("%s -f x -b ___x___"%(__file__))
                sys.exit()
                elif opt in ("-v", "--verbose"):
                    print_board(board)
                elif opt in ("-b", "--board"):
                    if len(arg) == 9:
                        board = list(arg)
                    else:
                        print("wrong board!")

    except getopt.GetoptError:
        print("%s -f x -b ___x___"%(__file__))
        sys.exit(2)