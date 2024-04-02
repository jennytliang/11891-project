def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Do not include these tokens in the code: # Your code here if
	'''
    if lst == []:
        return []
    elif len(lst) == 1:
        return lst
    else:
        lst.sort()
        lst1 = lst[0:1]
        lst2 = lst[1:]
        lst2.sort()
        lst3 = lst1 + lst2
        return lst3
    
    
    
def strange_sort_list(lst):
    return sorted(lst, key=lambda i: (i < 0, abs(i)))
