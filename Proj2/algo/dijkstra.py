from algo.ArrayQueue import ArrayQueue
# from algo.HeapQueue import HeapQueue
from algo.Queue import QueueEdge
from test.generateTest import GenerateTest

class DSearch():
    def __init__(self, graph:GenerateTest, useHeapAndList:bool=False, startNode:int=0) -> None:
        self.graph = graph
        self.adjMatrix = self.graph.adjMatrix
        self.adjList = self.graph.adjList
        self.useHeapAndList = useHeapAndList
        self.startNode = startNode
        self.path = [self.startNode]
        
        # shortest path tree (SPT) set = self.visited
        # keeps track of vertices that are included into the SPT
        # when the values are finalised
        self.visited = [False] * self.graph.dimension
        
        # i'th index is the distance of i'th node from start node
        self.distFromStart = [1e7] * self.graph.dimension 
        
        
        if(useHeapAndList):
            self.queue = ArrayQueue()
        else:
            self.queue = ArrayQueue()
        
        
    ### PUBLIC CALLABLE METHODS
        
    def solve(self) -> bool:
        self.__dArray()

        # if(self.useHeapAndList):
        #     self.__dHeap()
        # else:
        #     self.__dArray()

    
    
    
    
    ### Printing Methods
    
    def printMST(self) -> None:
        for i in range(self.graph.dimension):
            print(f"Node:{i}\tCost:{self.distFromStart[i]}")
        print(f"Path: {self.path}")
    
    
    
    ### helper methods
    
    def __getEdgesFrom(self, source:int) -> list[QueueEdge]:
        if(self.useHeapAndList):
            return self.adjList[source]
        else:
            return self.adjList[source]
        
    def __insertAdjNodesToQueueFrom(self, source:int) -> None:
        if(self.useHeapAndList):
            for edge in self.__getEdgesFrom(source):
                self.queue.insert(sourceNode=source, destNode=edge[0], weight=edge[1])
    
    
    
    
    ### Dijkstra methods
    
    def __dHeap(self) -> None:
        # init arrays for starting node
        self.distFromStart[self.startNode] = 0
        self.visited[self.startNode] = True
        
        # add starting node to the queue
        curNode = self.startNode
        self.__insertAdjNodesToQueueFrom(curNode)
        
        
        while not self.queue.isEmpty():
            nextEdge = self.queue.pop()
            self.visited[nextEdge.sourceNode] = True
            if(self.visited[nextEdge.destNode] == False):
                self.distFromStart[nextEdge.destNode] = self.distFromStart[nextEdge.sourceNode] + nextEdge.weight
                self.path.append(nextEdge.destNode)
                self.__insertAdjNodesToQueueFrom(nextEdge.destNode)
    
    def __dArray(self) -> None:
        # init arrays for starting node
        self.distFromStart[self.startNode] = 0
        self.visited[self.startNode] = True
        
        # add starting node to the queue
        curNode = self.startNode
        self.__insertAdjNodesToQueueFrom(curNode)
        
        
        while not self.queue.isEmpty():
            nextEdge = self.queue.pop()
            self.visited[nextEdge.sourceNode] = True
            if(self.visited[nextEdge.destNode] == False):
                self.distFromStart[nextEdge.destNode] = self.distFromStart[nextEdge.sourceNode] + nextEdge.weight
                self.path.append(nextEdge.destNode)
                self.__insertAdjNodesToQueueFrom(nextEdge.destNode)
                
        
                
            
            
            
        
        
        
        
    
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
    
