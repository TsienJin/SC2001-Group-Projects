from algo.Queue import QueueEdge

class HeapQueue():
    def __init__(self):
        self.queue = []
        
    def __str__(self):
        return '\n'.join([str(i) for i in self.queue])
    
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self, sourceNode:int, destNode:int, weight:int=0) -> None:
        self.queue.append()
        
    def pop(self) -> QueueEdge:
        pass
    