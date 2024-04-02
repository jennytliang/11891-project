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
    # your code here
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return lst
    else:
        min_value = min(lst)
        max_value = max(lst)
        lst.remove(min_value)
        lst.remove(max_value)
        return [min_value, max_value] + strange_sort_list(lst)


def strange_sort_list_2(lst):
    def helper(lst):
        if len(lst) < 2:
            return lst
        else:
            return [min(lst), max(lst)] + helper(lst[2:])
    return helper(lst)


print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))
print(strange_sort_list_2([1, 2, 3, 4]))
print(strange_sort_list_2([5, 5, 5, 5]))
print(strange_sort_list_2([]))
