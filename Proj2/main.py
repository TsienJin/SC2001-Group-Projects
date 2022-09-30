from algo.dijkstra import DSearch
from test.generateTest import GenerateTest
from algo.ArrayQueue import ArrayQueue

def main():
    obj = GenerateTest(dimension=5, isDirectional=False)
    # print(str(obj))
    # print(repr(obj))
    obj.printBoth()
    
    # # #create queue object
    # queue = ArrayQueue()

    # # #get adjList
    # adjList = obj.getAdjList()
    # for srcNode in adjList.keys():
    #     for edge in adjList[srcNode]:
    #         queue.insert(sourceNode=srcNode, destNode=edge[0], weight=edge[1])
    
    # print(queue)
    # print("Lowest node with source 0:")
    # print(queue.popFrom(source=0))
    
    print("\nArray")
    print("+"*10)
    dijk = DSearch(graph=obj, useHeapAndList=False)
    dijk.solve()
    dijk.printMST()
    
    print("\nHeap")
    print("+"*10)
    dijk1 = DSearch(graph=obj, useHeapAndList=False)
    dijk1.solve()
    dijk1.printMST()
    
if __name__ == '__main__':
    main()
