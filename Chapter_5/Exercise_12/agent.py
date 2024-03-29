
'''
This will be the agents mind
'''
# Imports
from env import RaceTrack
import random
import numpy as np
from statistics import mean
import itertools
from silence import shh


class agent():

    def __init__(self):

        super(agent, self).__init__()

        # Initalize enviroment
        self.env = RaceTrack()

        # Initalize set of actions for the agent to take
        self.actions = [[] for i in range(9)]
        for i in range(3):
            for j in range(3):
                self.actions[(i*3)+j] = [i-1,j-1]  

        print("Agents Hyperparameters: ")
        print("==========================")
        print("Actions: \n", self.actions)

        # Set discount rate
        self.GAMMA = 0.9
        print("Gamma: \n", self.GAMMA)
        print("==========================\n")

        # Initalize an arbitrary policy
        self.policy = {}
        for i in range(len(self.env.states)):
            self.policy[str(self.env.states[i])] = random.choice(self.actions)
        
        # Initalize an arbitrary Q-Function
        self.qfunc = {}
        for i in range(len(self.env.states)):
            for j in range(len(self.actions)):
                self.qfunc[str(self.env.states[i]+self.actions[j])] = 0

        # Initalize a returns table
        self.returns = {}
        for i in range(len(self.env.states)):
            for j in range(len(self.actions)):
                self.returns[str(self.env.states[i]+self.actions[j])] = []

        # Initalize episode counter
        self.n_episodes = 0

    def episode(self):
        '''
        This function will run an episode and update the policy and Q-function
        '''

        # Choose a random starting state 
        state = random.choice(self.env.starting_states)
        
        # Reset velocity to zero
        velocity = [0,0]

        # Reset the termination indicator to false
        terminate = False

        # Initalize the history
        history = []

        # Update episode counter
        self.n_episodes += 1

        # Reset returns
        self.returns = {}
        for i in range(len(self.env.states)):
            for j in range(len(self.actions)):
                self.returns[str(self.env.states[i]+self.actions[j])] = []
        G = 0

        print("Episode",self.n_episodes, "Summary")
        print("====================================================")

        # Run episode until termination
        iteration = 0
        #for i in range(100): 
        while terminate == False and iteration < 100:

            # Update Iteration
            iteration += 1

            # Compute action given state
            action = self.policy[str(state)]

            # Compute Current Returns
            G = G + (self.GAMMA**i)*-1

            # Store current state action pair pair
            self.returns[str(state + action)].append(G)

            # Store history
            history.append([state + action])
            
            # Take one step
            with shh(): # shh() suppresses print outs from calls
                state, velocity, terminate = self.env.step(state, action, velocity)

        #print("History: ")
        #print(history)
        #print("--------------------------------")

        # Find Unique History        
        history.sort()
        unique_history = list(history for history,_ in itertools.groupby(history))
        print("Unique States Visited: ")
        print(unique_history)
        print("--------------------------------")
        
        # Update state-action value for each state visited
        for state_action in unique_history:
            self.qfunc[str(state_action[0])] = mean(self.returns[str(state_action[0])])
            
        # Update the policy for states visited
        print("Policy Updates:")
        for i in range(len(unique_history)):
            state = unique_history[i][0][0:2]

            print('--------------------------------')
            print("State:", state)
            qvalues = []
            for action in self.actions:
                qvalues.append(self.qfunc[str(state+action)])
            
            print("Old Policy:",self.policy[str(state)])
            # Update policy for state
            self.policy[str(state)] = self.actions[np.argmax(qvalues)]
            print("New Policy", self.policy[str(state)])
        

        print("====================================================\n")
        

