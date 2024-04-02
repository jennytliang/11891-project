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
    # 1st solution
    # return sorted(lst, key=lambda x: (len(x), x))

    # 2nd solution
    # return sorted(lst, key=lambda x: (len(x), x), reverse=True)

    # 3rd solution
    sorted_list = []
    for element in lst:
        if len(element) % 2 == 0:
            sorted_list.append(element)
    return sorted(sorted_list, key=lambda x: (len(x), x))


assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
