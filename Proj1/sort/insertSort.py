# Insertion Sort
# --------------
# Input: Unsorted array
# Output: Sorted array
# Description: Sorts an array using insertion sort. Worst case O(n^2)

import copy

class InsertSort:
    def __init__(self, array) -> None:
        self.name = "Insertion Sort"
        self.array = array
        self.comparison = 0
        self.swaps = 0
        
    def sort(self) -> None:
        arrayNum = len(self.array);     #Count number of elements in array
        if(arrayNum >= 1):              #Check if more than 1 element exists
            for i in range(1, arrayNum, 1):
                for j in range(i, 0, -1):
                    self.comparison += 1
                    if(self.array[j] < self.array[j-1]):    #Compare if left side element is greater than the right side element
                        self.swap(j, j-1)       #Swap the elements
                        
    def swap(self, pos1, pos2) -> None:
        self.array[pos1], self.array[pos2] = self.array[pos2], self.array[pos1] #Swap 2 nodes
        self.swaps += 1
    
    def getArray(self) -> list[int]: #todo
        return self.array