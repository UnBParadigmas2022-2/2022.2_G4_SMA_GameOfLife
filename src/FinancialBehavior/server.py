from src.FinancialBehavior.model import MoneyModel
from src.FinancialBehavior.params import SIMULATION_PARAMS, SERVER_NAME
from src.FinancialBehavior.views.chart import chart_currents
from src.FinancialBehavior.views.grid import grid_visualization

from mesa.visualization.ModularVisualization import ModularServer

visualization_elements = [grid_visualization, chart_currents]

financial_server = ModularServer(MoneyModel, visualization_elements, SERVER_NAME, SIMULATION_PARAMS)
