def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list =
	Do not include these tokens in the code: return
	'''
    
    # Your code here
    if len(lst) == 0:
        return []
    else:
        min_val = min(lst)
        max_val = max(lst)
        lst.remove(min_val)
        lst.remove(max_val)
        lst.insert(0,min_val)
        lst.insert(1,max_val)
        return lst
    




def strange_sort_list_2(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list =
	Do not include these tokens in the code: return
	'''
    
    # Your code here
    if len(lst) == 0:
        return []
    else:
        min_val = min(lst)
        max_val = max(lst)
        lst.remove(min_val)
        lst.remove(max_val)
        lst.insert(0,min_val)
        lst.insert(1,max_val)
        return lst
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    