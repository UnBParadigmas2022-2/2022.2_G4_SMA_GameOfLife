from src.FinancialBehavior.server import financial_server

financial_behavior = True # Vai ser uma env var

server = None

if financial_behavior:
    server = financial_server
