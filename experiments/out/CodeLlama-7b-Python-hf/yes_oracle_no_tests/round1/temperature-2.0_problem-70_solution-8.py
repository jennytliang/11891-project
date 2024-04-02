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
    
    sorted_lst = sorted(lst)
    result = []
    for i in range(len(sorted_lst)):
        if i % 2 == 0:
            result.append(sorted_lst[0])
            sorted_lst.pop(0)
        else:
            result.append(sorted_lst[-1])
            sorted_lst.pop(-1)
    return result


def strange_sort_list_2(lst):
    return sorted(lst, key=lambda x: x % 2)