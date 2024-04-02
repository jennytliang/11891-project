def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    
	Include these tokens in the code: from fun ct ools import c mp _ to _
	"""
    pass


def sum_of_squares(x):
    """Write a function that accepts a list of integers as a parameter and returns the sum of the squares of all the values in the list.
    For example:
        assert sum_of_squares([1, 2, 3]) => 14
        assert sum_of_squares([10, 18, 14]) => 324
        assert sum_of_squares([11, 8, 19]) => 348
    """

    return sum(i**2 for i in x)


if __name__ == '__main__':
    # Do something. 
