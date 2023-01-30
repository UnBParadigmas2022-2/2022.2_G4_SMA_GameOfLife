from mesa import Agent, Model
from random import choice

class CellAgent(Agent):
    def __init__(self, unique_id: int, model: Model) -> None:
        super().__init__(unique_id, model)
        self.alive = choice([True, False])

    def renaissance(self) -> None:
        self.alive = True

    def extermination(self) -> None:
        self.alive = False

    def get_alive_neighbors(self) -> None:
        neighbors = self.model.grid.get_neighbors(
            self.pos, moore=True, include_center=False
        )

        alive = list(filter(lambda agent: agent.alive, neighbors))

        return alive

    def step(self) -> None:
        alive = self.get_alive_and_dead_neighbors()

        if self.alive:
            if len(alive) <= 1:
                self.extermination()
            
            elif len(alive) > 3:
                self.extermination()
            
        else:
            if len(alive) == 2 or len(alive) == 3:
                self.renaissance()
