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
        for i in range(50000, 1000000, 50000): # generates arr from len 10,000 to 1,000,000 in incr. of 10,000
            jitter = random.randrange(0, 10000) # generates a jitter to further randomize data
            print(f"Testing Array Size: {i+jitter}")
            testData = GenerateTestData(length=i+jitter)
            
            ### Creating sorting objects
            insert = InsertSort(testData.getArray())
            merge = MergeSort(testData.getArray())

            ### time for sorting methods
            # timeForMethod = self.calcTime(lamda: method(testData.getArray()))
            timeInsert = self.calcTime(lambda: insert.sort())
            timeMerge = self.calcTime(lambda: merge.sort())
            
            ### writing data to CSV file
            # self.writeResult(outputFile="./result/result_InsertMergeFocused.csv", outputStr=f"\n{testData.length},{timeInsert},{timeMerge}")
            self.writeResult(outputFile="./result/result_InsertMerge.csv", outputStr=f"\n{testData.length},{timeInsert},{timeMerge}")
        

    def hybridNTesting(self) -> None:
        for arrSize in range(2, 101):
            for i in range (1, 9): # testing where N = i to determine best N
                testData = GenerateTestData(length=arrSize)
                hybrid = HybridSort(testData.getArray(), threshold=i)
                timeHybrid = self.calcTime(lambda: hybrid.sort())
                
                # self.writeResult(outputFile="./result/result_hybridAnalysis.csv", outputStr=f"\n{testData.length},{i},{timeHybrid},{hybrid.comparison}")
                self.writeResult(outputFile="./result/result_hybridAnalysis10m.csv", outputStr=f"\n{testData.length},{i},{timeHybrid},{hybrid.comparison}")
            
    
    def compareInsertMergeHybridComparison(self) -> None:
        for i in range(2, 50):
            jitter = 0
            testData = GenerateTestData(length=i+jitter)
            
            ### Creating sorting objects
            insert = InsertSort(testData.getArray())
            merge = MergeSort(testData.getArray())
            hybrid = HybridSort(testData.getArray(), threshold=5)
            
            ### time for sorting methods
            timeInsert = self.calcTime(lambda: insert.sort())
            timeMerge = self.calcTime(lambda: merge.sort())
            timeHybrid = self.calcTime(lambda: hybrid.sort())
            
            ## writing data to CSV file
            # n,algo,time,comparisons
            # self.writeResult(outputFile="./result/result_InsertMergeHybridFocusedN_4.csv", outputStr=f"\n{testData.length},insert,{timeInsert},{insert.comparison}")
            # self.writeResult(outputFile="./result/result_InsertMergeHybridFocusedN_4.csv", outputStr=f"\n{testData.length},merge,{timeMerge},{merge.comparison}")
            # self.writeResult(outputFile="./result/result_InsertMergeHybridFocusedN_4.csv", outputStr=f"\n{testData.length},hybrid,{timeHybrid},{hybrid.comparison}")
            
            self.writeResult(outputFile="./result/result_InsertMergeHybridFocusedN_410m.csv", outputStr=f"\n{testData.length},insert,{timeInsert},{insert.comparison}")
            self.writeResult(outputFile="./result/result_InsertMergeHybridFocusedN_410m.csv", outputStr=f"\n{testData.length},merge,{timeMerge},{merge.comparison}")
            self.writeResult(outputFile="./result/result_InsertMergeHybridFocusedN_410m.csv", outputStr=f"\n{testData.length},hybrid,{timeHybrid},{hybrid.comparison}")
            
            

if __name__ == '__main__':
    for i in range(1):
        SolveCompare().compareInsertMerge()
    
    # result = open("Proj1/result/result_InsertMergeFocused10m.csv", "w") # Overwrites file if exist, else creates new file
    # result.close()
    # result = open("Proj1/result/result_hybridAnalysis10m.csv", "w") # Overwrites file if exist, else creates new file
    # result.close()
    # result = open("Proj1/result/result_InsertMergeHybridFocusedN_410m.csv", "w") # Overwrites file if exist, else creates new file
    # result.close()
    # for i in range(10000, 100001, 10000):
    #     SolveCompare().compareInsertMergeHybridComparison()