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


def check_parenthesis(parenthesis):
    s = Stack()
    is_balanced = True
    
    for para in parenthesis:
        if para == '(':
            s.push(para)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                s.pop()
    
    if is_balanced and s.is_empty():
        return True
    else:
        return False


print(check_parenthesis("((()))"))
print(check_parenthesis("())"))


                
