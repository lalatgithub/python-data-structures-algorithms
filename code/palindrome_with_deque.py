class Deque:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0,item)
    
    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
        

def palindrome(str):
    
    deq = Deque()
    
    for char in str:
        deq.add_rear(char)
        
    is_palindrome = True
    
    while is_palindrome and deq.size() > 1:
        if deq.remove_rear() != deq.remove_front():
            is_palindrome = False
            
    
    return is_palindrome
    
    
    
print(palindrome('lalal'))
    
    
    
    
    
    
        
    
