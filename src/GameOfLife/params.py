from mesa.visualization.ModularVisualization import UserSettableParameter

GRID_SIZE = 5
WINDOW_X_SIZE = 800
WINDOW_Y_SIZE = 800

SIMULATION_PARAMS = {
    "alive_cells": UserSettableParameter(
        "slider",
        name="Número de celulas vivas na partida do jogo",
        value=(GRID_SIZE*GRID_SIZE)/2,
        min_value=GRID_SIZE,
        max_value=GRID_SIZE*GRID_SIZE,
        step=5,
        description="Slider para definir a quantidade de células vivas na simulação"
    ),
    "size": GRID_SIZE,
}

SERVER_NAME = "Game of Life"
