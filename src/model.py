from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

from agent import CellAgent


class CellModel(Model):
    def __init__(self, num_agents: int, width: int, height: int) -> None:
        self.num_agents = num_agents
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True

        self.data_collector_currents = DataCollector(
            {
                "Rich Agents": CellModel.get_rich_agents,
                "Normal Agents": CellModel.get_normal_agents,
                "Poor Agents": CellModel.get_poor_agents,
            }
        )

        for idx in range(self.num_agents):
            agent = CellAgent(idx, self)
            self.schedule.add(agent)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x,y))

    def step(self) -> None:
        self.schedule.step()
        self.data_collector_currents.collect(self)

    @staticmethod
    def get_rich_agents(model) -> int:
        return sum([1 for agent in model.schedule.agents if agent.money >= 3])

    @staticmethod
    def get_normal_agents(model) -> int:
        return sum([1 for agent in model.schedule.agents if agent.money > 0 and agent.money < 3])

    @staticmethod
    def get_poor_agents(model) -> int:
        return sum([1 for agent in model.schedule.agents if agent.money == 0])
