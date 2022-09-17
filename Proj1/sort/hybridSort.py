class HybridSort: 

    def __init__(self, array, threshold:int=4) -> None:
        self.name = "Hybrid sort"
        self.comparison = 0
        self.swaps = 0
        self.array = array
        self.threshold = threshold  #set threshold to observe changes in time complexity and key comparisons

    #self-calling method
    def sort(self) -> None:
        self._sort(self.array)

    #insertionSort method 
    def insertSort(self, array)-> None:
        arrayNum = len(array);     #Count number of elements in array
        if(arrayNum >= 1):              #Check if more than 1 element exists
            for i in range(1, arrayNum, 1):
                for j in range(i, 0, -1):
                    self.comparison += 1
                    if(array[j] < array[j-1]):    #Compare if left side element is greater than the right side element
                        self.swap(array, j, j-1)       #Swap the elements
                        self.swaps += 1

    #function for swapping 2 elements 
    def swap(self, array, pos1, pos2) -> None:
        array[pos1], array[pos2] = array[pos2], array[pos1] #Swap 2 nodes

    #Hybrid sort (insertSort + mergeSort)
    def _sort(self, array) -> None:
        #if arraysize < threshold, use insertion sort method 
        if len(array) <= self.threshold: 
            self.insertSort(array)
    
        else:
            #Findin the mid of the array
            mid = len(array) //2 

            #Dividing the array into 2 halves 
            L = array[:mid]

            R = array[mid:]

             #Sorting the first half
            self._sort(L)

             #Sorting the second half 
            self._sort(R)

            i = j = k = 0
        
            #using temp array L and R, _sort the elements back to arr
            while i<len(L) and j < len(R):
                if L[i] < R[j]:
                   array[k] = L[i]
                   i += 1
            
                else: 
                    array[k] = R[j]
                    j += 1
                
                k += 1
                self.comparison +=1

            while i < len(L):
                array[k] = L[i]
                i +=1
                k +=1 

            while j < len(R):
                array[k] = R[j]
                j += 1
                k += 1