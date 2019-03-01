class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        #flip the first stack to get FIFO order.
        while len(self.first) != 0:
            self.second.append(self.first.pop())
        
        #get element at the front of the queue.
        front_element = self.second[-1]

        #return first stack to LIFO order to continue to enqueue
        while len(self.second) != 0:
            self.first.append(self.second.pop())
        
        return front_element
        
        
    def pop(self):
        #flip the first stack to get FIFO order.
        while len(self.first) != 0:
            self.second.append(self.first.pop())
        
        #get element at the front of the queue.
        front_element = self.second.pop()

        #return first stack to LIFO order to continue to enqueue
        while len(self.second) != 0:
            self.first.append(self.second.pop())
        
        return front_element
        
        
    def put(self, value):
        self.first.append(value)