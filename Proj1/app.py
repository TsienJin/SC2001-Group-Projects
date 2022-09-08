import time
import random
# from Proj1.sort import mergeSort2

from sort.insertSort import InsertSort
# from sort.mergeSort import MergeSort
from sort.mergeSort2 import MergeSort
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
        for i in range(1000, 1010000, 10000): # generates arr from len 10,000 to 1,000,000 in incr. of 10,000
            jitter = random.randrange(-999, 1001) # generates a jitter to further randomize data
            testData = GenerateTestData(length=i+jitter)
            
            ### Creating sorting objects
            insert = InsertSort(testData.getArray())
            merge = MergeSort(testData.getArray())

            ### time for sorting methods
            # timeForMethod = self.calcTime(lamda: method(testData.getArray()))
            timeInsert = self.calcTime(lambda: insert.sort())
            timeMerge = self.calcTime(lambda: merge.sort())
            
            ### writing data to CSV file
            self.writeResult(outputFile="./result/result_InsertMerge.csv", outputStr=f"\n{testData.length},{timeInsert},{timeMerge}")
        
        pass



if __name__ == '__main__':
    SolveCompare().compareInsertMerge()