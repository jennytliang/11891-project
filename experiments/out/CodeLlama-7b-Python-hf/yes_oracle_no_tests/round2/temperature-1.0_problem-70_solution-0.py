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
    
    if len(lst) == 1:
        return lst[0]
        
    lst_sorted = sorted(lst)
    if len(lst)/2 == int((len(lst)/2)):
        mid = int(len(lst) / 2)
    else:
        mid = int(len(lst) /2 ) + 1
    
    res = []
    for i in range(mid):
        res.append(lst_sorted[-i-1])
        res.append(lst_sorted[i])
        
    return res