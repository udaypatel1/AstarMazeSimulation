import random
from copy import deepcopy

"""
This class is for the Maze object which holds
the 2d array of blocked and unblocked values.
There are numerous methods to manipulate and
verify certain aspects of this Maze.
"""

class Maze:

    maxRow = 51
    maxCol = 51

    blockedProbability = 0.3 # 1
    unblockedProbability = 0.7 # 0

    maze = []

    flammability = 0

    """
    The __init__ method helps initialize the maze
    in its desired format with initial NoneType values.
    If a 2d array is already given, it will assign the maze
    as that 2d array.

    Args:
        arg1 (): None
        arg2 (int[][]): 2d array to convert into Maze Object

    Returns:
        None: None

    """
    def __init__(self, givenMaze=None):

        if givenMaze != None:
            self.maze = givenMaze

        else:
            self.maze = []
            for i in range(self.maxRow):
                rowEntry = []
                for j in range(self.maxCol):
                    rowEntry.append(None)
                self.maze.append(rowEntry)


    """
    The __str__ method simply prints out the maze
    in a desirable format to see in the terminal
    and disect different issues (or see the current
    state of the maze))

    Args:
        arg1 (): None

    Returns:
        String: 2d array but typecasted to a string

    """
    def __str__(self):
        f = ""
        for row in range(self.maxRow):
            f += str(self.maze[row]) + "\n"
        return f

    """
    Takes in a float value to assign as the current
    level of flammability for when the fire spreads

    Args:
        arg1 (float): non-negative float value for the
            current flammability
\
    Returns:
        None: None

    """
    def setFlammability(self, newFlammability):
        self.flammability = newFlammability

    """
    Returns the current 2d array stored in maze

    Args:
        arg1 (): None

    Returns:
        int[][]: 2d array of the object maze

    """
    def getMaze(self):
        return self.maze

    """
    Returns the maximum rows for the current maze

    Args:
        arg1 (): None

    Returns:
        int: non-negative value of maximum rows

    """
    def getMaxRow(self):
        return self.maxRow


    """
    Returns the maximum columns for the current maze

    Args:
        arg1 (): None

    Returns:
        int: non-negative value of maximum columns

    """
    def getMaxCol(self):
        return self.maxCol

    """
    This private method randomly populates a given maze with
    0s (unblocked cells) and 1s (blocked cells). This
    is done by probability (30% for blocked, 70% for 
    unblocked). It also calls another private method to
    ensure that both the corners and the center are 0,
    as per the instructions for a valid maze.

    Args:
        arg1 (): None

    Returns:
        None: None

    """
    def __randomBuild(self):

        for row in range(self.maxRow):
            for col in range(self.maxCol):

                probability = random.randint(1, 10)
                if probability <= 3:
                    self.maze[row][col] = 1
                else:
                    self.maze[row][col] = 0

        self.__unblockCenterAndCorners()

       # print("...Random Maze Build is Complete")

    """
    This particular private method builds an entire maze
    that is all 0 (used for search testing and other QA
    features).

    Args:
        arg1 (): None

    Returns:
        None: None

    """
    def __unblockedBuild(self):

        for row in range(self.maxRow):
            for col in range(self.maxCol):
                self.maze[row][col] = 0

    #    print("...Unblocked Maze Build is Complete")

    """
    This private instance method simply unblocks
    all of the corners and the center of the maze
    (changes them to 0 if it is 1).

    Args:
        arg1 (): None

    Returns:
        None: None

    """
    def __unblockCenterAndCorners(self):

        self.maze[self.maxRow // 2][self.maxCol // 2] = 0 # unblock the center
        self.maze[0][0] = 0 # unblock the top left
        self.maze[self.maxRow-1][0] = 0 # unblock the bottom left
        self.maze[0][self.maxCol-1] = 0 # unblock the top right
        self.maze[self.maxRow-1][self.maxCol-1] = 0 # unblock the bottom right

    """
    This private method does a DFS Tree Search to make sure
    that there is a free path from the center to each of the
    corners (as per the instructions).

    Args:
        arg1 (Tuple): (row, col) tuple of the particular
            corner of the maze.

    Returns:
        int: 0 if it is success
        int: -1 if it is a failure

    """
    def __centerToCornersCheck(self, goalTuple):

        start = (self.maxRow // 2, self.maxCol // 2)
        goal = goalTuple

        fringe = []
        fringe.append(start)

        explored = {}

        while len(fringe) != 0:

            current = fringe.pop()

            if current == goal:
     #           print("...Path is FOUND")
                return 0
            
            if explored.get(current) == None:
                explored[current] = True
            else:
                continue

            top = bottom = right = left = ()
            
            if current[0] + 1 < self.maxRow:
                top = (current[0] + 1, current[1])
            if current[0] - 1 >= 0:
                bottom = (current[0] - 1, current[1])
            if current[1] + 1 < self.maxCol:
                right = (current[0], current[1] + 1)
            if current[1] - 1 >= 0:
                left = (current[0], current[1] - 1)

            if top != ():
                if self.maze[top[0]][top[1]] != 1:
                    fringe.append(top)
                
            if bottom != ():
                if self.maze[bottom[0]][bottom[1]] != 1:
                    fringe.append(bottom)
                
            if left != ():
                if self.maze[left[0]][left[1]] != 1:
                    fringe.append(left)

            if right != ():
                if self.maze[right[0]][right[1]] != 1:
                    fringe.append(right)
        
        #print("...No Path")
        return -1           

    """
    This private method uses the centerToCorners check
    to ensure that each corner has a path to the center.
    If they are all valid (returning 0) or if one of them
    fails.

    Args:
        arg1 (): None

    Returns:
        int: 0 is successful
        int: -1 is unsuccessful

    """
    def __checkMaze(self):
        if self.__centerToCornersCheck((0, 0)) != 0:
      #      print("...Top Left Path Failed")
            return -1
        elif self.__centerToCornersCheck((0, self.maxCol-1)) != 0:
       #     print("...Top Right Path Failed")
            return -1
        elif self.__centerToCornersCheck((self.maxRow-1, 0)) != 0:
        #    print("...Bottom Left Path Failed")
            return -1
        elif self.__centerToCornersCheck((self.maxRow-1, self.maxCol-1)) != 0:
         #   print("...Bottom Right Path Failed")
            return -1
        else:
            return 0

    """
    This method uses the __checkMaze() method to ensure a
    valid maze is built. Otherwise, it will continuously
    build another random maze to check until a valid maze is
    found. The successful maze is then populated as the current
    2d array in the maze object.

    Args:
        arg1 (): None

    Returns:
        None: None

    """
    def generateValidMaze(self):

        self.__randomBuild()
        while self.__checkMaze() != 0:
            self.__randomBuild()
        
        #print("...Valid Maze is Complete")

        self.maze[self.maxRow // 2][self.maxCol // 2] = "F"

        return

    """
    This private method checks to see how many neighbors
    (up, down, left, right) are on fire (have "F"). This
    number will help in calculating the flammability
    probability for that particular cell.

    Args:
        arg1 (int): current row of the cell
        arg2 (int): current column of the cell

    Returns:
        int: the values that can be returned are
            0, 1, 2, 3, or 4

    """
    def __neighborsOnFire(self, curRow, curCol):

        if self.maze[curRow][curCol] == "F":
            return 0

        numOnFire = 0

        if curRow + 1 < self.maxRow:
            if self.maze[curRow + 1][curCol] == "F":
                numOnFire += 1

        if curRow - 1 >= 0:
            if self.maze[curRow - 1][curCol] == "F":
                numOnFire += 1
        
        if curCol + 1 < self.maxCol:
            if self.maze[curRow][curCol + 1] == "F":
                numOnFire += 1
        
        if curCol - 1 >= 0:
            if self.maze[curRow][curCol - 1] == "F":
                numOnFire += 1

        return numOnFire

    """
    This method actually advances the fire for the maze
    by one singular step. This is done by 1) creating a
    copy of the original maze, 2) populating that copy
    with fire probabilities for each cell that had a 0.
    This probability map was then realized with a random 
    number generator and the next step of F's (fires)
    is generated. This is then copied as the actual maze.

    Args:
        arg1 (): None

    Returns:
        None: None

    """
    def advanceFire(self):

        fireMap = deepcopy(self.maze)
        
        for row in range(self.maxRow):
            
            for col in range(self.maxCol):

                if self.maze[row][col] == "F":
                    fireMap[row][col] = "F"
                    continue
                elif self.maze[row][col] == 1:
                    continue

                numOnFire = self.__neighborsOnFire(row, col)
                probabilityOfFire = 1 - ((1 - self.flammability) ** numOnFire)

                fireMap[row][col] = probabilityOfFire
        # f = ""
        # for row in range(self.maxRow):
        #     f += str(fireMap[row]) + "\n"
        # print(f)

        for row in range(self.maxRow):
            for col in range(self.maxCol):
                if fireMap[row][col] == 0 or fireMap[row][col] == 1 or fireMap[row][col] == 'F':
                    continue
                else:
                    randomProb = random.random()
                    if fireMap[row][col] >= randomProb:
                        self.maze[row][col] = "F"

    """
    This private instance method calculates nearby fire cells
    for a given row and column in a maze (that is passed in).
    The reason this is formatted like such is to pass in a maze
    that is different from the original to avoid making changes on
    the current copy since this is a forecast.

    Args:
        arg1 (int[][]): 2d array of a maze
        arg2 (int): row of the maze
        arg3 (int): column of the maze

    Returns:
        int: possible values are 0, 1, 2, 3, or 4

    """
    def __neighborsFireFuture(self, maze, curRow, curCol):

        if maze[curRow][curCol] == "F":
            return 0

        numOnFire = 0

        if curRow + 1 < self.maxRow:
            if maze[curRow + 1][curCol] == "F":
                numOnFire += 1

        if curRow - 1 >= 0:
            if maze[curRow - 1][curCol] == "F":
                numOnFire += 1
    
        if curCol + 1 < self.maxCol:
            if maze[curRow][curCol + 1] == "F":
                numOnFire += 1
        
        if curCol - 1 >= 0:
            if maze[curRow][curCol - 1] == "F":
                numOnFire += 1

        return numOnFire

    """
    This method advances the fire various steps in the future given
    by the parameter. This future prediction is not
    copied to the original maze but returned as a separate
    entity. The probability logic remains the same.

    Args:
        arg1 (int): non-negative integer value of the number of
            steps to predict for a given maze

    Returns:
        int[][]: a 2d array of the predicted maze
            (non Maze object at this point)

    """
    def advanceFireFuture(self, futureSteps):

        mazeCopy = deepcopy(self.maze)

        for i in range(futureSteps):

            fireMap = deepcopy(mazeCopy)

            for row in range(self.maxRow):
                
                for col in range(self.maxCol):

                    if mazeCopy[row][col] == "F":
                        fireMap[row][col] = "F"
                        continue
                    elif mazeCopy[row][col] == 1:
                        continue

                    numOnFire = self.__neighborsFireFuture(mazeCopy, row, col)

                    probabilityOfFire = 1 - ((1 - self.flammability) ** numOnFire)
                    

                    fireMap[row][col] = probabilityOfFire
            # f = ""
            # for row in range(self.maxRow):
            #     f += str(fireMap[row]) + "\n"
            # print(f)

            for row in range(self.maxRow):
                for col in range(self.maxCol):
                    if fireMap[row][col] == 0 or fireMap[row][col] == 1 or fireMap[row][col] == 'F':
                        continue
                    else:
                        randomProb = random.random()
                        if fireMap[row][col] >= randomProb:
                            mazeCopy[row][col] = "F"

        return mazeCopy

       
                    
# m = Maze()
# m.generateValidMaze()
# print(m)

# future = m.advanceFireFuture(8)

# f = ""
# for row in range(m.getMaxRow()):
#     f += str(future[row]) + "\n"
# print(f)
