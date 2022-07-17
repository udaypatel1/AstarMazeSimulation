from copy import deepcopy

"""
This class holds the algorithm(s) to search within a maze along
with its supporting instance methods
"""

class SearchAlgo:

    def __init__(self):
        pass

    """
    The function below is the Heuristic for the A* algorithm 
    We used manhattan distance for our heurisitc 

    Args:
        passing through the self instance , maze , and the 
        row and column of the node
    Returns:
        None: H(n)
    """
    def heuristic(self, maze , curr_row, curr_col):

        goal_row = maze.getMaxRow() - 1
        goal_col = maze.getMaxCol() - 1
        #Use Manhattan distance for H(n)
        
        return abs(goal_row - curr_row) + abs(goal_col - curr_col)

    """
    This is the main instance method in this class which runs the 
    A* search algorithm to find the shortest path from the Agent
    (wherever he/she/they/it is on the maze) to the bottom rightmost
    cell in the maze.

    Args:
        Takes in a maze object and an agent (current row, col) position in that
        particular maze

    Returns:
        Shortest path 
    """
    def Astar(self, maze, agent):

        #F(n) = G(n) + H(n)
        priorityQueue = {}
        closed_set = {}
        prev = {}
        path = {}
        gVals = {}
        initial_state = (agent.getRow() , agent.getCol())
        goal_state = (maze.getMaxRow() - 1 , maze.getMaxCol() - 1)
        
        priorityQueue[initial_state] = 0 + self.heuristic(maze, initial_state[0], initial_state[1])

        gVals[initial_state] = 0

        temp = 0        
        while priorityQueue:
            temp+=1
            #current_state = priorityQueue[initial_state]
            current_state = min(priorityQueue, key=priorityQueue.get)

            #pop the value out so it doesnt run into a infinite loop

            priorityQueue.pop(current_state)
            #Get the min value cost from the priority queue
            #need to change the above line
            closed_set[current_state] = True
            
            #print(priorityQueue)
            if(current_state == goal_state):
                #print("WHILE LOOP RUNS... " , temp)
                value = ()
                key = goal_state
                while True:
                    
                    value = prev[key]
                    #print("value" , value)
                    #print("key" , key)

                    path[value] = key
                    
                    if(value == initial_state):
                        return path
                    
                    key = value

            # I think the rest of this should be similar to the code for BFS but need to find the cost
            # of the total path   

            top = bottom = right = left = ()
            
            if (current_state[0] + 1 < maze.getMaxRow()):
                bottom = (current_state[0] + 1, current_state[1])

                if (maze.getMaze()[bottom[0]][bottom[1]] != 1 and maze.getMaze()[bottom[0]][bottom[1]] != 'F'):
                    
                    if(bottom not in closed_set and bottom not in priorityQueue):

                        gn = gVals[current_state] + 1
                        hn = self.heuristic(maze, bottom[0], bottom[1])
                        fn = gn + hn

                        priorityQueue[bottom] = fn
                        gVals[bottom] = gn 
                        prev[bottom] = current_state
                        

            if (current_state[0] - 1 >= 0):
                top = (current_state[0] - 1, current_state[1])

                if (maze.getMaze()[top[0]][top[1]] != 1 and maze.getMaze()[top[0]][top[1]] != 'F'):
                    
                    if(top not in closed_set and top not in priorityQueue):

                        gn = gVals[current_state] + 1
                        hn = self.heuristic(maze, top[0], top[1])
                        fn = gn + hn
                        
                        priorityQueue[top] = fn
                        gVals[top] = gn 
                        prev[top] = current_state
                        

            if (current_state[1] + 1 < maze.getMaxRow()):
                right = (current_state[0], current_state[1] + 1)

                if (maze.getMaze()[right[0]][right[1]] != 1 and maze.getMaze()[right[0]][right[1]] != 'F'):

                    if(right not in closed_set and right not in priorityQueue): 

                        gn = gVals[current_state] + 1
                        hn = self.heuristic(maze, right[0], right[1])
                        fn = gn + hn
                        
                        priorityQueue[right] = fn
                        gVals[right] = gn 
                        prev[right] = current_state
                        

            if (current_state[1] - 1 >= 0):
                left = (current_state[0], current_state[1] - 1)

                if (maze.getMaze()[left[0]][left[1]] != 1 and maze.getMaze()[left[0]][left[1]] != 'F'):

                    if(left not in closed_set and left not in priorityQueue):    
                        gn = gVals[current_state] + 1
                        hn = self.heuristic(maze, left[0], left[1])
                        fn = gn + hn
                        
                        priorityQueue[left] = fn
                        gVals[left] = gn 
                        prev[left] = current_state
            
        return {}