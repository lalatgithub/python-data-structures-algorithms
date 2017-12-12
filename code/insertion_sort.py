def insertionSort(lst):
    """
    Start from index 1 we are going to start comparing with previous values
    and starting from index 0 wouldn't have any previous value.
    
    Hold value at index 1 (current index)
    
    Iterate through all previous values one by one
    
    Compare each value with current holding value
    
    Check if current index is still greater than 0 and iterated value is
    greater than current holding value then move on values to the right
    otherwise insert current value at that position
    
    """
    for index in range(1, len(lst)):
        currentElem = lst[index]
        currentIndex = index
        
        while currentIndex > 0 and lst[currentIndex-1] > currentElem:
            lst[currentIndex] = lst[currentIndex-1]
            currentIndex -= 1
            
        lst[currentIndex] = currentElem
        
    return lst
    
l = [7,2,4,1,0,5,6]
print(insertionSort(l))

