class Node:
    
    def __init__(self, data, nextNode, prevNode):
        self.data = data
        self.prevNode = prevNode
        self.nextNode = nextNode
        
    def __repr__(self):
        return '<Node Data={}>'.format(self.data)
        
    @property
    def get_next(self):
        return '<Node Data={}>'.format(self.nextNode.data if self.nextNode else None)
    
    @property
    def get_prev(self):
        return '<Node Data={}>'.format(self.prevNode.data if self.prevNode else None)
        
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def set_next(self, node):
        if self.head:
            self.head.prevNode = node
        else:
            self.tail = node
        
    def set_prev(self, node):
        if self.tail:
            self.tail.nextNode = node
        else:
            self.head = node
        
    def add_to_head(self, data):
        new_node = Node(data, self.head, None)
        self.set_next(new_node)
        self.head = new_node
        
    def add_to_tail(self, data):
        new_node = Node(data, None, self.tail)
        self.set_prev(new_node)
        self.tail = new_node
    
    def remove_head(self):
        if not self.head: 
            return None
            
        self.head = self.head.nextNode
        if self.head:
            self.head.prevNode = None
        else:
            self.tail = None
            
    def remove_tail(self):
        if not self.tail: 
            return None
            
        self.tail = self.tail.prevNode
        if self.tail:
            self.tail.nextNode = None
        else:
            self.head = None
            
    def search_node(self, node_value):
        current_node = self.head
        while current_node:
            if current_node.data == node_value:
                return current_node.data
            current_node = current_node.nextNode
        
    def __iter__(self):
        if self.head:
            head = self.head
            yield head
            while head.nextNode:
                head = head.nextNode
                yield head
        

ll = LinkedList()
ll.add_to_head(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(4)

print('search: ', ll.search_node(3))

ll.remove_tail()

for item in ll:
    print('Data: {}, Next: {}, Prev: {}'.format(item, item.get_next, item.get_prev))
    print('--------------------------------------------------')
    
ll.remove_tail()

for item in ll:
    print('Data: {}, Next: {}, Prev: {}'.format(item, item.get_next, item.get_prev))
    print('--------------------------------------------------')
    
ll.remove_tail()

for item in ll:
    print('Data: {}, Next: {}, Prev: {}'.format(item, item.get_next, item.get_prev))
    print('--------------------------------------------------')
    

    
ll.remove_tail()

print('last remove')
print(ll.__dict__)
for item in ll:
    print('Data: {}, Next: {}, Prev: {}'.format(item, item.get_next, item.get_prev))
    print('--------------------------------------------------')
    
    
ll.remove_tail()
