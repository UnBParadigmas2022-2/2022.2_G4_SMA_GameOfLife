from src.GameOfLife.agent import CellAgent

def agent_portrayal(agent: CellAgent):
    portrayal = {
        "Shape": "rect",
        "Filled": "true",
        "Color": "#FFFFFF",
        "Layer": 0,
        "w": 0.8,
        "h": 0.8,
    }

    if agent.alive:
        portrayal["Color"] = "#419939"

    return portrayal
