from mesa import Agent

"""

"""

class Wagent(Agent):
    """Agent for wage simulation, represents a single economic actor"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.bag = [] # start with nothing

    def step(self):
        pass
