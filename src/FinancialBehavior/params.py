from mesa.visualization.ModularVisualization import UserSettableParameter

GRID_SIZE = 50
GRID_X_SIZE = 800
GRID_Y_SIZE = 800

CANVAS_SIZE = 300

SIMULATION_PARAMS = {
    "num_agents": UserSettableParameter(
        "slider",
        name="Número de agentes da simulação",
        value=40,
        min_value=20,
        max_value=150,
        step=1,
        description="Slider para definir a quantidade de agentes a serem simulados"
    ),
    "width": GRID_SIZE,
    "height": GRID_SIZE,
}

SERVER_NAME = "Financial Behavior"
