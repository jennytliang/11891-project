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

    """
    Iterative Solution:
    
    if lst == []:
        return lst
    sorted_lst = sorted(lst)
    new_lst = []
    i, j = 0, 0

    while len(lst) > 0:
        if i == len(sorted_lst):
            new_lst.append(lst.pop())
        elif sorted_lst[i] >= lst[0]:
            new_lst.append(lst.pop(0))
            i += 1
        elif sorted_lst[i] < lst[0]:
            new_lst.append(sorted_lst[i])
            i += 1
    
    return new_lst
    """

    """
    Recursive Solution:

    # Iterative Solution:
    # if lst == []:
    #     return lst
    # sorted_lst = sorted(lst)
    # new_lst = []
    # i, j = 0, 0

    # while len(lst) > 0:
    #     if i == len(sorted_lst):
    #         new_lst.append(lst.pop())
    #     elif sorted_lst[i] >= lst[0]:
    #         new_lst.append(lst.pop(0))
    #         i += 1
    #     elif sorted_lst[i] < lst[0]:
    #         new_lst.append(sorted_lst[i])
    #         i += 1

    # return new_lst

    if lst == []:
        return lst
    else:
        min_, max_ = min(lst), max(lst)
        lst.remove(min_)
        lst.remove(max_)
        lst.append(min_)
        lst.append(max_)
        
        return strange_sort_list(lst)
    """

    if lst == []:
        return lst
    
    lst.sort()
    sorted_lst = []
    len_lst = len(lst)
    
    if len_lst % 2 == 0:
        index_count = len_lst // 2
       