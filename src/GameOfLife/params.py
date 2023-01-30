from mesa.visualization.ModularVisualization import UserSettableParameter

GRID_SIZE = 50
GRID_X_SIZE = 800
GRID_Y_SIZE = 800

CANVAS_SIZE = 300

SIMULATION_PARAMS = {
    "num_agents": UserSettableParameter(
        "slider",
        name="Quantidade de Agentes Vivos",
        value=(GRID_SIZE * GRID_SIZE) - 200,
        min_value=((GRID_SIZE - 30) * (GRID_SIZE - 30)) - 200,
        max_value=((GRID_SIZE - 30) * (GRID_SIZE + 30)) - 200,
        step=1,
        description=""
    ),
    "width": UserSettableParameter(
        "slider",
        name="Largura do quadro",
        value=GRID_SIZE,
        min_value=GRID_SIZE - 30,
        max_value=GRID_SIZE + 30,
        step=1,
        description=""
    ),
    "height": UserSettableParameter(
        "slider",
        name="Comprimento do quadro",
        value=GRID_SIZE,
        min_value=GRID_SIZE - 30,
        max_value=GRID_SIZE + 30,
        step=1,
        description=""
    ),
}

SERVER_NAME = "Jogo da Vida de Conway"