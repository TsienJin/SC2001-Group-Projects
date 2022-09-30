import numpy as np

class DSearch():
    def __init__(self, adjMatrix:list[list[int]]=[[]], useHeap:bool=True, startNode:int=0):
        self.adjMatrix = adjMatrix
        self.useHeap = useHeap
        self.distNode = []
        self.predecessor = []
        self.solutionSet = []
        self.tempQueue = [] #REMOVE LATER
        self.bfsQueue = [] #REMOVE LATER
        
        
    def solve(self) -> bool:
        # returns true if the graph is solvable
        # returns false if the graph is NOT solvable
        pass
    
    def dijkstra(self) -> None:
        srcNode = 0
        for i in range(len(self.adjMatrix)):
            self.distNode[i] = np.inf
            self.predecessor[i] = -1
            self.solutionSet[i] = 0
        self.solutionSet[srcNode] = 1
        self.distNode[srcNode] = 0
        
        # Queue stuff here
        
        while(len(self.tempQueue) != 0):
            shortestNode = self.shortestDist(self.tempQueue)
            self.solutionSet[shortestNode] = 1
            
            #BFS HERE
            
            for i in range(len(self.bfsQueue)):
                if(self.predecessor[i] != 1 and self.distNode[i] > self.distNode[shortestNode] + self.adjMatrix[i][shortestNode]):
                    self.bfsQueue.pop()
                    self.distNode[i] = self.distNode[shortestNode] + self.adjMatrix[i][shortestNode]
                    self.predecessor[i] = shortestNode
                    # Put i into priority queue
                pass
    
    def shortestDist(self, priorityQueue) -> bool:
        pass