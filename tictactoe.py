"""
Tic Tac Toe Player
"""
import copy
import math

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
    Returns player who has the next turn ona board.
    """

    x_list = []
    y_list = []
    for elem in board:
        for sym in elem:
            if sym == X:
                x_list.append(sym)
            elif sym == O:
                y_list.append(sym)
    if len(x_list) > len(y_list):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if (board[i][j] is not EMPTY):
        raise ValueError
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    win_ways = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for a, b, c in win_ways:
        player = board[a[0]][a[1]]

        if (player is not EMPTY and player == board[b[0]][b[1]] and player == board[c[0]][c[1]]):
            return player

    return None
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_slots = False
    for i in board:
        for j in i:
            if j == EMPTY:
                empty_slots = True

    if winner(board) in (X, O):
        return True
    if not empty_slots:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    if winner(board) == EMPTY:
        return 0


# MAX_VAL_DICT = {}
# MIN_VAL_DICT = {}
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    best_action = None
    best_value = -math.inf if current_player == X else math.inf
    for action in actions(board):
        if current_player == X:
            value = min_value(result(board, action))
            if best_value < value:
                best_value = value
                best_action = action
        else:
            value = max_value(result(board, action))
            if best_value > value:
                best_value = value
                best_action = action

    print(f'optimal move: {best_action}')
    return best_action



def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):

    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

