
class MergeSort: 

    def __init__(self, array) -> None:
       self.name = "Merge Sort"
       self.comparison = 0
       self.swaps = 0
       self.array = array
       self.sort(array)
       

    def sort(self) -> None:

     if len(self.array) > 1: 

        #Findin the mid of the array
        mid = len(self.array) //2 

        #Dividing the array into 2 halves 
        L = self.array[:mid]

        R = self.array[mid:]

        #Sorting the first half
        self.sort(L)

        #Sorting the second half 
        self.sort(R)

        i = j = k = 0
        
        #using temp array L and R, sort the elements back to self.array
        while i<len(L) and j < len(R):
            if L[i] < R[j]:
               self.array[k] = L[i]
               i += 1
            
            else: 
                self.array[k] = R[j]
                j += 1
                
            k += 1
           # self.comparison +=1

        while i < len(L):
            self.array[k] = L[i]
            i +=1
            k +=1 

        while j < len(R):
            self.array[k] = R[j]
            j += 1
            k += 1

