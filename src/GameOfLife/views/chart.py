from mesa.visualization.modules import ChartModule

from src.GameOfLife.params import CANVAS_SIZE

chart_currents = ChartModule(
    [
        {"Label": "Rich Agents", "Color": "blue"},
        {"Label": "Normal Agents", "Color": "green"},
        {"Label": "Poor Agents", "Color": "red"},
    ],
    canvas_height=CANVAS_SIZE,
    data_collector_name="data_collector_currents"
)
