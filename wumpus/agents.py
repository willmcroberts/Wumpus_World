# agents.py

import random

class WumpusAgent:
    def __init__(self):
        self.visited = set()
        self.safe = set()
        self.has_gold = False

    def initialize(self, percepts):
        self.visited.add((1, 1))
        self.safe.add((1, 1))

    def next_action(self, percepts):
        stench, breeze, glitter, bump, scream = percepts

        if glitter:
            self.has_gold = True
            return "GRAB"

        if self.has_gold:
            return "CLIMB"

        if stench or breeze:
            return random.choice(["TURN_LEFT", "TURN_RIGHT"])

        return "MOVE_FORWARD"