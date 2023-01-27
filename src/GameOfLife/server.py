from src.GameOfLife.model import CellModel
from src.GameOfLife.params import SIMULATION_PARAMS, SERVER_NAME
from src.GameOfLife.views.grid import grid_visualization

from mesa.visualization.ModularVisualization import ModularServer

visualization_elements = [grid_visualization]

# TODO: Está quebrando em algum lugar, entre o agente e o server. É necessário arrumar.
# TODO: Este todo é o mais prioritário.
game_of_life_server = ModularServer(CellModel, visualization_elements, SERVER_NAME, SIMULATION_PARAMS)