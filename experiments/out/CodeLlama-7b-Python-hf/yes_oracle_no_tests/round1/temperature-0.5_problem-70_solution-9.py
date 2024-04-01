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

    return sorted(lst, key=lambda x: (x, -x))


def strange_sort_list_inplace(lst):
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

    lst.sort(key=lambda x: (x, -x))
    return lst


print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))

print(strange_sort_list_inplace([1, 2, 3, 4]))
print(strange_sort_list_inplace([5, 5, 5, 5]))
print(strange_sort_list_inplace([]))
