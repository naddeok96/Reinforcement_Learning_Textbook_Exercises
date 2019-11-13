
'''
This will have an agent race until the agent reaches an optimal policy
'''

# Imports
from env import RaceTrack
from agent import agent
from silence import shh
import matplotlib.pyplot as plt
import numpy as np

# Initalize
with shh():
    env = RaceTrack()
    racer = agent()

# Race
n_episodes = 100000
for i in range(n_episodes):
    with shh():
        racer.episode()

# Plot
fig, ax = plt.subplots()

plt.axes([-3, -3, 3, 0.5])

track_values = np.zeros((32,17))

for state in racer.env.states:
    action = racer.policy[str(state)]
    value = racer.qfunc[str(state+action)]
    track_values[state[0],state[1]] = value
    ax.text(state[1],state[0], str(action), ha="center", va="center", color="k")

im = ax.imshow(track_values)

ax.set_title("Action Value Heat Map")
ax.set_aspect(aspect=0.4)
plt.grid(True)


plt.show()



