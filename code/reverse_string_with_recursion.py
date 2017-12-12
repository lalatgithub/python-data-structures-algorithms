def reverse(str):
    
    if len(str) == 1:
        return str
    
    return str[len(str) - 1] + reverse(str[:-1])

s = 'lalzada'
print(reverse(s))

s = 'aham'
print(reverse(s))
