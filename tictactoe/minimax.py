# minimax.py

def best_move(board, player):
    maximizing = (player == 'X')
    best_score = float('-inf') if maximizing else float('inf')
    best_move = None

    for move in available_moves(board):
        new_board = board.copy()
        new_board[move] = player
        score = minimax(new_board, maximizing=False, player=player)
        if maximizing and score > best_score:
            best_score = score
            best_move = move
        if not maximizing and score < best_score:
            best_score = score
            best_move = move

    return best_move


def minimax(board, maximizing, player):
    opponent = 'O' if player == 'X' else 'X'

    if winner(board) == player:
        return 1
    if winner(board) == opponent:
        return -1
    if terminal(board):
        return 0

    if maximizing:
        best = float('-inf')
        for move in available_moves(board):
            new_board = board.copy()
            new_board[move] = player
            val = minimax(new_board, False, player)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for move in available_moves(board):
            new_board = board.copy()
            new_board[move] = opponent
            val = minimax(new_board, True, player)
            best = min(best, val)
        return best

def available_moves(board):
    return [i for i, v in enumerate(board) if v is None]

def winner(board):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in wins:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

def terminal(board):
    if winner(board) is not None:
        return True
    if all(cell is not None for cell in board):
        return True
    return False