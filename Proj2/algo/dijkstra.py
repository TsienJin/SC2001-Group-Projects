

class DSearch():
    def __init__(self, adjMatrix:list[list[int]]=[[]], useHeap:bool=True):
        self.adjMatrix = adjMatrix
        self.useHeap = useHeap
        
    def solve(self) -> bool:
        # returns true if the graph is solvable
        # returns false if the graph is NOT solvable
        pass