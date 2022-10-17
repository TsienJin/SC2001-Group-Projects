import time


### function to measure the time taken of lambda function
# takes in lambda function and returns a float (in ms)
def timeIt(func) -> float:
    start = time.time()
    func()
    end = time.time()
    return (end-start)*1000



### knap object

class knap():
    def __init__(self, capacity:int, weight:list[int]=[4, 6, 8], profit:list[int] = [7, 6, 9]) -> None:
        self.capacity = capacity
        self.weight = weight
        self.profit = profit
        self.items = len(self.weight)
        self.memTD = {}
        self.memBU = [0] * (capacity+1)
        
        if(len(self.weight) != len(self.profit)):
            raise ValueError("Number of elements in WEIGHT and PROFIT do not match!")
        
        
        
    def recursive(self) -> int:
        return self.__recursive(self.capacity)
    
    def __recursive(self, capacity:int) -> int:
        
        # base case, cannot fit any new items 
        if(capacity<min(self.weight)):
            return 0

        children = [0] # contains max profit from children calls
        
        # iterate over items recursively
        for item in range(self.items):
            if(capacity - self.weight[item] >= 0):
                children.append(self.__recursive(capacity=capacity-self.weight[item]) + self.profit[item])
            
        # returns max value from children + value of item
        return max(children)
    
    
    def dpTopDown(self) -> int:
        val = self.__dpTopDown(self.capacity)
        # print(self.memTD)
        return val
        
    def __dpTopDown(self, capacity) -> int: # memoization from a top down recursive approach
        
        # base case, cannot fit any new items 
        if(capacity<min(self.weight)):
            return 0

        children = [0] # contains max profit from children calls
        
        # iterate over items recursively
        for item in range(self.items):
            if(capacity>self.weight[item] and (capacity-self.weight[item]) in self.memTD.keys() and (self.memTD[capacity-self.weight[item]]>=0)):
                children.append(self.memTD[capacity-self.weight[item]] + self.profit[item])
            elif(capacity-self.weight[item]>=0):
                children.append(self.__dpTopDown(capacity=capacity-self.weight[item]) + self.profit[item])
            
        # returns max value from children + value of item
        self.memTD[capacity] = max(children)
        return self.memTD[capacity]
        
        
        
        
    def dpBottomUp(self) -> int: # memoization from a bottom up dp approach
        
        for cap in range(self.capacity+1):
            for item in range(self.items):
                if(cap>self.weight[item]): 
                    self.memBU[cap] = max(self.memBU[cap], self.memBU[cap-self.weight[item]]+self.profit[item])
        
        return self.memBU[self.capacity]

        


if __name__ == "__main__":
    # obj = knap(capacity=8, weight=[1, 3, 4, 5], profit=[10, 40, 50, 70])
    obj = knap(capacity=50)
    print(f"Recursive:\t\t{timeIt(lambda: obj.recursive())}")
    print(f"Memoization Top Down:\t{timeIt(lambda: obj.dpTopDown())}")
    print(f"Memoization Bottom Up:\t{timeIt(lambda: obj.dpBottomUp())}")
    
        