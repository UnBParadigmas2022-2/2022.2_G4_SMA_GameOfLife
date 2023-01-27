from agent import MoneyAgent
from model import MoneyModel

from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

SIZE = 50
X_SIZE = 800
Y_SIZE = 800

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

simulation_params = {
    "num_agents": UserSettableParameter(
        "slider",
        name="Número de agentes da simulação",
        value=40,
        min_value=20,
        max_value=150,
        step=1,
        description="Slider para definir a quantidade de agentes a serem simulados"
    ),
    "width": SIZE,
    "height": SIZE
}

chart_currents = ChartModule(
    [
        {"Label": "Rich Agents", "Color": "blue"},
        {"Label": "Normal Agents", "Color": "green"},
        {"Label": "Poor Agents", "Color": "red"},
    ],
    canvas_height=300,
    data_collector_name="data_collector_currents"
)

grid_visualization = CanvasGrid(agent_portrayal, SIZE, SIZE, X_SIZE, Y_SIZE)
server = ModularServer(MoneyModel, [grid_visualization, chart_currents], "Financial Behavior", simulation_params)
server.port = 8521
server.launch()