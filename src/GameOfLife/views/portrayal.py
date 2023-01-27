from src.GameOfLife.agent import CellAgent

def agent_portrayal(agent: CellAgent):
    portrayal = {
        "Shape": "circle",
        "Filled": "true",
        "r": 0.8,
        "Layer": 0
    }

    if agent.alive: 
        portrayal["Color"] = "green"

    else:
        portrayal["Color"] = "black"

    return portrayal
