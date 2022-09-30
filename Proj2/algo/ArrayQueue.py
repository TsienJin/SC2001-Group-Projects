

from algo.Queue import QueueEdge


class ArrayQueue():
    def __init__(self):
      self.queue = []

    def __str__(self):
        return '\n'.join([str(i) for i in self.queue])

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def insert(self, sourceNode:int, destNode:int, weight:int=0) -> None:
        self.queue.append(QueueEdge(sourceNode=sourceNode, destNode=destNode, weight=weight))
            
    
    # iterates over entire queue to find the lowest weightage edge
    # regardless of source edge
    def pop(self) -> QueueEdge:
        if(~self.isEmpty()):
            minEdge = self.queue[0] 
            for edge in self.queue:
                if edge.weight < minEdge.weight:
                    minEdge = edge
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
            
        return minEdge
    
