
'''
This will be the agents mind
'''

from env import RaceTrack
import random
import numpy as np

class agent():

    def __init__(self):

        super(agent, self).__init__()

        self.env = RaceTrack()

        self.velocity = [0,0]
        self.rewards = 0
        self.gamma = 0.9
        self.state = random.choice(self.env.starting_states)        
