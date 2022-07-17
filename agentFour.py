"""
This file runs the free strategy (agent 4). for each of the flammabilites we
test the program will find the shortest path and execute it while advancing the 
fire after each time step. We check 3 steps into the future on the simulated reality,
and if that path doesnt exist 2 in the future and so on. The we run the program for THREE
time steps without recalculating the future prediction. 

** The goal of this is to create a much faster executing version of agent 3 while trying to 
minimize the decrease in success rate and intelligence**

Outputs:
    (current flammability, Trial number for the given flammability, Success/fire hit/ no path)
    List of the Flammabilility values
    List of the Success rate for the given flammability
"""

from locale import currency
from re import search
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
        
        futureMaze = maze.advanceFireFuture(3)
        futureMazeObj = Maze(futureMaze)
        futureMazeObj.setFlammability(curFlammability)
        futurePath = searchAlgo.Astar(futureMazeObj, agent) 

        if futurePath == {}:
            path = searchAlgo.Astar(maze, agent)
        else:
            path = futurePath
        futureCheck = 0

        
        while (agent.getRow(), agent.getCol()) != (maze.getMaxRow()-1, maze.getMaxCol()-1):
            
            futureCheck +=1
            agentOriginal = (agent.getRow(), agent.getCol())
            
            agent.setRow(path[agentOriginal][0])
            agent.setCol(path[agentOriginal][1])

            maze.advanceFire()

            if (agent.getRow(), agent.getCol()) == (maze.getMaxRow()-1, maze.getMaxCol()-1):
                print(curFlammability,i, "SUCCESS")
                numSuccess += 1
                break

            if futureCheck == 3:
                futureCheck = 0
                if maze.getMaze()[agent.getRow()][agent.getCol()] == "F":
                    print(curFlammability,i , "FIRE HIT")
                    numFailure += 1
                    break
                
                futureMaze = maze.advanceFireFuture(3)
                futureMazeObj = Maze(futureMaze)
                futureMazeObj.setFlammability(curFlammability)
                futurePath = searchAlgo.Astar(futureMazeObj, agent) 

                if futurePath == {}:
                    #print("Fail on 3")
                    futureMaze = maze.advanceFireFuture(2)
                    futureMazeObj = Maze(futureMaze)
                    futureMazeObj.setFlammability(curFlammability)
                    futurePath = searchAlgo.Astar(futureMazeObj, agent)

                    if futurePath == {}:
                        #print("fail on 2")
                        futureMaze = maze.advanceFireFuture(1)
                        futureMazeObj = Maze(futureMaze)
                        futureMazeObj.setFlammability(curFlammability)
                        futurePath = searchAlgo.Astar(futureMazeObj, agent)

                        if futurePath == {}:
                            path = searchAlgo.Astar(maze, agent)

                            if path == {}:
                                print(curFlammability , i, "NO PATH FOUND")
                                numFailure += 1
                                break
                        else:
                            path = futurePath
                            #print("Success on 1")
                    else:
                        path = futurePath
                        #print("Success on 2")
                else:
                    path = futurePath
                    #print("Success on 3")

    trialResults.append(float(numSuccess) / float(trials))
    curFlammability += 0.05

print("Flammability = " , flameNum)
print("Trial results = " , trialResults)

print("Agent 4 Simulation Complete")
fig = plt.figure(figsize= (10, 5))

plt.bar(flameNum,trialResults, width=.05)
plt.xticks([0, .05, .1, .15, .2, .25, .3, .35, .4, .45, .5])
plt.xlabel("Flammability (q)")
plt.ylabel("Success Rate After 100 Trials Each")
plt.title("Agent 4 Graph Simulation")
plt.show()