from algo.Queue import QueueEdge

class HeapQueue():
    def __init__(self):
      self.queue = []

    def __str__(self):
        return '\n'.join([str(i) for i in self.queue])

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def insert(self, sourceNode:int, destNode:int, weight:int=0) -> None:
        self.queue.append(QueueEdge(sourceNode=sourceNode, destNode=destNode, weight=weight))
        
    def insertEdge(self, edge:QueueEdge):
        self.queue.append(edge)
            
    # HeapSort Functions
    def heapify(self, arrLength, LargestDist) -> None:
        currLargest = LargestDist
        leftHeap = 2 * LargestDist + 1
        rightHeap = 2 * LargestDist + 2
        
        if(leftHeap < arrLength and self.queue[leftHeap].weight > self.queue[LargestDist].weight):
            currLargest = leftHeap
        
        if(rightHeap < arrLength and self.queue[rightHeap].weight > self.queue[LargestDist].weight):
            currLargest = rightHeap
            
        if(currLargest != LargestDist):
            (self.queue[LargestDist], self.queue[currLargest]) = (self.queue[currLargest], self.queue[LargestDist])
            self.heapify(arrLength, currLargest)
        
    def heapSort(self) -> None:
        arrLength = len(self.queue)
        
        for i in range((arrLength // 2) - 1, -1, -1):
            self.heapify(arrLength, i)

        for i in range(arrLength - 1, 0, -1):
            (self.queue[i], self.queue[0]) = (self.queue[0], self.queue[i])
            self.heapify(i, 0)
    
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
                if(edge.sourceNode==source and (minEdge==None or edge.weight<minEdge.weight)):
                    minEdge = edge
            
        if(minEdge != None):
            self.queue.remove(minEdge)
        
        return minEdge
    