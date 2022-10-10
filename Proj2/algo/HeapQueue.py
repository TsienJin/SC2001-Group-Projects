from logging import root
import queue
from algo.Queue import QueueEdge

class HeapQueue():
    def __init__(self):
      self.queue = []

    def __str__(self):
        return '\n'.join([str(i) for i in self.queue])

    def isEmpty(self) -> bool:
        return len(self.queue) == 0


    def insert(self, sourceNode:int, destNode:int, weight:int, distFromStart:int) -> None:
        self.queue.append(QueueEdge(sourceNode=sourceNode, destNode=destNode, weight=weight, distFromStart=distFromStart))
        self.upHeap(len(self.queue)-1)
        
    def insertEdge(self, edge:QueueEdge):
        self.queue.append(edge)
       
    # HeapSort Functions
    #upheap: when a new node is addded to the end of array, perform heapify, ie compare the new node with its parent, and swap places if necessary 
    def upHeap(self, lastNode) -> None:
        if(lastNode < 1): return 
        parentNode = (lastNode -1) // 2

        minNode = self.smallestWt(parentNode, lastNode)

        if(minNode != parentNode):
            self.queue[lastNode], self.queue[parentNode] = self.queue[parentNode], self.queue[lastNode]
            self.upHeap(parentNode)
    
    #downheap: The node to be removed is the rootNode, pop() first swap the rootNode with the lastNode, the rootNode (which is now contains the lastNode) will do heapify 
    #to check against its child node, and swap places if necessary 
    def downHeap(self, parentNode) -> None:    
        arrLength = len(self.queue)
        leftNode = 2 * parentNode + 1 
        rightNode = 2 * parentNode + 2 

        if(leftNode < arrLength and rightNode< arrLength):
            minNode = self.smallestWt(leftNode, rightNode)
            minNode = self.smallestWt(minNode, parentNode)
            if(minNode!= parentNode):
                self.queue[minNode], self.queue[parentNode] = self.queue[parentNode], self.queue[minNode]
                self.downHeap(minNode)

        if(leftNode < arrLength):
            minNode = self.smallestWt(leftNode, parentNode)
            if(minNode!= parentNode):
                self.queue[minNode], self.queue[parentNode] = self.queue[parentNode], self.queue[minNode]
                self.downHeap(minNode)
    
    def smallestWt(self, first, second):
        return second if (self.queue[second].distFromStart < self.queue[first].distFromStart) else first

    # Uses HeapSort to sort based on weight of edge
    # regardless of source edge
    def pop(self) -> QueueEdge:
        if(not self.isEmpty()):
            toPop = self.queue[0]
            minNode = 0
            lastNode = len(self.queue)-1
            self.queue[minNode], self.queue[lastNode] = self.queue[lastNode],self.queue[minNode]
            self.queue.remove(self.queue[lastNode])
            self.downHeap(minNode)
            return toPop
        else: 
            return None
        
    # iterates over entire queue to find the lowest weightage edge
    # with respect to source edge
    def popFrom(self, source:int):
        
        minEdge = None
        
        if(not self.isEmpty()):
            for edge in self.queue:
                if(edge.sourceNode==source and (minEdge==None or edge.distFromStart<minEdge.distFromStart)):
                    minEdge = edge
            
        if(minEdge != None):
            self.queue.remove(minEdge)
        
        return minEdge
    
