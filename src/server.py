from src.FinancialBehavior.server import financial_server
from src.GameOfLife.server import game_of_life_server

financial_behavior = False # Vai ser uma env var

server = None

if financial_behavior:
    server = financial_server
else:
    server = game_of_life_server