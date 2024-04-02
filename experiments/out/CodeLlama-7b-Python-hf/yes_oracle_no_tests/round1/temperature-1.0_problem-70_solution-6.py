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
    if lst == []:
        return []
    elif len(lst) == 1:
        return lst
    else:
        return [min(lst)] + [max(lst)] + [min(lst)] + [max(lst)] + [min(lst)] + [max(lst)] + [min(lst)] + [max(lst)] + strange_sort_list(sorted(lst))


#print(strange_sort_list([1, 2, 3, 4]))
#print(strange_sort_list([5, 5, 5, 5]))
#print(strange_sort_list([]))
#print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
#print(strange_sort_list([1, 1, 1, 1, 1, 1, 1, 1, 1]))
#print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
#print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
#print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
#print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
#print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 