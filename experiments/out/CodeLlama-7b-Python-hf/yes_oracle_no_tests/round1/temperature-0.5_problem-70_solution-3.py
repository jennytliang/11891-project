def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code:  sorted _ list = sorted
	Do not include these tokens in the code: if len
	'''

    # Pass list through sorted function to sort in ascending order
    # Then reverse order of list
    lst = sorted(lst)
    lst.reverse()
    return lst


if __name__ == '__main__':
    print(strange_sort_list([1, 2, 3, 4]))
    print(strange_sort_list([5, 5, 5, 5]))
    print(strange_sort_list([]))
