# layouts.py

class WumpusLayout:
    def __init__(self, width, height, pits, wumpus, gold, start, start_dir):
        self.width = width
        self.height = height
        self.pits = pits
        self.wumpus = wumpus
        self.gold = gold
        self.start = start
        self.start_dir = start_dir

def tiny_layout():
    return WumpusLayout(
        width=4,
        height=4,
        pits={(3, 1), (3, 3)},
        wumpus=(1, 3),
        gold=(2, 3),
        start=(1, 1),
        start_dir="EAST"
    )