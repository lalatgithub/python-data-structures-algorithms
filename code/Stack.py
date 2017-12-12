class Stack(object):
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[ len(self.items) -1 ]
        
    def is_empty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)
        
        
s = Stack()

print('is Stack empty? ', s.is_empty())
print('Stack size: ', s.size())

s.push(1);

print('Stack size after 1 push: ', s.size())

s.push(2)

print('Stack size after 2 push:', s.size())
print('Stack top item: ', s.peek())

s.pop()

print('Stack size after pop: ', s.size())
print('Stack top item after pop: ', s.peek())


