from mesa.visualization.modules import CanvasGrid

from src.GameOfLife.views.portrayal import agent_portrayal
from src.GameOfLife.params import GRID_SIZE, WINDOW_X_SIZE, WINDOW_Y_SIZE

grid_visualization = CanvasGrid(agent_portrayal, GRID_SIZE, WINDOW_X_SIZE, WINDOW_Y_SIZE)
