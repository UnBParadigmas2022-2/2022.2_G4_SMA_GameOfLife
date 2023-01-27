from mesa.visualization.modules import CanvasGrid

from src.FinancialBehavior.views.portrayal import agent_portrayal
from src.FinancialBehavior.params import GRID_SIZE, GRID_X_SIZE, GRID_Y_SIZE

grid_visualization = CanvasGrid(agent_portrayal, GRID_SIZE, GRID_SIZE, GRID_X_SIZE, GRID_Y_SIZE)
