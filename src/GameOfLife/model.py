from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import random

from src.GameOfLife.agent import CellAgent


class CellModel(Model):
    def __init__(self, width: int, height: int, num_agents: int) -> None:
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True

        self.data_collector_currents = DataCollector(
            {}
        )

        index = 0

        for _ in range(num_agents):
            x = random.randint(0, width-1)    
            y = random.randint(0, height-1)

            agent = CellAgent(index, self, True)
            index += 1
            self.schedule.add(agent)

            self.grid.place_agent(agent, (x,y))


        while self.grid.exists_empty_cells:

            coord = self.grid.find_empty()
            if coord is None:
                return
            else:
                print(coord)
                agent = CellAgent(index, self, False)
                index += 1

                self.schedule.add(agent)
                self.grid.place_agent(agent, coord)

    def step(self) -> None:
        self.schedule.step()
        # self.data_collector_currents.collect(self)
