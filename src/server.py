from src.FinancialBehavior.server import financial_server
from src.GameOfLife.server import game_of_life_server
import os

financial_behavior = os.environ.get("FINANCIAL_BEHAVIOR", False)

server = None

if financial_behavior == "true":
    server = financial_server
else:
    server = game_of_life_server