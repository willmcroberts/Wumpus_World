# environments.py

class WumpusWorld:
    DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]

    MOVES = {
        "NORTH": (0, 1),
        "EAST": (1, 0),
        "SOUTH": (0, -1),
        "WEST": (-1, 0)
    }

    def __init__(self, layout):
        self.width = layout.width
        self.height = layout.height
        self.pits = layout.pits
        self.wumpus = layout.wumpus
        self.gold = layout.gold

        self.agent_pos = layout.start
        self.agent_dir = layout.start_dir

        self.has_gold = False
        self.arrow_available = True
        self.wumpus_alive = True

        self.game_over = False
        self.score = 0

    def get_percepts(self):
        x, y = self.agent_pos

        stench = any(
            (abs(x - wx) + abs(y - wy) == 1)
            for (wx, wy) in [self.wumpus]
        ) if self.wumpus_alive else False

        breeze = any(
            (abs(x - px) + abs(y - py) == 1)
            for (px, py) in self.pits
        )

        glitter = (self.agent_pos == self.gold and not self.has_gold)

        bump = False
        scream = False

        return (stench, breeze, glitter, bump, scream)

    def apply_action(self, action):
        if self.game_over:
            return self.get_percepts()

        if action == "MOVE_FORWARD":
            self._move_forward()

        elif action == "TURN_LEFT":
            self._turn_left()

        elif action == "TURN_RIGHT":
            self._turn_right()

        elif action == "GRAB":
            if self.agent_pos == self.gold and not self.has_gold:
                self.has_gold = True
                self.score += 1000

        elif action == "SHOOT":
            if self.arrow_available:
                self.arrow_available = False
                if self._arrow_hits_wumpus():
                    self.wumpus_alive = False
                    self.score += 100
            self.score -= 10

        elif action == "CLIMB":
            if self.agent_pos == (1, 1):
                self.game_over = True

        if self.agent_pos in self.pits:
            self.score -= 1000
            self.game_over = True

        if self.agent_pos == self.wumpus and self.wumpus_alive:
            self.score -= 1000
            self.game_over = True

        return self.get_percepts()

    def _move_forward(self):
        dx, dy = self.MOVES[self.agent_dir]
        new_x = self.agent_pos[0] + dx
        new_y = self.agent_pos[1] + dy

        if 1 <= new_x <= self.width and 1 <= new_y <= self.height:
            self.agent_pos = (new_x, new_y)
        else:
            pass

        self.score -= 1

    def _turn_left(self):
        idx = self.DIRECTIONS.index(self.agent_dir)
        self.agent_dir = self.DIRECTIONS[(idx - 1) % 4]
        self.score -= 1

    def _turn_right(self):
        idx = self.DIRECTIONS.index(self.agent_dir)
        self.agent_dir = self.DIRECTIONS[(idx + 1) % 4]
        self.score -= 1

    def _arrow_hits_wumpus(self):
        # Simple straight-line check
        ax, ay = self.agent_pos
        wx, wy = self.wumpus

        if self.agent_dir == "NORTH" and ax == wx and wy > ay:
            return True
        if self.agent_dir == "SOUTH" and ax == wx and wy < ay:
            return True
        if self.agent_dir == "EAST" and ay == wy and wx > ax:
            return True
        if self.agent_dir == "WEST" and ay == wy and wx < ax:
            return True

        return False

    def render(self):
        print("\nCurrent World State:")
        print(f"Agent at {self.agent_pos}, facing {self.agent_dir}")
        print(f"Has gold: {self.has_gold}, Wumpus alive: {self.wumpus_alive}")
        print()

        for y in range(self.height, 0, -1):
            row = []
            for x in range(1, self.width + 1):
                pos = (x, y)

                if pos == self.agent_pos:
                    row.append("A")
                elif pos == self.wumpus and self.wumpus_alive:
                    row.append("W")
                elif pos in self.pits:
                    row.append("P")
                elif pos == self.gold and not self.has_gold:
                    row.append("G")
                else:
                    row.append(".")
            print("  ".join(row))
        print()