# Merge Sort
# --------------
# Input: Unsorted array
# Output: Sorted array
# Description: Sorts an array using merge sort. Worst case O(n lg n)
import copy

class MergeSort:
    def __init__(self, array) -> None:
        self.name = "Merge Sort"
        self.array = copy.deepcopy(array)
    
    def mergeSort(self, start, end) -> None:
        mid = (start + end) // 2
        if((end - start) <= 0):
            return
        elif((end - start) > 1):
            self.mergeSort(start, mid)
            self.mergeSort((mid+1), end)
        self.sort(start, end)
    
    def sort(self, start, end) -> None:
        if((end - start) <= 0):
            return
        mid = (start + end) // 2
        
        firstList = []
        secondList = []
        
        for i in range(start, mid + 1, 1):
            firstList.insert(i, self.array.pop(start))
        for i in range(mid + 1, end + 1, 1):
            secondList.insert(i, self.array.pop(start))
        pos = start
        while(firstList and secondList):
            if(firstList[0] < secondList[0]):
                self.array.insert(pos, firstList.pop(0))
            elif(secondList[0] < firstList[0]):
                self.array.insert(pos, secondList.pop(0))
            else:
                self.array.insert(pos, firstList.pop(0))
                pos += 1
                self.array.insert(pos, secondList.pop(0))
            pos += 1
        if(firstList):
            for j in firstList:
                self.array.insert(pos, j)
                pos += 1
        elif(secondList):
            for j in secondList:
                self.array.insert(pos, j)
                pos += 1