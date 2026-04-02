# Tic Tac Toe Tests

from tictactoe.game import TicTacToe

def test_legal_moves():
    board = [
        ["X", "O", "X"],
        ["-", "O", "-"],
        ["-", "-", "X"]
    ]

    game = TicTacToe()
    moves = game.get_legal_moves()

    assert moves == [(1,0), (2,0), (2,1)], "Legal moves must be empty squares only"

def test_terminal_state_win():
    board = [
        ["X", "X", "X"],
        ["O", "-", "O"],
        ["-", "-", "-"]
    ]

    game = TicTacToe()

    assert game.is_terminal() is True
    assert game.get_winner() == "X"

def test_minimax_optimal_move():
    board = [
        ["X", "X", "-"],
        ["O", "O", "-"],
        ["-", "-", "-"]
    ]

    game = TicTacToe()

    best_move = game.minimax_decision()

    assert best_move == (0, 2), "Minimax should choose the winning move"