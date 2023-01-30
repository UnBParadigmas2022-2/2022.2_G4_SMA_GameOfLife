from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

from src.GameOfLife.agent import CellAgent


class CellModel(Model):
    def __init__(self, num_agents: int, width: int, height: int) -> None:
        self.num_agents = num_agents
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True

        self.data_collector_currents = DataCollector(
            {}
        )

        count_index = 0
        for i in range(width):
            for j in range(height):
                agent = CellAgent(count_index, self)
                count_index += 1

                self.schedule.add(agent)

                self.grid.place_agent(agent, (i,j))

    def step(self) -> None:
        self.schedule.step()
        # self.data_collector_currents.collect(self)
