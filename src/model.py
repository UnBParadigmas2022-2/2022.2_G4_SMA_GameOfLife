from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation

from agent import CellAgent


class CellModel(Model):
    def __init__(self, num_agents: int, width: int, height: int) -> None:
        self.num_agents = num_agents
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True

        for idx in range(self.num_agents):
            agent = CellAgent(idx, self)
            self.schedule.add(agent)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x,y))

    def step(self) -> None:
        self.schedule.step()
