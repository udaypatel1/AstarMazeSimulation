
"""
This particular class is the Agent object which holds the current
row and current column in a particular maze
"""
class Agent:

    """
    The __init__ method helps initialize the currentRow
    and currentColumn to the values given in the parameter

    Args:
        Parameters are currentRow (int) and currentColumn (int)

    Returns:
        None: None

    """
    def __init__(self, currentRow, currentCol):
        self.currentRow = currentRow
        self.currentCol = currentCol
    
    """
    This method resets the Agent location to (0, 0)

    Args:
        arg1 (): None

    Returns:
        None: None

    """
    def reset(self):
        self.currentRow = 0
        self.currentCol = 0
    
    """
    Gets the currentRow of the Agent

    Args:
        arg1 (): None

    Returns:
        None: None

    """
    def getRow(self):
        return self.currentRow
    
    """
    Gets the currentCol of the Agent

    Args:
        arg1 (): None

    Returns:
        None: None

    """
    def getCol(self):
        return self.currentCol

    """
    Sets the currentRow of the Agent

    Args:
        arg1 (int): value of new row

    Returns:
        int: value of the new row

    """
    def setRow(self, newRow):
        self.currentRow = newRow
    
    """
    Sets the currentCol of the Agent

    Args:
        arg1 (int): value of new col

    Returns:
        int: value of the new col

    """
    def setCol(self, newCol):
        self.currentCol = newCol