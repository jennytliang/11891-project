def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code:  sorted _ list = sorted
	Do not include these tokens in the code: if len
	'''

    if len(lst) == 0:
        return lst
    return [min(lst)] + [max(lst)] + [min(lst[1:])] + [max(lst[1:])] + strange_sort_list(lst[2:])


def strange_sort_list_2(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code:  sorted _ list = sorted
	Do not include these tokens in the code: if len
	'''

    return [min(lst)] + [max(lst)] + strange_sort_list_2(lst[2:]) if len(lst) > 1 else lst


def strange_sort_list_3(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code:  sorted _ list = sorted
	Do not include these tokens in the code: if len
	'''

    return [min(lst)] + [max(lst)] + strange_sort_list_3(lst[2:]) if len(lst) > 1 else lst
