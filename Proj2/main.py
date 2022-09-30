from test.generateTest import GenerateTest
from algo.ArrayQueue import ArrayQueue

def main():
    obj = GenerateTest(dimension=10, isDirectional=False)
    # print(str(obj))
    # print(repr(obj))
    obj.printBoth()
    
    # #create queue object
    queue = ArrayQueue()

    # #get adjList
    adjList = obj.getAdjList()
    for srcNode in adjList.keys():
        for edge in adjList[srcNode]:
            queue.insert(sourceNode=srcNode, destNode=edge[0], weight=edge[1])
    
    print(queue)
    print("Lowest node with source 0:")
    print(queue.popFrom(source=0))
    
if __name__ == '__main__':
    main()
