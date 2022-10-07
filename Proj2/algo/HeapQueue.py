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
        
    def insertEdge(self, edge:QueueEdge):
        self.queue.append(edge)
       
    # HeapSort Functions
    def heapify(self, arrLength, smallestDist) -> None:
        rootPos = smallestDist # 2
        leftPos = 2 * rootPos + 1
        rightPos = 2 * rootPos + 2
        currSmallest = rootPos
        
        if(leftPos < arrLength):
            if(leftPos < arrLength) and (rightPos < arrLength):
                currSmallest = self.smallestWt(leftPos, rightPos)
                if(currSmallest == rightPos):
                    self.queue[leftPos], self.queue[rightPos] = self.queue[rightPos], self.queue[leftPos]
                    currSmallest = leftPos
            currSmallest = self.smallestWt(currSmallest, rootPos)
        
        if(currSmallest != rootPos):
            self.queue[rootPos], self.queue[currSmallest] = self.queue[currSmallest], self.queue[rootPos]
            self.heapify(arrLength, currSmallest)
            
    def heapSort(self) -> None:
        arrLength = len(self.queue)
        
        for i in range(((arrLength // 2) - 1),-1 , -1):
            self.heapify(arrLength, i)
    
    def smallestWt(self, first, second):
        return second if (self.queue[second].distFromStart < self.queue[first].distFromStart) else first

    # Uses HeapSort to sort based on weight of edge
    # regardless of source edge
    def pop(self) -> QueueEdge:
        if(not self.isEmpty()):
            self.heapSort()
            minEdge = self.queue[0] 
            self.queue.remove(minEdge)
            return minEdge
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
    