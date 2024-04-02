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
    if lst == []:
        return lst
    else:
        min_num = min(lst)
        max_num = max(lst)
        lst.remove(max_num)
        lst.remove(min_num)
        lst.append(min_num)
        lst.append(max_num)
        return lst


print(strange_sort_list([5, 5, 5, 5]))
