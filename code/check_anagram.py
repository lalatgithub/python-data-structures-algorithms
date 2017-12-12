"""

    One string is an anagram of another if the second is simply a rearrangement of the first. 
    For example, 'heart' and 'earth' are anagrams. The strings 'python' and 'typhon' are anagrams as
    well.

"""

def is_anagram(str1, str2):
    d = {}
    
    for char in str1:
        if char not in d.keys(): 
            d[char] = 0
        
        d[char] += 1
    
    is_anagram = True
    
    for char in str2:
        if char in d.keys(): 
            d[char] -= 1
            
            if d[char] < 0: 
                is_anagram = False
        else: 
            is_anagram = False
    
    return is_anagram
    
print(is_anagram('lal', 'all'))
