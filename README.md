# Reinforcement Learning Textbook Exercises

## Table of Contents
> Chapter 5
- [Race Track](#racetrack)

---

## Chapter 5 

### Race Track
The goal of this exercise is to train an agent with any Monte-Carlo method to perform the fast right turn possible on the track below:

![image](https://user-images.githubusercontent.com/48805713/68787892-33a90f80-05f7-11ea-84e7-6fdfb5d7f0e5.png)

This track was built in the env.py file which builds a class containing the track and transitions.

The MC method used will be Exploring States

![image](https://user-images.githubusercontent.com/48805713/68788016-69e68f00-05f7-11ea-8a36-89a70ec392ab.png)

The agent will uses this algorithm to update its policy. 

The race.py file will perform episodes untill the policy convegerges, below shows the policy printed on each state and a heatmap of the value of each state action pair.

![image](https://user-images.githubusercontent.com/48805713/68788342-0c9f0d80-05f8-11ea-9906-0a3f7c36a88f.png)
