'''
This will build the enviroment of the racetrack
'''
import numpy as np
import random

class RaceTrack():

    def __init__(self):
        super(RaceTrack, self).__init__()

        print("===============================================================================")
        self.starting_states = [[] for i in range(6)]
        for i in range(6):
            self.starting_states[i] = [31, i+3]
        print("Starting States: \n",self.starting_states)

        self.terminal_states = [[] for i in range(6)]
        for i in range(6):
            self.terminal_states[i] = [i, 16]
        print("Terminal States: \n",self.terminal_states)

        self.states = [[] for i in range((17*32))]
        for i in range(17):
            for j in range(32):
                self.states[(i*32) + j] = [j,i]
        print("States: \n",self.states)

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
        print("Bounds: \n", bounds)

        for state in bounds: self.states.remove(state)

        print("===============================================================================\n\n")

    def step(self, state, action, velocity):
        print("==========================")
        print("Inital State: ", state)
        print("Intial Velocity:  ", velocity)
        print("Action ", action)
        print("--------------------------")

        velocity = list(np.asarray(velocity) + np.asarray(action))

        mirror_effect = [-1*velocity[0], velocity[1]]


        state = list(np.asarray(state) + mirror_effect)

        if state not in self.states:
            state = random.choice(self.starting_states)
            velocity = [0,0]

        terminate = False
        if state in self.terminal_states:
            terminate = True

        print("Final State: ", state)
        print("Final Velocity: ", velocity)
        print("Episode Terminated: ", terminate)
        print("==========================")

        return state, velocity, terminate



race = RaceTrack()

state = [31, 7]
action = [3,-3]
velocity = [0,0]

race.step(state,action,velocity)
