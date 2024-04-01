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

    return sorted(lst, reverse=True)


def test_function():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3], "First"
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5], "Second"
    assert strange_sort_list([]) == [], "Third"
    assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3], "Fourth"
    assert strange_sort_list([1]) == [1], "Fifth"
    assert strange_sort_list([1, 1]) == [1, 1], "Sixth"
    assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [
        1, 10, 2, 9, 3, 8, 4, 7, 5, 6
    ], "Seventh"
    assert strange_sort_list([-1, -2, -3, -4, -5]) == [
        -5, -4, -3, -2, -1
    ], "Eighth"
    assert strange_sort_list([-1]) == [-1], "Ninth"
    assert strange_sort_list([-1, -1]) == [-1, -1], "Tenth"
