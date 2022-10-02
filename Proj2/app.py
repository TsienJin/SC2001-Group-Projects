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
        for i in range(1, 100):
            jitter = 0
            localDim = i+jitter
            minWeight=0
            maxWeight=50
            testGraph = GenerateTest(dimension=localDim, isDirectional=False, minWeight=minWeight, maxWeight=maxWeight)
            
            print(repr(testGraph))
            
            # create searching objects
            dHeapNList = DSearch(graph=testGraph, useHeapAndList=True)
            dNormal = DSearch(graph=testGraph, useHeapAndList=False)
            
            # timing each item
            timeHNL = self.__timeIt(lambda: dHeapNList.solve())
            timeNorm = self.__timeIt(lambda: dNormal.solve())
            
            # write data
            self.__writeResults(outputFile="compareLargeRangeUndirected.csv", outputStr=f"\n{localDim},{testGraph.edges},{False},{minWeight},{maxWeight},dHeapNList,{timeHNL}")
            self.__writeResults(outputFile="compareLargeRangeUndirected.csv", outputStr=f"\n{localDim},{testGraph.edges},{False},{minWeight},{maxWeight},dNormal,{timeNorm}")
            


if __name__ == "__main__":
    for i in range(100):
        Compare().compareLargeRangeUndirected()