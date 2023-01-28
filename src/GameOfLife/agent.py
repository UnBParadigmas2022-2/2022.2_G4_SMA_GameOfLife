from mesa import Agent, Model

class CellAgent(Agent):
    def __init__(self, unique_id: int, model: Model, alive: bool) -> None:
        super().__init__(unique_id, model)
        self.alive = alive

    def check_neighbors(self) -> None:
        neighbors = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        print(len(neighbors))
        print(neighbors[0])
        # TODO: realizar filtro de vizinhos vivos
        def count_neighbors(self, grid):
            neighbors = 0
            for i in range(self.x-1, self.x+2):
                for j in range(self.y-1, self.y+2):
                    if (i, j) != (self.x, self.y) and 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                        if grid[i][j].state == 1:
                            neighbors += 1
            return neighbors

        # TODO: realizar filtro de vizinhos mortos
        def count_dead_neighbors(self, grid):
            dead_neighbors = 0
            for i in range(self.x-1, self.x+2):
                for j in range(self.y-1, self.y+2):
                    if (i, j) != (self.x, self.y) and 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                        if grid[i][j].state == 0:
                            dead_neighbors += 1
            return dead_neighbors
        # TODO: Acionar método de renaissance ou death de acordo com as regras do jogo
        def update_cell(self, x, y):
            cell = self.grid[x][y]
            live_neighbors = cell.count_neighbors(self.grid)
            dead_neighbors = cell.count_dead_neighbors(self.grid)
            if cell.state == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    cell.death()
                if live_neighbors >= 3:
                    cell.death()
                if live_neighbors < 2:
                    cell.death()
            else:
                if dead_neighbors == 3:
                    cell.renaissance()

    def renaissance(self) -> None: #revive
        self.alive = True

    def death(self) -> None: #morre
        self.alive = False

    def step(self) -> None:
        print("Agent " + str(self.unique_id) + " stepped!")