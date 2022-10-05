from algo.ArrayQueue import ArrayQueue
from algo.HeapQueue import HeapQueue
from algo.Queue import QueueEdge
from test.generateTest import GenerateTest

class DSearch():
    def __init__(self, graph:GenerateTest, startNode:int=0, useHeap:bool=False, useAdjList:bool=False) -> None:
        self.graph = graph
        self.adjMatrix = self.graph.adjMatrix
        self.adjList = self.graph.adjList
        self.useAdjList = useAdjList
        self.useHeap = useHeap
        self.startNode = startNode
        self.path = [self.startNode]
        
        # shortest path tree (SPT) set = self.visited  
        # keeps track of vertices that are included into the SPT
        # when the values are finalised
        self.visited = [False] * self.graph.dimension
        
        # i'th index is the distance of i'th node from start node
        self.distFromStart = [1e7] * self.graph.dimension 
        
        
        if(useHeap):
            self.queue = HeapQueue()
        else:
            self.queue = ArrayQueue()
        
        
    ### PUBLIC CALLABLE METHODS
        
    def solve(self) -> bool:
        self.__dijkstra()

    
    
    
    
    ### Printing Methods
    
    def printMST(self) -> None:
        for i in range(self.graph.dimension):
            print(f"Node:{i}\tCost:{self.distFromStart[i]}")
        print(f"Path: {self.path}")
    
    
    
    ### helper methods
    
    def __getEdgesFrom(self, source:int) -> list[QueueEdge]:
        if(self.useAdjList):
            return self.adjList[source]
        else:
            # maps from row to col
            edgesFromSource = []
            for i in range(self.graph.dimension):
                if(self.graph.adjMatrix[source][i] > 0):
                    edgesFromSource.append([i, self.graph.adjMatrix[source][i]])
            return edgesFromSource
        
    def __insertAdjNodesToQueueFrom(self, source:int) -> None:
        for edge in self.__getEdgesFrom(source):
            self.queue.insert(sourceNode=source, destNode=edge[0], weight=edge[1])
    
    
    
    
    ### Dijkstra methods
    def __dijkstra(self) -> None:
        # init arrays for starting node
        self.distFromStart[self.startNode] = 0
        self.visited[self.startNode] = True
        
        # add starting node to the queue
        self.__insertAdjNodesToQueueFrom(self.startNode)
        
        while not self.queue.isEmpty():
            nextEdge = self.queue.pop()
            self.visited[nextEdge.sourceNode] = True
            if(self.visited[nextEdge.destNode] == False):
                self.visited[nextEdge.destNode] = True
                self.distFromStart[nextEdge.destNode] = self.distFromStart[nextEdge.sourceNode] + nextEdge.weight
                self.path.append(nextEdge.destNode)
                self.__insertAdjNodesToQueueFrom(nextEdge.destNode)