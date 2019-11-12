
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
        print("Gamma: ", self.gamma)

        self.actions = [[] for i in range(9)]
        for i in range(3):
            for j in range(3):
                self.actions[(i*3)+j] = [i-1,j-1]  
        print("Actions: \n", self.actions)

        self.policy = [[] for i in range(len(self.env.states))]
        for i in range(len(self.env.states)):
            self.policy[i] = [self.env.states[i], random.choice(self.actions)]
        
        self.qfunc = [[] for i in range(len(self.env.states)*len(self.actions))]
        for i in range(len(self.env.states)):
            for j in range(len(self.actions)):
                self.qfunc[(i*len(self.actions)) + j] = [self.env.states[i]+self.actions[j], 0]

        self.returns = [[] for i in range(len(self.env.states)*len(self.actions))]
        for i in range(len(self.env.states)):
            for j in range(len(self.actions)):
                self.returns[(i*len(self.actions)) + j] = [self.env.states[i]+self.actions[j]]

        #self.returns[0].append(5)


        


agent()