from agent import MoneyAgent
from params import SIZE, X_SIZE, Y_SIZE

from mesa.visualization.modules import CanvasGrid, ChartModule

def agent_portrayal(agent: MoneyAgent):
    portrayal = {
        "Shape": "circle",
        "Filled": "true",
    }

    if agent.money >= 3:
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.8
    
    elif agent.money > 0:
        portrayal["Color"] = "green"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.6
    
    else:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 2
        portrayal["r"] = 0.4
    
    return portrayal

grid_visualization = CanvasGrid(agent_portrayal, SIZE, SIZE, X_SIZE, Y_SIZE)

chart_currents = ChartModule(
    [
        {"Label": "Rich Agents", "Color": "blue"},
        {"Label": "Normal Agents", "Color": "green"},
        {"Label": "Poor Agents", "Color": "red"},
    ],
    canvas_height=300,
    data_collector_name="data_collector_currents"
)