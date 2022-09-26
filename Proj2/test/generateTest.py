import numpy as np
import copy
import math


### Generate test object
class GenerateTest():
    
    # Constructor
    def __init__(self, dimension:int=10, isDirectional:bool=True) -> None:
        # init values
        self.dimension = dimension
        self.isDirectional = isDirectional
        self.adjMatrix = np.random.randint(0,2, (self.dimension, self.dimension)).tolist()
        
        # house keeping for non-directional graphs

        
        # number of vertecies and housekeeping for non-directional graphs
        self.edges = 0
        if(isDirectional):
            # Count edges
            for i in range(self.dimension):
                for j in range(self.dimension):
                    self.edges+=self.adjMatrix[i][j]
        else:
            # Refactor adj matrix
            for i in range(self.dimension):
                for j in range(self.dimension):
                    self.adjMatrix[j][i] = self.adjMatrix[i][j]
            # Count edges
            for i in range(self.dimension):
                self.edges+=self.adjMatrix[i][i]
                for j in range(i):
                    self.edges+=self.adjMatrix[i][j]
                
    def __repr__(self) -> str:
        return f"G(V:{self.dimension}, E:{self.edges}) [Directional Graph = {self.isDirectional}]"
    
    def __str__(self) -> str:
        return '\n'.join(' '.join(str(x) for x in row) for row in self.adjMatrix)

    def getArjMatrix(self) -> list[list[int]]:
        return copy.deepcopy(self.adjMatrix)
    