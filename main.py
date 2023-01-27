from src.server import server

if __name__ == "__main__":
    if server is not None:
        server.port = 8521
        server.launch()