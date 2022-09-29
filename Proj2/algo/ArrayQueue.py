class ArrayQueue():
    def __init__(self):
      self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, node):
        self.queue.append(node)
    
    def pop(self):
        if(~self.isEmpty()):
            max = 0 
            for i in range(len(self.queue)):
                if self.queue[i]
    