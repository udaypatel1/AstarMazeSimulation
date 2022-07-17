"""
This file runs the first strategy (agent 1). for each of the flammabilites we
test the program will find the shortest path and execute it while advancing the 
fire after each time step. 

Outputs:
    (current flammability, Trial number for the given flammability, Success/fire hit/ no path)
    List of the Flammabilility values
    List of the Success rate for the given flammability
"""

from Maze import Maze
from Agent import Agent
from SearchAlgo import SearchAlgo
import matplotlib.pyplot as plt

searchAlgo = SearchAlgo()
maze = Maze()

curFlammability = 0
maze.setFlammability(curFlammability)

agent = Agent(0, 0)

trials = 100

flameNum = []
trialResults = []

for flame in range(11):

    flameNum.append(curFlammability)
    numSuccess = 0
    numFailure = 0

    for i in range(trials):

        agent.reset()
        
        maze.generateValidMaze()
        maze.setFlammability(curFlammability)
        path = searchAlgo.Astar(maze, agent)

        while (agent.getRow(), agent.getCol()) != (maze.getMaxRow()-1, maze.getMaxCol()-1):

            agentOriginal = (agent.getRow(), agent.getCol())
            
            agent.setRow(path[agentOriginal][0])
            agent.setCol(path[agentOriginal][1])

            maze.advanceFire()

            if (agent.getRow(), agent.getCol()) == (maze.getMaxRow()-1, maze.getMaxCol()-1):
                print(curFlammability, i,"SUCCESS")
                numSuccess += 1
                break
            
            if maze.getMaze()[agent.getRow()][agent.getCol()] == "F":
                print(curFlammability, i, "FIRE HIT")
                numFailure += 1
                break

    trialResults.append(float(numSuccess) / float(trials))
    curFlammability += 0.05

#print(trialResults)

print("Flammability = " , flameNum)
print("Trial results = " , trialResults)
print("Agent 1 Simulation Complete")
fig = plt.figure(figsize= (10, 5))

plt.bar(flameNum,trialResults, width=.05)
plt.xticks([0, .05, .1, .15, .2, .25, .3, .35, .4, .45, .5])
plt.xlabel("Flammability (q)")
plt.ylabel("Success Rate After 100 Trials Each")
plt.title("Agent 1 Graph Simulation")
plt.show()

