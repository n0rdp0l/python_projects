import random
import matplotlib.pyplot as plt
import numpy as np

# constants for the game
NUM_ROCKS = 50
NUM_PAPERS = 50
NUM_SCISSORS = 50

# initialize the environment and agents
environment = [[0.0 for i in range(101)] for j in range(101)]
rocks = [(np.random.randint(0,100), np.random.randint(0,100)) for i in range(NUM_ROCKS)]
papers = [(np.random.randint(0,100), np.random.randint(0,100)) for i in range(NUM_PAPERS)]
scissors = [(np.random.randint(0,100), np.random.randint(0,100)) for i in range(NUM_SCISSORS)]

# initialize the plot
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# simulate the game
while len(rocks) > 0 and len(papers) > 0 and len(scissors) > 0:
  # move the agents
  for i in range(len(rocks)):
    rocks[i] = (rocks[i][0] + np.random.randn(), rocks[i][1] + np.random.randn())
  for i in range(len(papers)):
    papers[i] = (papers[i][0] + np.random.randn(), papers[i][1] + np.random.randn())
  for i in range(len(scissors)):
    scissors[i] = (scissors[i][0] + np.random.randn(), scissors[i][1] + np.random.randn())

  # check for collisions
  for rock in rocks:
    for paper in papers:
      if rock == paper:
        papers.remove(paper)
    for scissor in scissors:
      if rock == scissor:
        scissors.remove(scissor)
  for paper in papers:
    for scissor in scissors:
      if paper == scissor:
        scissors.remove(scissor)

  # update the environment
  environment = [[0.0 for i in range(101)] for j in range(101)]
  for rock in rocks:
    environment[int(rock[0])][int(rock[1])] = "R"
  for paper in papers:
    environment[int(paper[0])][int(paper[1])] = "P"
  for scissors in scissors:
    environment[int(scissors[0])][int(scissors[1])] = "S"

  # plot the environment
  ax.clear()
  ax.imshow(environment, cmap="viridis")
  plt.pause(0.1)

# print the final state of the environment
for row in environment:
  print(" ".join(str(x) for x in row))

# keep the plot open until the user closes it
plt.show(block=True)
