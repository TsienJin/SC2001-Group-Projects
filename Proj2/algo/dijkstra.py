from re import A
import numpy as np

import ArrayQueue
from Proj2.test.generateTest import GenerateTest

class DSearch():
    def __init__(self, graph:GenerateTest, useHeap:bool=False, startNode:int=0) -> None:
        self.graph = graph
        self.adjMatrix = self.graph.adjMatrix
        self.adjArr = self.adjArr
        self.useHeap = useHeap
        self.startNode = startNode
        
        
        self.distFromStart = [] # i'th index is the distance of i'th node from start node
        self.predecessor = []
        self.solutionSet = []
        
        # shortest path tree (SPT) set = self.visited
        # keeps track of vertices that are included into the SPT
        # when the values are finalised
        self.visited = [False] * self.graph.dimension
        
        
        if(useHeap):
            self.queue = ArrayQueue()
        else:
            self.queue = ArrayQueue()
        
        
        self.tempQueue = [] #REMOVE LATER
        self.bfsQueue = [] #REMOVE LATER
        
        
    def solve(self) -> bool:
        if(self.useHeap):
            self.__dHeap()
        else:
            self.__dArray()
        pass
    
    def __dHeap(self) -> None:
        pass
    
    def __dArray(self) -> None:
        pass
    
    # def dijkstra2(self) -> None:
    #     self.distNode = [1e7] * self.graph.dimension
    #     self.predecessor = [-1] * self.graph.dimension
    #     # self.visited = [False] * self.graph.dimension
        
    #     # insert first element into the queue
    #     self.queue.insert()
    
    # def dijkstra1(self) -> None:
    #     for i in range(len(self.adjMatrix)):
    #         self.distNode[i] = np.inf
    #         self.predecessor[i] = -1
    #         self.solutionSet[i] = 0
    #     self.solutionSet[self.startNode] = 1
    #     self.distNode[self.startNode] = 0
        
    #     # Queue stuff here
        
    #     while(len(self.tempQueue) != 0):
    #         shortestNode = self.shortestDist(self.tempQueue)
    #         self.solutionSet[shortestNode] = 1
            
    #         #BFS HERE
            
    #         for i in range(len(self.bfsQueue)):
    #             if(self.predecessor[i] != 1 and self.distNode[i] > self.distNode[shortestNode] + self.adjMatrix[i][shortestNode]):
    #                 self.bfsQueue.pop()
    #                 self.distNode[i] = self.distNode[shortestNode] + self.adjMatrix[i][shortestNode]
    #                 self.predecessor[i] = shortestNode
    #                 # Put i into priority queue
    #             pass
    
