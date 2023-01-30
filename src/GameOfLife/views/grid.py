from mesa.visualization.modules import CanvasGrid

from src.GameOfLife.views.portrayal import agent_portrayal
from src.GameOfLife.params import GRID_SIZE, GRID_X_SIZE, GRID_Y_SIZE

grid_visualization = CanvasGrid(agent_portrayal, GRID_SIZE, GRID_SIZE, GRID_X_SIZE, GRID_Y_SIZE)
