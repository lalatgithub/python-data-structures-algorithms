from functools import reduce

lst = [1,2,3,4,5,43,45,5]
print(reduce(lambda x, y: x if x > y else y, lst))

"""
[1,4,5,0,3]

1st iter: (1,4): 1 > 4 : false so return 4. new list: [4,5,0,3]
2nd iter: (4,5): 4 > 5 : false so return 5. new list: [5,0,3]
3rd iter: (5,0): 5 > 0 : true so return 5. new list: [5,3]
4th iter: (5,3): 5 > 3 : true so return 5
"""
