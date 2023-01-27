from mesa.visualization.ModularVisualization import UserSettableParameter

SIZE = 50
X_SIZE = 800
Y_SIZE = 800

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
    "width": SIZE,
    "height": SIZE
}

SERVER_NAME = "Financial Behavior"
