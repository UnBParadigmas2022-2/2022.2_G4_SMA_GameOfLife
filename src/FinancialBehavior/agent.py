from mesa import Agent, Model


class MoneyAgent(Agent):
    def __init__(self, unique_id: int, model: Model) -> None:
        super().__init__(unique_id, model)
        self.money = 2

    def give_money(self) -> None:
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            other.money += 1
            self.money -= 1

    def move(self) -> None:
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self) -> None:
        self.move()
        if self.money > 0:
            self.give_money()
