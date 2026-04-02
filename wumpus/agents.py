class WumpusAgent:
    def __init__(self):
        self.kb = ...
        self.has_arrow = True
        self.has_gold = False
        self.position = (1, 1)
        self.direction = "EAST"
        self.alive = True

    def initialize(self, initial_percepts):
        """Called at start of episode."""
        ...

    def tell(self, percepts):
        """Update KB with new percepts."""
        ...

    def ask(self):
        """Infer safe cells / Wumpus location, choose next action."""
        ...

    def next_action(self, percepts):
        """
        Convenience wrapper:
        - self.tell(percepts)
        - action = self.ask()
        - return action
        """
        ...