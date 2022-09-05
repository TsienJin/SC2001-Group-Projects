from copy import copy
import string
import sys
import os
import copy
import random



class GenerateTestData:
    def __init__(self, length:int=1000) -> None:
        self.name = "Hello"
        self.length = length
        self.sortedArray = [x+1 for x in range(self.length)]
        self.array = copy.deepcopy(self.sortedArray)
        random.shuffle(self.array)
    
    def getArray(self) -> list[int]:
        return self.array
    
    def getSortedArray(self) -> list[int]:
        return self.sortedArray
    
    def validate(self, array:list) -> bool:
        if(len(array) != self.length):
            return False
        
        for i in range(self.length):
            if(array[i] != self.sortedArray[i]):
                return False
            
        return True
    
    def exportArray(self, name:string="output") -> None:
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
    # test.exportArray("outputTest")
    # print(test.validate(test.array))



if __name__ == '__main__':
    main()