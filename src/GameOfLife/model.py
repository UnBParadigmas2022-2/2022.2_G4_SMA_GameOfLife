from mesa import Model
from mesa.space import SingleGrid
from mesa.time import RandomActivation

from src.GameOfLife.agent import CellAgent

class CellModel(Model):
    def __init__(self, alive_cells: int, size: int) -> None:
        self.alive_cells = alive_cells
        self.grid = SingleGrid(width=size, height=size, torus=True)
        self.schedule = RandomActivation(self)
        self.running = True

        # TODO: adicionar atributo de data collector

        id_count = 0
        for i in range(size):
            for j in range(size):
                agent = CellAgent(id_count, self, True) #TODO: adicionar método de randomizar células vivas e mortas, a partir do input de número de células vivas
                id_count += 1

                self.schedule.add(agent)

                self.grid.place_agent(agent, (i,j))
            
    def step(self) -> None:
        self.schedule.step()
        # TODO: acionar o data collector pra coletar informações

    # TODO: adicionar método de coleta de células vivas
    # TODO: Adicionar método de coleta de células mortas
    