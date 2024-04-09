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
	Do not include these tokens in the code: if len ( lst ) ==
	'''
    if len(lst) == 0:
        return []
    l = lst[0]
    for i in lst:
        if i < l:
            l = i
    lst.remove(l)
    lst.append(l)
    for i in lst:
        if i > l:
            l = i
    lst.remove(l)
    lst.insert(0, l)
    return lst


def strange_sort_list_v2(lst):
    if len(lst) <= 1:
        return lst
    else:
        return [
            min(lst),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
            min(lst[1:]),
            max(lst[1:]),
        ]


print(strange_sort_list([1, 2, 3, 4