

class QueueEdge():
    def __init__(self, sourceNode:int, destNode:int, weight:int):
        self.sourceNode = sourceNode
        self.destNode = destNode
        self.weight = weight
        
    def __str__(self) -> str:
        return f"src:{self.sourceNode}\tdest:{self.destNode}\tweight:{self.weight}\tdistFromStart:{self.distFromStart}"






# class Queue():
#     def __init__(self, isHeap:bool=True):
#         self.isHeap = isHeap
#         self.arr = []
        
#     def __sortHeap(self) -> None:
#         pass
    
#     def __sortInsert(self) -> None:
#         pass
    
#     def __sort(self) -> None:
#         if self.isHeap:
#             pass
#         else:
#             pass
        
#     def pop(self, index:int=0):
#         pass
    
#     def insert(self, index:int=-1, val:int=-1):
#         pass
