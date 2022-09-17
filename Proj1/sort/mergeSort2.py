
class MergeSort: 

    def __init__(self, array) -> None:
       self.name = "Merge _sort"
       self.array = array
       self.comparison = 0
       self.swaps = 0
    
    def sort(self) -> None:
        self._sort(self.array)
       

    def _sort(self, arr) -> None:

     if len(arr) > 1: 

        #Findin the mid of the array
        mid = len(arr) //2 

        #Dividing the array into 2 halves 
        L = arr[:mid]

        R = arr[mid:]

        #Sorting the first half
        self._sort(L)

        #Sorting the second half 
        self._sort(R)

        i = j = k = 0
        
        #using temp array L and R, _sort the elements back to arr
        while i<len(L) and j < len(R):
            if L[i] < R[j]:
               arr[k] = L[i]
               i += 1
            
            else: 
                arr[k] = R[j]
                j += 1
                
            k += 1
            self.comparison +=1

        while i < len(L):
            arr[k] = L[i]
            i +=1
            k +=1 

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

