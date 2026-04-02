# main.py

import time
from tictactoe.game import TicTacToe
from wumpus.environments import WumpusWorld
from wumpus.agents import WumpusAgent
from wumpus.layouts import tiny_layout

def run_tictactoe():
    print("=== Tic Tac Toe ===")
    print("You are O. AI is X.")
    print("Board positions are numbered 0–8.\n")

    game = TicTacToe()
    game.play(ai_player='X')


def run_wumpus_world():
    print("=== Wumpus World ===\n")

    layout = tiny_layout()
    env = WumpusWorld(layout)
    agent = WumpusAgent()

    percepts = env.get_percepts()
    agent.initialize(percepts)

    while not env.game_over:
        env.render()

        print("Percepts:", percepts)
        action = agent.next_action(percepts)
        print("Action:", action)

        percepts = env.apply_action(action)

        time.sleep(1.5)

    env.render()
    print("\nGame Over!")
    print(f"Final score: {env.score}")

def main():
    print("Choose a game:")
    print("1) Tic Tac Toe")
    print("2) Wumpus World\n")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        run_tictactoe()
    elif choice == "2":
        run_wumpus_world()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()