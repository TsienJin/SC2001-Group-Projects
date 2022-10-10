import time
import random

from algo.dijkstra import DSearch
from test.generateTest import GenerateTest

class Compare():
    def __init__(self) -> None:
        self.resultFolder = "./results/"
        
    def __timeIt(self, func) -> int:
        startTime = time.time()
        func()
        endTime = time.time()
        
        return (endTime-startTime)*1000 # returns time elapsed in ms
    
    def __writeResults(self, outputFile:str, outputStr:str) -> None:
        # print(outputStr)
        with open(self.resultFolder+outputFile, 'a') as f:
            f.write(outputStr)
        return
    
    def compareLargeRangeUndirected(self) -> None:
        for i in range(1, 60):
            jitter = 0
            localDim = i+jitter
            minWeight=0
            maxWeight=50
            testGraph = GenerateTest(dimension=localDim, isDirectional=False, minWeight=minWeight, maxWeight=maxWeight)
            
            print(repr(testGraph))
            
            # create searching objects
            dHeapNList = DSearch(graph=testGraph, useHeap=True, useAdjList=True)
            dNormal = DSearch(graph=testGraph, useHeap=False, useAdjList=False)
            
            # timing each item
            timeHNL = self.__timeIt(lambda: dHeapNList.solve())
            timeNorm = self.__timeIt(lambda: dNormal.solve())
            
            # write data
            # self.__writeResults(outputFile="compareLargeRangeUndirected.csv", outputStr=f"\n{localDim},{testGraph.edges},{False},{minWeight},{maxWeight},dHeapNList,{timeHNL}")
            # self.__writeResults(outputFile="compareLargeRangeUndirected.csv", outputStr=f"\n{localDim},{testGraph.edges},{False},{minWeight},{maxWeight},dNormal,{timeNorm}")
            
            self.__writeResults(outputFile="compareLargeRangeUndirected_ZY.csv", outputStr=f"\n{localDim},{testGraph.edges},{False},{minWeight},{maxWeight},dHeapNList,{timeHNL}")
            self.__writeResults(outputFile="compareLargeRangeUndirected_ZY.csv", outputStr=f"\n{localDim},{testGraph.edges},{False},{minWeight},{maxWeight},dNormal,{timeNorm}")
    
    def __templateTester(self, graph:GenerateTest, startNode:int=0, outputFile:str=f"result_{time.time()}.csv"):
        binArr = [True, False]
        for isHeap in binArr:
            for isAdjList in binArr:
                curDijkstra = DSearch(graph=graph, startNode=0, useHeap=isHeap, useAdjList=isAdjList)
                curTime = self.__timeIt(lambda: curDijkstra.solve())
                self.__writeResults(outputFile=f"{outputFile}", outputStr=f"\n{graph.dimension},{graph.edges},{graph.isDirectional},{graph.minWeight},{graph.maxWeight},{'heap' if isHeap else 'array'},{'adjList' if isAdjList else 'adjMatrix'},{curTime}")

        
            
    def compareAllVar(self, minDim:int=1, maxDim:int=100, jump:int=1) -> None:
        for i in range(minDim, maxDim, jump):
            jitter = 0 #random.randrange(-25, 25)
            localDim = i+jitter
            minWeight = 0
            maxWeight = 50
            testGraph = GenerateTest(dimension=localDim, isDirectional=False, minWeight=minWeight, maxWeight=maxWeight)
            
            self.__templateTester(graph=testGraph, outputFile="compareAllVar.csv")
            
            
    def compareAllNonWeighted(self, minDim:int=1, maxDim:int=100, jump:int=1) -> None:
        for i in range(minDim,maxDim, jump):
            jitter = 0
            localDim = i+jitter
            minWeight = 0
            maxWeight = 1
            testGraph = GenerateTest(dimension=localDim, isDirectional=False, minWeight=minWeight, maxWeight=maxWeight)
            
            self.__templateTester(graph=testGraph, outputFile="CompareAllNonWeighted.csv")
            
    def compareAllWeighted(self, minDim:int=1, maxDim:int=100, jump:int=1) -> None:
        for i in range(minDim, maxDim, jump):
            jitter = 0
            localDim = jitter+i
            minWeight = 1
            maxWeight = 50
            testGraph = GenerateTest(dimension=localDim, isDirectional=False, minWeight=minWeight, maxWeight=maxWeight)

            self.__templateTester(graph=testGraph, outputFile="CompareAllWeighted.csv")
            





### testing
def testSmallAll():
    for i in range(10):
        print(f"Run: {i+1}")
        Compare().compareAllNonWeighted()
        Compare().compareAllWeighted()
        Compare().compareAllVar()

def testLargeAll():
    for i in range(5):
        print(f"Run: {i+1}")
        Compare().compareAllNonWeighted(minDim=100,maxDim=251,jump=10)
        Compare().compareAllWeighted(minDim=100,maxDim=251,jump=10)
        Compare().compareAllVar(minDim=100,maxDim=251,jump=10)


if __name__ == "__main__":
    for i in range(5):
        # testLargeAll()
        testSmallAll()
    
