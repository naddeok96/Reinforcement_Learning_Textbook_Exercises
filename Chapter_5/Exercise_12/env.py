'''
This will build the enviroment of the racetrack
'''
import numpy as np
import random

class RaceTrack():

    def __init__(self):
        super(RaceTrack, self).__init__()

        print("==========================")
        starting_states = [[] for i in range(6)]
        for i in range(6):
            starting_states[i] = [31, i+3]
        print("Starting States: \n",starting_states)

        terminal_states = [[] for i in range(6)]
        for i in range(6):
            terminal_states[i] = [i, 16]
        print("Terminal States: \n",terminal_states)

        states = [[] for i in range((17*32))]
        for i in range(17):
            for j in range(32):
                states[(i*32) + j] = [j,i]
        print("States: \n",states)

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
        print("Bounds: ", bounds)

        for state in bounds: states.remove(state)

        print("==========================")

    def step(self, state, action, velocity):
        print("==========================")
        print("Inital State: ", state)
        print("Intial Velocity:  ", velocity)
        print("Action ", action)
        print("--------------------------")

        velocity = velocity + action
        state = state + velocity

        if state not in states:
            state = random.choice(starting_states)
            velocity = [0,0]

        if state in terminal_states:
            terminate = True

        print("Final State: ", state)
        print("Final Velocity: ", velocity)
        print("==========================")

        return state, velocity, terminate



race = RaceTrack()

state = [0,0]
action = [2,3]
velocity = [0,0]

race.step(state,action,velocity)
