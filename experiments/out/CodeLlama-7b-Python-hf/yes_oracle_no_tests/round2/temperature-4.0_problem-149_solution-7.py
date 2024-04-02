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

    # 1. sort the list
    lst = sorted(lst)

    # 2. remove words with odd length
    lst = [i for i in lst if len(i) % 2 == 0]

    # 3. sort the list alphabetically
    lst = sorted(lst)

    return lst


# Tests
def test_sorted_list_sum():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["a", "b", "c"]) == []
    assert sorted_list_sum(["a", "a", "a"]) == ["a"]
    assert sorted_list_sum(["a", "b", "c", "b"]) == ["b", "c"]
    assert sorted_list_sum(["1", "2", "3", "4", "5", "6", "7", "8", "9"]) == []
    assert sorted_list_sum(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]) == ["10"]
    assert sorted_list_sum(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]) == ["11", "10"]
    assert sorted_list_sum(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]) == ["12", "11", "10"]
    assert sorted_list_sum(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]) == ["13", "12", "11", "10"]


if __name__ == '__main__':
    test_sorted_list