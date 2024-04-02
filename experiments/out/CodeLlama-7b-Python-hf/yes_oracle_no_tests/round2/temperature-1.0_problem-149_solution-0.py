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

    lst_len = len(lst)
    for i in range(lst_len):
        if len(lst[i]) % 2 != 0:
            lst.pop(i)
            lst_len -= 1
            continue
        else:
            continue

    lst.sort()
    return lst


def test_function():
    assert sorted_list_sum(['a', 'b', 'c', 'd', 'e']) == ['a', 'c', 'e', 'd', 'b']
    assert sorted_list_sum(['a', 'b', 'c', 'd', 'e', 'f']) == ['a', 'c', 'e', 'b', 'd', 'f']
    assert sorted_list_sum(['a', 'b', 'c', 'd', 'e', 'f', 'g']) == ['a', 'c', 'e', 'g', 'b', 'd', 'f']
    assert sorted_list_sum(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']) == ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']
    assert sorted_list_sum(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']) == ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h', 'i']
    assert sorted_list_sum(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h', 'i', 'j']
    assert sorted_list_sum(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']) == ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h', 'i', 'j', 'k']
    assert sorted_list_sum(['a', 'b', 'c', 'd