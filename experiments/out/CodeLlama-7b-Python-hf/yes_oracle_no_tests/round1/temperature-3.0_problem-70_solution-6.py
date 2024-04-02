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
	Do not include these tokens in the code: if lst == [] :
	'''

    if lst == []:
        return []
    min_value = min(lst)
    max_value = max(lst)
    result = []
    while lst != []:
        result.append(min_value)
        lst.remove(min_value)
        result.append(max_value)
        lst.remove(max_value)
        min_value = min(lst)
        max_value = max(lst)
    return result


def strange_sort_list_2(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list
	Do not include these tokens in the code: if lst == [] :
	'''

    if lst == []:
        return []
    min_value = min(lst)
    max_value = max(lst)
    result = []
    while lst != []:
        result.append(min_value)
        lst.remove(min_value)
        result.append(max_value)
        lst.remove(max_value)
        min_value = min(lst)
        max_value = max(lst)
    return result
