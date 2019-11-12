
'''
This will be the agents mind
'''
# Imports
from env import RaceTrack
import random
import numpy as np

class agent():

    def __init__(self):

        super(agent, self).__init__()

        # Initalize enviroment
        self.env = RaceTrack()

        # Start at zero velocity
        self.velocity = [0,0]

        # Set discount rate
        self.gamma = 1
        print("Gamma: ", self.gamma)

        # Initalize set of actions for the agent to take
        self.actions = [[] for i in range(9)]
        for i in range(3):
            for j in range(3):
                self.actions[(i*3)+j] = [i-1,j-1]  
        print("Actions: \n", self.actions)

        # Initalize an arbitrary policy
        self.policy = [[] for i in range(len(self.env.states))]
        for i in range(len(self.env.states)):
            self.policy[i] = [self.env.states[i], random.choice(self.actions)]
        
        # Initalize an arbitrary Q-Function
        self.qfunc = [[] for i in range(len(self.env.states)*len(self.actions))]
        for i in range(len(self.env.states)):
            for j in range(len(self.actions)):
                self.qfunc[(i*len(self.actions)) + j] = [self.env.states[i]+self.actions[j], 0]

        # Initalize a returns table
        self.returns = [[] for i in range(len(self.env.states)*len(self.actions))]
        for i in range(len(self.env.states)):
            for j in range(len(self.actions)):
                self.returns[(i*len(self.actions)) + j] = [self.env.states[i]+self.actions[j]]

        #self.returns[0].append(5)


    def episode(self):
        '''
        This function will run an episode and update the policy and Q-function
        '''

        # Choose a random starting state 
        state = random.choice(self.env.starting_states)

        # Reset velocity to zero
        self.velocity = [0,0]

        # Reset the termination indicator to false
        terminate = False

        # Run episode until termination
        #while terminate = False:
    
    def getAction(self, state):
    
    def setAction(self, state):

    def getValue(self, state, action):

    def setValue(self, state, action):

    def getReturns(self, state, action):

    def setReturns(self, state, action):
        


agent()