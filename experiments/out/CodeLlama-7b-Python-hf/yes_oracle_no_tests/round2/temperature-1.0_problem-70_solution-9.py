def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: if len ( lst ) <=
	'''
    
    strn_lst = []
    while len(lst) > 0:
        n_vals = sorted(lst)
        strn_lst.extend([n_vals.pop(0)] + [n_vals.pop(-2)])
        n_vals.remove(n_vals.pop(0))
        lst = n_vals
            
    return strn_lst
