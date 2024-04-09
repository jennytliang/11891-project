def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list
	Do not include these tokens in the code: # Your code here
	'''
    
    # Your code here
    if len(lst) == 0:
        return lst
    new_lst = []
    while len(lst) > 0:
        new_lst.append(min(lst))
        lst.remove(min(lst))
        new_lst.append(max(lst))
        lst.remove(max(lst))
        new_lst.append(min(lst))
        lst.remove(min(lst))
        new_lst.append(max(lst))
        lst.remove(max(lst))
    return new_lst
    

print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))
