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
    return sorted(lst)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3], "Sorting 1"
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5], "Sorting 2"
    assert strange_sort_list([2, 2, 2, 2]) == [2, 2, 2, 2], "Sorting 3"
    assert strange_sort_list([]) == [], "Sorting empty"
