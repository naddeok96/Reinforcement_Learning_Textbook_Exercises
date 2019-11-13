
'''
This will have an agent race until the agent reaches an optimal policy
'''

# Imports
from agent import agent
from silence import shh
import matplotlib.pyplot as plt
import numpy as np
import copy

# Initalize agent and enviroment
racer = agent()

# Race for n number of episodes
N_EPISODES = 200
LOG_EVERY_N = 1e5
converged = False
converged_counter = 0
initial_converged = False
streak = []
episode = 0
#for i in range(N_EPISODES):
while converged_counter < 1e5 and episode < 1e7:
    episode += 1
    old_policy = copy.copy(racer.policy)
    
    with shh(): # shh() suppresses print outs from calls
        racer.episode()
    
    initial_converged = converged
    converged = (racer.policy == old_policy)

    if converged == initial_converged and converged == True:
        converged_counter += 1

    if converged_counter > 0 and converged != initial_converged:
        converged_counter = 0

    if episode % LOG_EVERY_N == 0:
        print("--------------------------------")
        print("Episode:")
        print(episode)
        print("Converged counter:")
        print(converged_counter)
        print("--------------------------------\n")

print("Converged:")
print(converged)

# Plot
fig, ax = plt.subplots()

track_values = np.zeros((32,17))
for state in racer.env.states:
    action = racer.policy[str(state)]
    value = racer.qfunc[str(state+action)]
    track_values[state[0],state[1]] = value
    ax.text(state[1],state[0], str(action), ha="center", va="center", color="k")

im = ax.imshow(track_values)
ax.set_title("Action Value Heat Map and Policy Table")
ax.set_aspect(aspect=0.4)
ax.set_xticks(np.arange(0, 17, 1))
ax.set_yticks(np.arange(0, 32, 1))
ax.set_xticks(np.arange(-1.5, 18.5, 1), minor=True)
ax.set_yticks(np.arange(-1.5, 33.5, 1), minor=True)
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
plt.show()

