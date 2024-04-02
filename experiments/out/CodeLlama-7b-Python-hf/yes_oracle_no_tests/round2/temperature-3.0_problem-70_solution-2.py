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
	Do not include these tokens in the code: # my code # return
	'''
    # my code
    lst = sorted(lst)
    ret = []
    while lst:
        ret.append(lst[0])
        lst = lst[1:]
        lst.sort(reverse=True)
    return ret


def strange_sort_list_2(lst):
    return sorted(lst, key=lambda x: (x, -x))


def strange_sort_list_3(lst):
    return sorted(lst, key=lambda x: (-x % len(lst), x))
