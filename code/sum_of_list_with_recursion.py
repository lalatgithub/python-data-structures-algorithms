def sum_list(lst):
    my_list = lst

    if len(my_list) == 1:
        return my_list[0]
        
    return my_list[0] + sum_list(my_list[1:])
    

lst = [1,2,3,4]

print(sum_list(lst))
