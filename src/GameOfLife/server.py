from src.GameOfLife.model import CellModel
from src.GameOfLife.params import SIMULATION_PARAMS, SERVER_NAME
from src.GameOfLife.views.chart import chart_currents
from src.GameOfLife.views.grid import grid_visualization

from mesa.visualization.ModularVisualization import ModularServer

visualization_elements = [grid_visualization, chart_currents]

game_of_life_server = ModularServer(CellModel, visualization_elements, SERVER_NAME, SIMULATION_PARAMS)
