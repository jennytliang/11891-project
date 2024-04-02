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
	if len(lst) <= 1:
		return lst
	
    min_value = min(lst)
    lst.remove(min_value)
    lst_one = sorted(lst)
    min_list = [min_value] * len(lst)
    if len(lst_one) > 0:
        max_value = max(lst_one)
        lst_one.remove(max_value)
        lst_two = [max_value] + lst_one
    else:
        lst_two = [min_value + 1e-1]
    return lst_two + min_list
lst = [5, 1, 1, 5, 3, 4, 5, 6, 7, 2, 5, 6]
    # [1, 2,3,4,5,5,5,5,5,6,7, 6]
    print(strange_sort_list(lst))