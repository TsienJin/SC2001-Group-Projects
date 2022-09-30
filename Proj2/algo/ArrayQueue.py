


class ArrayQueue():
    def __init__(self):
      self.queue = list([])

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, node):
        self.queue.append(node)
    
    #to pop, iterate over the queue array to find the node with the least weight, 
    #for instance, self.queue[min] = (1,2), self.queue[i] = (2,1) 
    #since self.queue[min][1] = 2 > self.queue[i][1] = 1
    #min = i
    def pop(self):
        if(~self.isEmpty()):
            min_mode = 0 
            for i in range(len(self.queue)):
                if self.queue[i][1] < self.queue[min_mode][1]:
                    min_mode = i
            item = self.queue[min_mode]
            del self.queue[min_mode]
            return item
        
        else: 
            return 0
    
