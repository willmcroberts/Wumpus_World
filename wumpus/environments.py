class WumpusWorld:
    def __init__(self, layout):
        self.width = layout.width
        self.height = layout.height
        self.pits = layout.pits
        self.wumpus = layout.wumpus
        self.gold = layout.gold
        self.agent_pos = layout.start
        self.agent_dir = layout.start_dir
        self.wumpus_alive = True
        self.game_over = False
        self.score = 0

    def get_percepts(self):
        """Return (stench, breeze, glitter, bump, scream) as booleans."""
        ...

    def apply_action(self, action):
        """
        action in {"MOVE_FORWARD", "TURN_LEFT", "TURN_RIGHT",
                   "GRAB", "SHOOT", "CLIMB"}
        Updates world state, score, game_over.
        Returns new_percepts.
        """
        ...