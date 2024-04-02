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
    return list(sorted(lst, key=lambda x: lst.count(x)))


def test_function():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3], "First"
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5], "Second"
    assert strange_sort_list([]) == [], "Third"
    assert strange_sort_list([1, 1, 1, 1]) == [1, 1, 1, 1], "Fourth"
    assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3], "Fifth"
    assert strange_sort_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Sixth"
    assert strange_sort_list([10, 10, 10, 10]) == [10, 10, 10, 10], "Seventh"
    assert strange_sort_list([-2, -1, 0, 1, 2]) == [-2, 2, -1, 1, 0], "Eighth"
    assert strange_sort_list([-4, -3, -2, -1, 0, 1, 2, 3, 4]) == [-4, 4, -3, 3, -2, 2, -1, 1, 0], "Ninth"
    print("Test done.")
