# game.py

from . import minimax

class TicTacToe:
    def __init__(self):
        self.board = [None] * 9
        self.current_player = 'X'

    def print_board(self):
        RESET = "\033[0m"
        GREEN = "\033[92m"
        RED = "\033[91m"
        BLUE = "\033[94m"

        def cell(i):
            v = self.board[i]
            if v == 'X':
                return RED + 'X' + RESET
            elif v == 'O':
                return BLUE + 'O' + RESET
            else:
                return GREEN + str(i) + RESET

        print()
        print(GREEN + f" {cell(0)} | {cell(1)} | {cell(2)} " + RESET)
        print(GREEN + "---+---+---" + RESET)
        print(GREEN + f" {cell(3)} | {cell(4)} | {cell(5)} " + RESET)
        print(GREEN + "---+---+---" + RESET)
        print(GREEN + f" {cell(6)} | {cell(7)} | {cell(8)} " + RESET)
        print()

    def available_moves(self):
        return [i for i, v in enumerate(self.board) if v is None]

    def make_move(self, index, player):
        if self.board[index] is None:
            self.board[index] = player
            return True
        return False

    def winner(self):
        wins = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        for a,b,c in wins:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def terminal(self):
        if self.winner() is not None:
            return True
        if all(cell is not None for cell in self.board):
            return True
        return False

    def play(self, ai_player='X'):
        while not self.terminal():
            self.print_board()

            if self.current_player == ai_player:
                move = minimax.best_move(self.board, ai_player)
                print(f"AI ({ai_player}) chooses {move}")
                self.make_move(move, ai_player)
            else:
                # Human move (or random/scripted later)
                move = int(input("Your move (0-8): "))
                if move not in self.available_moves():
                    print("Invalid move.")
                    continue
                self.make_move(move, self.current_player)

            self.current_player = 'O' if self.current_player == 'X' else 'X'

        self.print_board()
        w = self.winner()
        if w:
            print(f"Winner: {w}")
        else:
            print("Draw.")