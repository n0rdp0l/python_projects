import random
import matplotlib.pyplot as plt
import numpy as np

# constants for the game
NUM_ROCKS = 50
NUM_PAPERS = 50
NUM_SCISSORS = 50

# initialize the environment and agents
environment = [[0.0 for i in range(101)] for j in range(101)]
rocks = [(np.random.randn(0,99).astype('float32'), np.random.randn(0,99).astype('float32')) for i in range(NUM_ROCKS)]
papers = [(np.random.randn(0,99).astype('float32'), np.random.randn(0,99).astype('float32')) for i in range(NUM_PAPERS)]
scissors = [(np.random.randn(0,99).astype('float32'), np.random.randn(0,99).astype('float32')) for i in range(NUM_SCISSORS)]

# initialize the plot
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# simulate the game
while len(rocks) > 0 and len(papers) > 0 and len(scissors) > 0:
  # move the agents
  for i in range(len(rocks)):
    rocks[i] = (rocks[i][0] + np.random.randn(-1,1).astype('float32'), rocks[i][1] + np.random.randn(-1,1).astype('float32'))
  for i in range(len(papers)):
    papers[i] = (papers[i][0] + np.random.randn(-1,1).astype('float32'), papers[i][1] + np.random.randn(-1,1).astype('float32'))
  for i in range(len(scissors)):
    scissors[i] = (scissors[i][0] + np.random.randn(-1,1).astype('float32'), scissors[i][1] + np.random.randn(-1,1).astype('float32'))

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
    environment[rock[0]][rock[1]] = "R"
  for paper in papers:
    environment[paper[0]][paper[1]] = "P"
  for scissors in scissors:
    environment[scissors[0]][scissors[1]] = "S"

  # plot the environment
  ax.clear()
  ax.imshow(environment, cmap="viridis")
  plt.pause(0.1)

# print the final state of the environment
for row in environment:
  print(" ".join(row))

# keep the plot open until the user closes it
plt.show(block=True)
