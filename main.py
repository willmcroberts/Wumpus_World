# main.py

from tictactoe.game import TicTacToe
from wumpus.environments import WumpusWorld
from wumpus.agents import WumpusAgent
from wumpus.layouts import tiny_layout

def main():
    print("=== Tic Tac Toe ===")
    print("You are O. AI is X.")
    print("Board positions are numbered 0–8.\n")

    game = TicTacToe()
    game.play(ai_player='X')

if __name__ == "__main__":
    main()