"""
Tic Tac Toe Player
"""

import random
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
    Returns player who has the next turn on a board.
    """
    p = True
    for line in board:
        for cell in line:
            p = p ^ (cell is EMPTY)
    return "XO"[p % 2]


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    x = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                x.add((i, j))
    return x


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    return [[board[i][j] if (i,j)!=action else player(board) for i in range(3)] for j in range(3)]


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] is not None and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] is not None and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] is not None and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] is not None and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return EMPTY

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board): return True
    for line in board:
        for cell in line:
            if cell is EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    dictionary = {
        'X': 1,
        'O': -1,
        None: 0
    }
    return dictionary[winner(board)]


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    bestAction = None   
    goal = 2*('OX'.index(player(board)))-1
    print(goal)
    bestEvaluation = -goal
    for action in actions(board):
        evaluation = evaluate(result(board, action), -goal)
        #objetivo 1
        #evaluation 0
        #bestEvaluation -1
        print(evaluation)
        if (goal == -1 and (evaluation - bestEvaluation < 0)) or\
           (goal == 1 and (evaluation - bestEvaluation > 0)):
            bestEvaluation = evaluation
            bestAction = action
    return bestAction

def evaluate(board, goal = None):
    # The evaluation of a board is defined to be the worst evaluation it can achieve
    if goal is None: goal = 2*('OX'.index(player(board)))-1
    if terminal(board): return utility(board)
    bestEvaluation = -goal
    for action in actions(board):
        evaluation = evaluate(result(board, action), -goal)
        if (goal == -1 and (evaluation - bestEvaluation < 0)) or\
           (goal == 1 and (evaluation - bestEvaluation > 0)):
            bestEvaluation = evaluation
    return bestEvaluation

if __name__ == '__main__':
    board = initial_state()
    # print(player(board))
    for i in range(9):
        board[i % 3][i//3] = 'X'
    # print(terminal(board))
    board = initial_state()
    # print(actions(board))
    #print(evaluate(board))
    board[0][0] = 'X'
    board[1][0] = 'X'
    board[1][1] = 'O'
    board[2][2] = 'O'
    print(evaluate(board))
    print(minimax(board))
