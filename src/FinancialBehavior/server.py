from model import MoneyModel
from params import SIMULATION_PARAMS, SERVER_NAME
from views import grid_visualization, chart_currents

from mesa.visualization.ModularVisualization import ModularServer

visualization_elements = [grid_visualization, chart_currents]

financial_server = ModularServer(MoneyModel, visualization_elements, SERVER_NAME, SIMULATION_PARAMS)
financial_server.port = 8521
financial_server.launch()