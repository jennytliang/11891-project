def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list =
	Do not include these tokens in the code: return
	'''
    # your code here
    if len(lst) == 0:
        return lst
    else:
        sorted_lst = sorted(lst)
        lst_len = len(lst)
        new_lst = []
        for i in range(lst_len):
            if i % 2 == 0:
                new_lst.append(sorted_lst[-1])
            else:
                new_lst.append(sorted_lst[0])
            del sorted_lst[-1] if i % 2 == 0 else sorted_lst.pop(0)
        return new_lst


def strange_sort_list_2(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list =
	Do not include these tokens in the code: return
	'''
    # your code here
    if len(lst) == 0:
        return lst
    else:
        sorted_lst = sorted(lst)
        lst_len = len(lst)
        new_lst = []
        for i in range(lst_len):
            if i % 2 == 0:
                new_lst.append(sorted_lst[-1])
            else:
                new_lst.append(sorted_lst[0])
            del sorted_lst[-1] if i % 2 == 0 else sorted_lst.pop(0)
        return new_lst


def strange_sort_list_3(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers,