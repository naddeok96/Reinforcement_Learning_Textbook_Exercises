'''
This will build the enviroment of the racetrack
'''
import numpy as np
import random

class RaceTrack():

    def __init__(self):

        super(RaceTrack, self).__init__()

        print("===============================================================================")
        # Initalize possible starting states
        self.starting_states = [[] for i in range(6)]
        for i in range(6):
            self.starting_states[i] = [31, i+3]
        print("Starting States: \n",self.starting_states)

        # Initalize terminal states
        self.terminal_states = [[] for i in range(6*4)]
        for i in range(6):
            for j in range(4)
                self.terminal_states[(i*4) + j] = [i, 16 + j]
        print("Terminal States: \n",self.terminal_states)

        # Generate a set representing a square grid 32x17
        self.states = [[] for i in range((32*17))]
        for i in range(17):
            for j in range(32):
                self.states[(i*32) + j] = [j,i]
        #print("States: \n",self.states)

        # Make sets of locations not in possible states
        bound1 = [[] for i in range(4)]
        for i in range(4):
            bound1[i] = [i,0]

        bound2 = [[] for i in range(18)]
        for i in range(18):
            bound2[i] = [i + 14,0]

        bound3 = [[] for i in range(3)]
        for i in range(3):
            bound3[i] = [i,1]

        bound4 = [[] for i in range(10)]
        for i in range(10):
            bound4[i] = [i + 22,1]

        bound5 = [[0,2]]

        bound6 = [[] for i in range(3)]
        for i in range(3):
            bound6[i] = [i + 29,2]

        bound7 = [[] for i in range(25)]
        for i in range(25):
            bound7[i] = [i + 7,9]

        bound8 = [[] for i in range(182)]
        for i in range(26):#rows
            for j in range(7):#cols
                bound8[(i*7) + j] = [i + 6, j +10]

        bounds = bound1 + bound2 + bound3 + bound4 + bound5 + bound6 + bound7 + bound8
        #print("Bounds: \n", bounds)

        # Remove states in the square grid that are out of bounds
        for state in bounds: self.states.remove(state)

        print("===============================================================================\n\n")

    def step(self, state, action, velocity):
        '''
        Given the current state, chosen action and current velocity
        this function will compute the next state, velocity and whether 
        the episode reached its terminal state
        '''

        print("==========================")
        print("Inital State: ", state)
        print("Intial Velocity:  ", velocity)
        print("Action ", action)
        print("--------------------------")

        # Compute new velocity given action
        intial_velocity = self.velocity
        velocity = list(np.asarray(velocity) + np.asarray(action))
        self.fix_velocity(velocity, intial_velocity)

        # The way the gridworld is set up a negative velocity is needed to move forward
        #  so this just flips the sign of the vertical velocity for calculating next state
        mirror_effect = [-1*velocity[0], velocity[1]]

        # Calculate new state
        state = list(np.asarray(state) + mirror_effect)

        # Determine if the new state is out of bounds
        if state not in self.states:
            state = random.choice(self.starting_states)
            velocity = [0,0]

        # Determine if episode is over
        terminate = False
        if state in self.terminal_states:
            terminate = True

        print("Final State: ", state)
        print("Final Velocity: ", velocity)
        print("Episode Terminated: ", terminate)
        print("==========================")

        return state, velocity, terminate

    def fix_velocity(self,velocity, intial_velocity):
        '''
        This function will limit the velocity to its max and min value and 
        prevent the car from coming to a stop at any point
        '''

        if velocity[0] > 3:
            velocity[0] = 3
        if velocity[0] < -3:
            velocity[0] = -3
        if velocity[1] > 3:
            velocity[1] = 3
        if velocity[1] < -3:
            velocity[1] = -3
        if velocity == [0,0]
            velocity = intial_velocity

        return velocity
        

