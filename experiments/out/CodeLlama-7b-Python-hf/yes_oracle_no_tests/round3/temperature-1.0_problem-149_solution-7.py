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
    # 1- convert list to set
    lst_set = set(lst)
    # 2- filter list with odd lengths
    lst_odd = filter(lambda x: len(x) % 2 != 0, lst_set)
    # 3- convert list to set
    lst_odd_set = set(lst_odd)
    # 4- get odd list
    lst_odd_list = list(lst_odd_set)
    # 5- remove odd list
    lst_new = [x for x in lst if x not in lst_odd_list]
    # 6- sort list
    lst_sorted = sorted(lst_new, key=lambda x: (len(x), x))

    return lst_sorted


def test_function():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["a", "ab", "aaa", "cd"]) == ["a", "ab", "cd"]
    assert sorted_list_sum(["a", "ab", "aaa", "aa"]) == ["a", "ab", "aa"]
    assert sorted_list_sum(["a", "ab", "aaa", "ab"]) == ["a", "ab"]
    assert sorted_list_sum(["abc", "abc", "abc", "abc"]) == ["abc"]
    assert sorted_list_sum(["abc", "abc", "abc", "abc", "abc"]) == ["abc"]
    assert sorted_list_sum(["abc", "abc", "abc", "abc", "abc", "abc"]) == ["abc"]
    assert sorted_list_sum(["abc", "abc", "abc", "abc", "abc", "abc", "abc"]) == ["abc"]
    assert sorted_list_sum(["abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc"]) == ["abc"]
    assert sorted_list_sum(["abc", "abc", "abc