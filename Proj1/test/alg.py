# Insertion Sort
# --------------
# Input: Unsorted array
# Output: Sorted array
def insertionSort(myArray):
    arrayNum = len(myArray);    #Count number of elements in array
    if(arrayNum >= 1):          #Check if more than 1 element exists
        for i in range(1, arrayNum, 1):
            for j in range(i, 0, -1):
                if(myArray[j] < myArray[j-1]):  #Compare if left side element is greater than the right side element
                    swap(myArray, j, j-1)       #Swap the elements
                    
def swap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1] #Swap elements

# Merge Sort
# --------------
# Input: Unsorted array
# Output: Sorted array
def mergeSort(myArray):
    return 1