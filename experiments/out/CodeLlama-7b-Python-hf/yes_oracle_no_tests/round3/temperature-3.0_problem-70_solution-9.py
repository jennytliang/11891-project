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
	Do not include these tokens in the code: # Y OUR CO DE H
	'''
    return sorted(lst)

if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    lst = [1, 2, 3, 4]
    print(strange_sort_list(lst))
    lst = [1, 2, 3, 4, 5]
    print(strange_sort_list(lst))
    lst = [5, 5, 5, 5]
    print(strange_sort_list(lst))
    lst = [1, 2, 3, 4, 4, 3, 2, 1]
    print(strange_sort_list(lst))
    lst = [1, 1]
    print(strange_sort_list(lst))
    lst = [1, 2, 3, 4, 5, 6, 7]
    print(strange_sort_list(lst))
    lst = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7]
    print(strange_sort_list(lst))
    lst = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
    print(strange_sort_list(lst))
    lst = []
    print(strange_sort_list(lst))