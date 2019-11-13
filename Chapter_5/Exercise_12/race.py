
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



'''
vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
              "potato", "wheat", "barley"]
farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])


fig, ax = plt.subplots()





im = ax.imshow(harvest)

# We want to show all ticks...
ax.set_xticks(np.arange(len(farmers)))
ax.set_yticks(np.arange(len(vegetables)))
# ... and label them with the respective list entries
ax.set_xticklabels(farmers)
ax.set_yticklabels(vegetables)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Harvest of local farmers (in tons/year)")
fig.tight_layout()
plt.show()

'''


