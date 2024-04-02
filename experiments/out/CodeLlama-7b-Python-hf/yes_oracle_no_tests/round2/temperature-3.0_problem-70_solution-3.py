def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list = sorted ( lst )
	'''
    result = []
    while lst:
        min_val = min(lst)
        result.append(min_val)
        lst.remove(min_val)
        if lst:
            max_val = max(lst)
            result.append(max_val)
            lst.remove(max_val)
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
    
    Include these tokens in the code: sorted _ list = sorted ( lst )
    '''
    result = []
    while lst:
        min_val = min(lst)
        result.append(min_val)
        lst.remove(min_val)
        if lst:
            max_val = max(lst)
            result.append(max_val)
            lst.remove(max_val)
    return result


print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))


print(strange_sort_list_v2([1, 2, 3, 4]))
print(strange_sort_list_v2([5, 5, 5, 5]))
print(strange_sort_list_v2([]))
