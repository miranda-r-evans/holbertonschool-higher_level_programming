#!/usr/bin/python3
''' module to solve N queens puzzle
place N queens on a NxN chess board such that they do not attack eachother '''

from sys import argv


def checker(board, row, col):
    ''' this checks if the placement of a particular queen would conflict with
    queens already placed on the board '''
    mat_len = len(board)
    for i in range(mat_len):
        if row - i >= 0 and col - i >= 0 and board[row - i][col - i] == 1:
            return False
        if row - i >= 0 and col + i >= 0 and col + i < mat_len and \
           board[row - i][col + i] == 1:
            return False
        if board[i][col] == 1:
            return False
    return True


def print_board(board):
    ''' this prints the board as a list of x/y positions '''
    toprint = []
    mat_len = len(board)
    for row in range(mat_len):
        for col in range(mat_len):
            if board[row][col] == 1:
                break
        toprint.append([row, col])
    print(toprint)


def place_queen(board, row):
    ''' place_queen places queens if they do not intersect with other queens,
    and calls itself until a solution is found or cannot be found for the
    current placement of queens '''
    mat_len = len(board)
    if row == mat_len:
        print_board(board)
        return
    for col in range(mat_len):
        if checker(board, row, col) is True:
            board[row][col] = 1
            place_queen(board, row + 1)
            board[row][col] = 0


def main(argv):
    ''' main function does input checks, generates board, and calls recursive
    function '''
    if len(argv) != 2:
        print('Usage: nqueens N')
        return 1
    try:
        n = int(argv[1])
    except:
        print('N must be a number')
        return 1
    if n < 4:
        print('N must be at least 4')
        return 1
    board = [[0 for i in range(n)] for j in range(n)]
    place_queen(board, 0)

if __name__ == "__main__":
    main(argv)
