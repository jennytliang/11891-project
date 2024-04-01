def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    if len(lst) == 0:
        return lst
    elif len(lst) == 1:
        return lst
    elif len(lst) == 2:
        return [min(lst), max(lst)]
    else:
        return [min(lst), max(lst[1:]), min(lst[2:]), max(lst[3:]), min(lst[4:])]

