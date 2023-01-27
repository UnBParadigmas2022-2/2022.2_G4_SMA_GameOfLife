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
        # TODO: realizar filtro de vizinhos mortos
        # TODO: Acionar método de renaissance ou death de acordo com as regras do jogo

    def renaissance(self) -> None:
        self.alive = True

    def death(self) -> None:
        self.alive = False

    def step(self) -> None:
        print("Agent " + str(self.unique_id) + " stepped!")
