from mesa import Model
from mesa.time import RandomActivation
from agents import Wagent

class WageModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        # create agents
        for i in range(self.num_agents):
            a = Wagent(i, self)
            self.schedule.add(a)

    def step(self):
        """Advances models by one step."""
        self.schedule.step()


