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
        mid = (start + (end-1)) // 2
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
        
        for i in range(start, mid, 1):
            firstList.insert(i, self.array[i])
        for i in range(mid + 1, end, 1):
            secondList.insert(i, self.array[i])
        for pos in range(start, end, 1):
            while(firstList and secondList):
                print("firstList[0] = {}, secondList[0] = {} \n".format(firstList, secondList))
                if(firstList[0] < secondList[0]):
                    self.array[pos] = firstList.pop(0)
                    print("Array {} assigned\n".format(pos))
                elif(secondList[0] < firstList[0]):
                    self.array[pos] = secondList.pop(0)
                    print("Array {} assigned\n".format(pos))
                else:
                    self.array[pos] = firstList.pop(0)
                    print("Array {} assigned\n".format(pos))
                    pos += 1
                    self.array[pos] = secondList.pop(0)
                    print("Array {} assigned\n".format(pos))
                    if(len(firstList) == 0 and len(secondList) == 0):
                        break
                    elif(len(firstList) != 0):
                        for j in range(len(firstList)):
                            self.array[pos] = firstList[j]
                    elif(len(secondList) != 0):
                        for j in range(len(secondList)):
                            self.array[pos] = secondList[j]
                            
                print(self.array)