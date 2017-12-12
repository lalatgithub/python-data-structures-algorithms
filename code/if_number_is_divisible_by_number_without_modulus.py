def is_divisible(number, divisible_by):
    """
    divide number by divisible_by
    
    Convert result to integer (that is get rid of the decimal portion)
    
    Multiply the integer value by divisible_by
    
    If the result of the multiplication equals the original number than the number is evenly divisible 
    by divisible_by.
    
    """
    return divisible_by * int((number/divisible_by)) == number
    

print(is_divisible(74, 37))

print(is_divisible(74, 3))

print(is_divisible(9, 3))

print(is_divisible(4, 33))
