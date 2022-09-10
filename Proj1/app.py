import time
import random
# from Proj1.sort import mergeSort2

from sort.insertSort import InsertSort
# from sort.mergeSort import MergeSort
from sort.mergeSort2 import MergeSort
from sort.hybridSort import HybridSort
from test.generateTest import GenerateTestData


class SolveCompare():
    def __init__(self) -> None:
        # self.header = ['n', 'insertTime', 'mergeTime']
        self.name = "Hello"
        
    def calcTime(self, func) -> int:
        startTime = time.time()
        func()
        endTime = time.time()
        
        return (endTime-startTime)*1000 # returns time elapsed in ms
    
    def writeResult(self, outputFile:str="/result/output.txt", outputStr:str="") -> None:
        with open(outputFile, 'a') as f:
            f.write(outputStr)
        return
    
    
        
    def compareInsertMerge(self) -> None:
        for i in range(2, 50): # generates arr from len 10,000 to 1,000,000 in incr. of 10,000
            # jitter = random.randrange(0, 100 ) # generates a jitter to further randomize data
            jitter = 0
            testData = GenerateTestData(length=i+jitter)
            
            ### Creating sorting objects
            insert = InsertSort(testData.getArray())
            merge = MergeSort(testData.getArray())

            ### time for sorting methods
            # timeForMethod = self.calcTime(lamda: method(testData.getArray()))
            timeInsert = self.calcTime(lambda: insert.sort())
            timeMerge = self.calcTime(lambda: merge.sort())
            
            ### writing data to CSV file
            self.writeResult(outputFile="./result/result_InsertMergeFocused.csv", outputStr=f"\n{testData.length},{timeInsert},{timeMerge}")
        
        pass
    
    
    def compareInsertMergeHybridComparison(self) -> None:
        for i in range(2, 50):
            jitter = 0
            testData = GenerateTestData(length=i+jitter)
            
            ### Creating sorting objects
            insert = InsertSort(testData.getArray())
            merge = MergeSort(testData.getArray())
            hybrid = HybridSort(testData.getArray())
            
            ### time for sorting methods
            timeInsert = self.calcTime(lambda: insert.sort())
            timeMerge = self.calcTime(lambda: merge.sort())
            timeHybrid = self.calcTime(lambda: hybrid.sort())
            
            ## writing data to CSV file
            # n,algo,time,comparisons
            self.writeResult(outputFile="./result/result_InsertMergeHybridFocusedN_4.csv", outputStr=f"\n{testData.length},insert,{timeInsert},{insert.comparison}")
            self.writeResult(outputFile="./result/result_InsertMergeHybridFocusedN_4.csv", outputStr=f"\n{testData.length},merge,{timeInsert},{merge.comparison}")
            self.writeResult(outputFile="./result/result_InsertMergeHybridFocusedN_4.csv", outputStr=f"\n{testData.length},hybrid,{timeInsert},{hybrid.comparison}")
            
            

if __name__ == '__main__':
    for i in range(100):
        SolveCompare().compareInsertMergeHybridComparison()