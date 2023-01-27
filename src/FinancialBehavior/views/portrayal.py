from src.FinancialBehavior.agent import MoneyAgent

def agent_portrayal(agent: MoneyAgent):
    portrayal = {
        "Shape": "circle",
        "Filled": "true",
    }

    if agent.money >= 3:
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.8
    
    elif agent.money > 0:
        portrayal["Color"] = "green"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.6
    
    else:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 2
        portrayal["r"] = 0.4
    
    return portrayal
