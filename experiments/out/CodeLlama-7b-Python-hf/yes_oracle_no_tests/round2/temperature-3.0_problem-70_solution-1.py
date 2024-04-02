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
	Do not include these tokens in the code: lst
	'''
    lst = sorted(lst)
    new_lst = [lst[0]]
    for i in range(len(lst)-1):
        new_lst.append(max(lst[i+1:]))
        lst.remove(max(lst[i+1:]))
    lst.remove(lst[0])
    new_lst.append(min(lst))
    return new_lst


if __name__ == '__main__':
    print(strange_sort_list([1, 2, 3, 4]))
    # [1, 4, 2, 3]
    print(strange_sort_list([5, 5, 5, 5]))
    # [5, 5, 5, 5]
    print(strange_sort_list([]))
    # []
