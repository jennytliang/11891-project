def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Do not include these tokens in the code: # Your code here if
	'''
    if lst == []:
        return []
    else:
        lst_out = []
        while lst != []:
            lst_out.append(min(lst))
            lst.remove(min(lst))
            lst_out.append(max(lst))
            lst.remove(max(lst))
            lst_out.append(min(lst))
            lst.remove(min(lst))
            lst_out.append(max(lst))
            lst.remove(max(lst))
        return lst_out


def strange_sort_list_v2(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Do not include these tokens in the code: # Your code here if
	'''
    if lst == []:
        return []
    else:
        lst_out = []
        lst_out.append(min(lst))
        lst.remove(min(lst))
        lst_out.append(max(lst))
        lst.remove(max(lst))
        lst_out.append(min(lst))
        lst.remove(min(lst))
        lst_out.append(max(lst))
        lst.remove(max(lst))
        return lst_out


def strange_sort_list_v3(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]