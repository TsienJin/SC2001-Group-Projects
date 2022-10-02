from algo.dijkstra import DSearch
from test.generateTest import GenerateTest
from algo.ArrayQueue import ArrayQueue

def debug():
    obj = GenerateTest(dimension=5, isDirectional=True)
    obj.printBoth()
    
    print("\nArray")
    print("+"*10)
    dijk = DSearch(graph=obj, useHeapAndList=False)
    dijk.solve()
    dijk.printMST()
    
    print("\nHeap")
    print("+"*10)
    dijk1 = DSearch(graph=obj, useHeapAndList=True)
    dijk1.solve()
    dijk1.printMST()
    

    
if __name__ == '__main__':
    debug()
