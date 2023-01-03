"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = 0
    count_O = 0
    if not terminal(board):
        for row in board:
            count_X += row.count(X)
            count_O += row.count(O)
        if count_X > count_O:
            return O
        else:
            return X
    else:
        return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    if not terminal(board):
        for i in range(3):
            for j in range(3):
                if board[i][j] is EMPTY:
                    actions.add((i, j))
        return actions
    else:
        return None


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_symbol = player(board)
    new_board = deepcopy(board)
    i, j = action
    if new_board[i][j] != EMPTY:
        raise Exception
    else:
        new_board[i][j] = player_symbol
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player_sym in (O, X):
        for row in board:
            if row == [player_sym] * 3:
                return player_sym

        for i in range(3):
            if [board[x][i] for x in range(3)] == [player_sym] * 3:
                return player_sym

        if [board[i][i] for i in range(3)] == [player_sym] * 3:
            return player_sym

        if [board[2 - i][i] for i in range(3)] == [player_sym] * 3:
            return player_sym
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player_win = winner(board)
    if player_win == O:
        return -1
    elif player_win == X:
        return 1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def min_value(board):
        optimal_action = ()
        if terminal(board):
            return utility(board), optimal_action
        else:
            v = math.inf
            for action in actions(board):
                maxvalue = max_value(result(board, action))[0]
                if maxvalue < v:
                    v = maxvalue
                    optimal_action = action
            return v, optimal_action

    def max_value(board):
        optimal_action = ()
        if terminal(board):
            return utility(board), optimal_action
        else:
            v = -math.inf
            for action in actions(board):
                minvalue = min_value(result(board, action))[0]
                if minvalue > v:
                    v = minvalue
                    optimal_action = action
            return v, optimal_action

    player_now = player(board)

    if terminal(board):
        return None

    if player_now == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]
