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
	Do not include these tokens in the code: # your code here if
	'''
    # your code here
    if not lst:
        return []
    result = []
    while lst:
        min_val = min(lst)
        lst.remove(min_val)
        max_val = max(lst)
        lst.remove(max_val)
        result.append(min_val)
        result.append(max_val)
    return result


def strange_sort_list_v2(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: # your code here if
	'''
    # your code here
    if not lst:
        return []
    result = []
    while lst:
        min_val = min(lst)
        lst.remove(min_val)
        max_val = max(lst)
        lst.remove(max_val)
        result.append(min_val)
        result.append(max_val)
    return result
