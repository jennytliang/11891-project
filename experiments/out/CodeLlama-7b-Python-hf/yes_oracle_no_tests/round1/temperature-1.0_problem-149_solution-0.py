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

    # Create a new list with only the odd length strings
    new_lst = [x for x in lst if len(x) % 2 == 0]

    # Sort the new list by length
    new_lst.sort(key=len)

    # Return the new list
    return new_lst


def test_function():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["aaa", "ab"]
    assert sorted_list_sum(["a", "abc", "b"]) == ["abc", "a"]
    assert sorted_list_sum(["a", "a", "ab", "abc"]) == ["abc", "a", "ab"]
    assert sorted_list_sum(["a", "a", "ab", "abc", "aaa", "aa"]) == ["aaa", "aa", "abc", "a", "ab"]
    assert sorted_list_sum(["a", "a", "ab", "abc", "aaa", "aa", "ccc", "bbb"]) == ["aaa", "aa", "abc", "a", "ab", "bbb", "ccc"]
    assert sorted_list_sum(["ccc", "bbb", "aaa", "aa", "ab", "abc", "a", "a", "aaa", "aa"]) == ["aaa", "aa", "abc", "a", "ab", "bbb", "ccc"]
    assert sorted_list_sum(["", "abc", "b"]) == ["abc", "b"]
    assert sorted_list_sum(["", "a", "ab", "abc", "aaa", "aa", "ccc", "bbb", ""]) == ["aaa", "aa", "abc", "a", "ab", "bbb", "ccc", ""]
    assert sorted_list_sum(["", "abc", "b", ""]) == ["abc", "b", ""]
    assert sorted_list_sum(["a", "a", "ab", "abc", "", "aaa",