from array import array
from copy import copy
import copy
import random

#Import a timer function to see runtime
import timeit

class GenerateTestData:
    def __init__(self, length:int=1000) -> None:
        self.length = length
        self.sortedArray = [x+1 for x in range(self.length)]
        self.array = copy.deepcopy(self.sortedArray)
        random.shuffle(self.array)
    
    def getArray(self) -> list[int]:
        return copy.deepcopy(self.array)
    
    def getSortedArray(self) -> list[int]:
        return copy.deepcopy(self.sortedArray)
    
    def validate(self, array:list) -> bool:
        if(len(array) != self.length):
            return False
        
        for i in range(self.length):
            if(array[i] != self.sortedArray[i]):
                return False
            
        return True
    
    def exportArray(self, name:str="output") -> None:
        with open(name+".txt", 'w') as f:
            for i in range(self.length):
                f.write(f"{self.array[i]}\n")
            
        with open(name+"_sorted.txt", 'w') as f:
            for i in range(self.length):
                f.write(f"{self.sortedArray[i]}\n")




def main():
    test = GenerateTestData(20)
    # print(test.array)
    # print(test.sortedArray)
    # test.exportArray("outputTest")
    # print(test.validate(test.array))
    
    #Insertion Sort test
    # insertionStart = timeit.default_timer()
    # insertionSort(test.array) #Does insertion sort on the given array
    # insertionStop = timeit.default_timer()
    # print('Insertion Sort Time: ', insertionStop - insertionStart)  
    # print(test.validate(test.array))
    
    # curData = GenerateTestData(length = 1000)
    # curData2 = copy.deepcopy(curData)
    # curData3 = copy.deepcopy(curData)
    # #print(curData.array)
    # mergeSort = MergeSort(curData.array)
    # mergeSort.sort()
    # #print(mergeSort.array)
    # print('MergeSort Comparisons: ' , mergeSort.comparison, '\n')
    # #print(curData2.array, "\n")
    # hybridSort = HybridSort(curData2.array)
    # hybridSort.sort()
    # #print(hybridSort.array)
    # print('HybridSort Key Comparisons: ' , hybridSort.comparison)
    # insertSort = InsertSort(curData3.array)
    # insertSort.sort()
    # print('Insert sort key comparison: ', insertSort.comparison)
    
    


if __name__ == '__main__':
    main()
