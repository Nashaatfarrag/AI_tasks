import numpy as np
import random
# assuming that each column should contain a queen


def init_board():
    board = [[0 for i in range(0, 4)] for j in range(0, 4)]
    # initialize queens at random places
    for col in range(0, 4):
        rand_row = random.randint(0, 3)
        board[rand_row][col] = "Q"
    return board


def get_h(board):
    # these are separate for easier debugging
    totalhcost = 0
    totaldcost = 0
    for i in range(0, 4):
        for j in range(0, 4):
            # if this node is a queen, calculate all violations
            if board[i][j] == "Q":
                # subtract 2 so don't count self
                # sideways and vertical
                totalhcost -= 2
                for k in range(0, 4):
                    if board[i][k] == "Q":
                        totalhcost += 1
                    if board[k][j] == "Q":
                        totalhcost += 1
                # calculate diagonal violations
                k, l = i + 1, j + 1
                while k < 4 and l < 4:
                    if board[k][l] == "Q":
                        totaldcost += 1
                    k += 1
                    l += 1
                k, l = i + 1, j - 1
                while k < 4 and l >= 0:
                    if board[k][l] == "Q":
                        totaldcost += 1
                    k += 1
                    l -= 1
                k, l = i - 1, j + 1
                while k >= 0 and l < 4:
                    if board[k][l] == "Q":
                        totaldcost += 1
                    k -= 1
                    l += 1
                k, l = i - 1, j - 1
                while k >= 0 and l >= 0:
                    if board[k][l] == "Q":
                        totaldcost += 1
                    k -= 1
                    l -= 1
    print((totaldcost+totalhcost)/2)
    return ((totaldcost + totalhcost) / 2)


def get_next_h(board):
    h = 99 * np.ones((4, 4))
    for i in range(0, 4):
        for j in range(0, 4):
            if board[i][j] == 'Q':
                continue
            h[i, j] = get_h(move(board, i, j))
    return h


def select_min(h):
    (x, y) = np.unravel_index(h.argmin(), h.shape)
    min_h_new = np.min(h)
    return x, y, min_h_new


def move(board, x, y):
    for k in range(0, 4):
        board[k][y] = 0
    board[x][y] = 'Q'
    return board


def show(board):
    mstr = ""
    for i in range(0, 4):
        for j in range(0, 4):
            mstr = mstr + str(board[i][j]) + " "
        mstr = mstr + "\n"
    print(mstr)


min_h = 999
board = init_board()
while True:
    show(board)
    h = get_next_h(board)
    x, y, min_h_new = select_min(h)
    if min_h_new >= min_h:
        break
    min_h = min_h_new
    board = move(board, x, y)
show(board)
