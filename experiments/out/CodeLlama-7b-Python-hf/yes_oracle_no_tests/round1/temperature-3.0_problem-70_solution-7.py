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
    lst = sorted(lst)
    return [lst[0]] + [lst[-1]] + lst[1:-1]


def strange_sort_list_v2(lst):
    lst = sorted(lst)
    return [lst[0]] + lst[-1:] + lst[1:-1]


def strange_sort_list_v3(lst):
    lst = sorted(lst)
    return [lst[0]] + lst[-1::-1] + lst[1:-1]


def strange_sort_list_v4(lst):
    return [min(lst)] + [max(lst)] + lst[1:-1]


def strange_sort_list_v5(lst):
    return [min(lst)] + lst[::-1] + [max(lst)]


def strange_sort_list_v6(lst):
    return [min(lst)] + lst[1:] + [max(lst)]
