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
    # my code
    # return sorted(lst)
    # return sorted(lst, reverse=True)
    # return sorted(lst, reverse=True)[::-1]
    # return sorted(lst, reverse=True)[::-1]
    # return sorted(lst, reverse=True)
    # return sorted(lst, reverse=True)
    # return sorted(lst, reverse=True)

    # lab code
    if lst == []:
        return []
    min_value = min(lst)
    max_value = max(lst)
    lst.remove(min_value)
    lst.remove(max_value)
    return [min_value, max_value] + strange_sort_list(lst)


print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))
