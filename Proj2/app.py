import time
import random

from algo.dijkstra import DSearch
from test.generateTest import GenerateTest

class Compare():
    def __init__(self) -> None:
        self.name = 'hello'
        self.resultFolder = "./results/"
        
    def __timeIt(self, func) -> int:
        startTime = time.time()
        func()
        endTime = time.time()
        
        return (endTime-startTime)*1000 # returns time elapsed in ms
    
    def __writeResults(self, outputFile:str, outputStr:str) -> None:
        print(outputStr)
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
            self.__writeResults(outputFile="compareLargeRangeUndirected.csv", outputStr=f"\n{localDim},{testGraph.edges},{False},{minWeight},{maxWeight},dHeapNList,{timeHNL}")
            self.__writeResults(outputFile="compareLargeRangeUndirected.csv", outputStr=f"\n{localDim},{testGraph.edges},{False},{minWeight},{maxWeight},dNormal,{timeNorm}")
            
            
    def compareAllVar(self) -> None:
        for i in range(1, 50):
            jitter = 0 #random.randrange(-25, 25)
            localDim = i+jitter
            minWeight = 0
            maxWeight = 50
            testGraph = GenerateTest(dimension=localDim, isDirectional=False, minWeight=minWeight, maxWeight=maxWeight)
            
            ### Creating testing object
            binArr = [True, False]
            for isHeap in binArr:
                for isAdjList in binArr:
                    curDijkstra = DSearch(graph=testGraph, startNode=0, useHeap=isHeap, useAdjList=isAdjList)
                    curTime = self.__timeIt(lambda: curDijkstra.solve())
                    self.__writeResults(outputFile="compareAllVar.csv", outputStr=f"\n{testGraph.dimension},{testGraph.edges},{testGraph.isDirectional},{minWeight},{maxWeight},{'heap' if isHeap else 'array'},{'adjList' if isAdjList else 'adjMatrix'},{curTime}")




if __name__ == "__main__":
    for i in range(100):
        Compare().compareAllVar()