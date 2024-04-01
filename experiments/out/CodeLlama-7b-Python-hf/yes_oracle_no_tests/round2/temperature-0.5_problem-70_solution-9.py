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
    lst = sorted(lst)
    i = 0
    while i < len(lst):
        if lst[i] == lst[-1]:
            lst.remove(lst[-1])
        else:
            i += 1
    return lst


def strange_sort_list2(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
    '''
    return sorted(lst, key=lambda x: lst.count(x))


print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list2([1, 2, 3, 4]))
