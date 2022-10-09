
import numpy as np
import copy
import math


### Generate test object
class GenerateTest():
    
    # Constructor
    def __init__(self, dimension:int=10, isDirectional:bool=False, minWeight:int=0, maxWeight:int=9) -> None:
        # init values
        self.dimension = dimension
        self.isDirectional = isDirectional
        self.minWeight = minWeight
        self.maxWeight = maxWeight
        self.adjMatrix = np.random.randint(self.minWeight,self.maxWeight, (self.dimension, self.dimension)).tolist()
        self.adjList = {}
        
        # number of vertecies and housekeeping for non-directional graphs
        self.edges = self.__refactorAndCount()
        
        # convert matrix to list 
        self.adjList = self.__matrixToList()
        
    #added adjMatrix -> list method 
    def __matrixToList(self): 
        adjList = {}
        for i in range(self.dimension):
            adjList[i] = []  
        for i in range(self.dimension):
            for j in range(self.dimension):
                weight = self.adjMatrix[i][j] ## from row to column
                if(weight >0):
                    temp = [j, weight]
                    adjList[i].append(temp)
        return adjList
    
    def __refactorAndCount(self) -> int:
        edges = 0
        if(self.isDirectional):
            # Count edges
            for i in range(self.dimension):
                for j in range(self.dimension):
                    if(i == j): 
                        self.adjMatrix[i][j] = 0 #for self- looping the  weight should equal 0 
                    if(self.adjMatrix[i][j] > 0):
                        edges+=1
        else:
            # Refactor adj matrix
            for i in range(self.dimension):
                for j in range(self.dimension):
                    if(i == j): 
                        self.adjMatrix[i][j] = 0 #for self- looping the  weight should equal 0 
                    self.adjMatrix[j][i] = self.adjMatrix[i][j]
            # Count edges
            for i in range(self.dimension):
                edges+=self.adjMatrix[i][i]
                for j in range(i):
                    if(self.adjMatrix[i][j] > 0):
                        edges+=1
                        
        return edges
                
    def __repr__(self) -> str:
        return f"G(V:{self.dimension}, E:{self.edges}) [Directional Graph = {self.isDirectional}]"
    
    def __str__(self) -> str:
        return '\n'.join(' '.join(str(x) for x in row) for row in self.adjMatrix)

    def getAdjMatrix(self) -> list[list[int]]:
        return copy.deepcopy(self.adjMatrix)
    
    def getAdjList(self):
        return copy.deepcopy(self.adjList)

    
    # print both adjacent list and adjacent matrix
    def printBoth(self) -> None:
        print("\nAdjacency List:\n" + "=" * 10)
        for v in self.adjList:
            toPrint = "{} -> ".format(v)
            for e in self.adjList[v]:
                toPrint += "{} ".format(e)
            print(toPrint)
        print("\nAdjacency Matrix:\n" + "=" * 10)
        print(self.__str__())
