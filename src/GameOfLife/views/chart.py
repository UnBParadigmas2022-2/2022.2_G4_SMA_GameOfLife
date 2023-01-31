from mesa.visualization.modules import ChartModule

from src.GameOfLife.params import CANVAS_SIZE

chart_currents = ChartModule(
    [
        {"Label": "cell alive", "Color": "green"},
        {"Label": "cell dead", "Color": "gray"},
    ],
    canvas_height=CANVAS_SIZE,
    data_collector_name="data_collector_currents"
)
