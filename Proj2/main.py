from test.generateTest import GenerateTest
from algo.ArrayQueue import ArrayQueue

def main():
    obj = GenerateTest(dimension=3, isDirectional=True)
    print(str(obj))
    print(repr(obj))
    obj.printBoth()
    
    #create queue object
    queue = ArrayQueue()

    #get adjList
    adjList = obj.getAdjList()
    #insert the edges of the 2nd node
    for i in adjList[1]:
        temp = i
        queue.insert(temp)
    
    print(queue)
    #pop the node with the least weight
    item = queue.pop()
    print(item)
    print(queue)
    
if __name__ == '__main__':
    main()
