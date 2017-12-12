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
        

def decimal_to_binary(decimal):
    s = Stack()
    binary = ""
    
    while decimal > 0:
        remainder = decimal % 2
        s.push(remainder)
        decimal = decimal // 2
        
    while not s.is_empty():
        binary = binary + str(s.pop())
        
    return binary
    

print(decimal_to_binary(233))


