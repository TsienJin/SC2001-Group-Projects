import time

from sort.insertSort import InsertSort
from sort.mergeSort import MergeSort
from test.generateTest import GenerateTestData


class SolveCompare():
    def __init__(self):
        self.header = ['n', 'insertTime', 'mergeTime']
        
    def calcTime(self, func):
        startTime = time.time()
        func()
        endTime = time.time()
        
        return (endTime-startTime)*1000 # returns time elapsed in ms
        
    def compareInsertMerge(self):
        for i in range(1000, 1010000, 10000): # generates arr from len 10,000 to 1,000,000 in incr. of 10,000
            testData = GenerateTestData(length=i)

            ### time sorting methods
            # timeForMethod = self.calcTime(lamda: method(testData.getArray()))
        
        pass



if __name__ == '__main__':
    SolveCompare().compareInsertMerge()