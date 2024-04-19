class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) == 0:
            return " Queue is empty"
        else:
            return self.queue.pop(0)
        
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)
      

q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(6)
q.enqueue(9)

q.display()

q.dequeue()
print('After removing an elements:')
q.display()
