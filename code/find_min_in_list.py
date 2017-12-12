import time

def find_min(lst):
    """
    The Big-O of this function is O(n) as we are going through each number no matter the minimum 
    number exist at the start of list, middle or at the end.
    """
    t1 = time.time()
    
    min_number = lst[0]
    
    for num in lst:
        if num < min_number:
            min_number = num
    
    t2 = time.time()
    print('Time: {:0.10f}'.format(t2 - t1))
    
    return min_number
    
lst1 = range(0, 1000)
lst2 = range(0, 10000)
lst3 = range(0, 1000000)
lst4 = range(0, 10000000)
lst5 = range(0, 100000000)

find_min(lst1)
find_min(lst2)
find_min(lst3)
find_min(lst4)
find_min(lst5)
    
    
    
    
    
    
    
