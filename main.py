from src.server import server
import os

if __name__ == "__main__":
    if server is not None:
        server.port = os.environ.get("PORT", 8521)
        server.launch()