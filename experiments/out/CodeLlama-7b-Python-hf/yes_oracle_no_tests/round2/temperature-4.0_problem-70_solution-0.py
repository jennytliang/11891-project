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
	Do not include these tokens in the code: # your code here
	'''
    # your code here
    sort = []
    if len(lst) == 0:
        return sort
    lst.sort()
    min = lst[0]
    max = lst[-1]
    while len(lst) > 0:
        if min < max:
            sort.append(min)
            lst.remove(min)
            min = max
            max = lst[-1]
        elif max > min:
            sort.append(max)
            lst.remove(max)
            max = lst[-1]
        else:
            sort.append(min)
            lst.remove(min)
            min = lst[0]
            max = lst[-1]
    return sort


def strange_sort_list_inplace(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list =
	Do not include these tokens in the code: # your code here
	'''
    # your code here
    lst.sort()
    min = lst[0]
    max = lst[-1]
    idx = 0
    while idx < len(lst):
        if min < max:
            lst[idx] = min
            idx += 1
            min = max
            max = lst[-1]
        elif max > min:
            lst[idx] = max
            idx += 1
            max = lst[-1]
        else:
            lst[idx] = min
            idx += 1
            min = lst[0]
            max = lst[-1]
    return lst
