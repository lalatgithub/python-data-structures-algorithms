class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
        
q = Queue()

print('is Queue empty?', q.is_empty())
print('Queue Size?', q.size())
q.enqueue(1)
q.enqueue(1)
print('is Queue empty?', q.is_empty())
print('Size ', q.size())



