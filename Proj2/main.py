from algo.dijkstra import DSearch
from test.generateTest import GenerateTest
from algo.ArrayQueue import ArrayQueue

def debug():
    obj = GenerateTest(dimension=5, isDirectional=True)
    obj.printBoth()
    
    print("\nArray")
    print("+"*10)
    dijk = DSearch(graph=obj, useHeap=False, useAdjList=False)
    dijk.solve()
    dijk.printMST()
    
    print("\nHeap")
    print("+"*10)
    dijk1 = DSearch(graph=obj, useHeap=True, useAdjList=True)
    dijk1.solve()
    dijk1.printMST()
    

    
if __name__ == '__main__':
    debug()
