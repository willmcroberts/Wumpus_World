# test_wumpus.py

from wumpus.environments import WumpusWorld
from wumpus.agents import WumpusAgent

def test_percept_rules():
    env = WumpusWorld()
    env.place_pit(1, 2)
    env.place_wumpus(2, 1)
    env.place_gold(0, 0)

    percept = env.get_percept(1, 1)

    assert percept.breeze is True, "Breeze should be present near a pit"
    assert percept.stench is True, "Stench should be present near the Wumpus"
    assert percept.glitter is False, "No glitter unless gold is in the same square"

def test_agent_avoids_unsafe():
    agent = WumpusAgent()

    agent.kb.mark_unsafe((2, 2))

    safe_moves = agent.get_safe_moves()

    assert (2, 2) not in safe_moves, "Agent should not consider known-unsafe squares"

def test_kb_updates_after_percept():
    agent = WumpusAgent()

    percept = {
        "breeze": True,
        "stench": False,
        "glitter": False
    }

    agent.update_kb(percept)

    assert agent.kb.has_fact("breeze_at", agent.position), \
        "KB should record breeze at the agent's location"