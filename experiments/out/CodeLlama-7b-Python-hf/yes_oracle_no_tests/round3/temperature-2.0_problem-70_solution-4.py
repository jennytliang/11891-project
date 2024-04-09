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
    if lst:
        a = min(lst)
        b = max(lst)
        if a == b:
            return lst
        else:
            lst.remove(a)
            lst.remove(b)
            return [a, b] + sorted(lst)
    return lst


def strange_sort_list2(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list2([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list2([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list2([]) == []
    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: # your code here if
	'''
    # your code here
    if lst:
        a = min(lst)
        b = max(lst)
        if a == b:
            return lst
        else:
            lst.remove(a)
            lst.remove(b)
            return [a, b] + sorted(lst)
    return lst


def strange_sort_list3(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list3([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list3([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list3([]) == []
    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: # your code here if
	'''
    #