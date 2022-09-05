from copy import copy
import sys
import os
import copy
import random



class GenerateTestData:
    def __init__(self, length=1000) -> None:
        self.name = "Hello"
        self.length = length
        self.sortedArray = [x+1 for x in range(self.length)]
        self.array = copy.deepcopy(self.sortedArray)
        random.shuffle(self.array)
    
    def getArray(self):
        return self.array
    
    def getSortedArray(self):
        return self.sortedArray
    
    def exportArray(self, name="output"):
        with open(name+".txt", 'w') as f:
            for i in range(self.length):
                f.write(f"{self.array[i]}\n")
            
        with open(name+"_sorted.txt", 'w') as f:
            for i in range(self.length):
                f.write(f"{self.sortedArray[i]}\n")




def main():
    test = GenerateTestData(10)
    print(test.array)
    print(test.sortedArray)
    test.exportArray("outputTest")



if __name__ == '__main__':
    main()