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

    # create a list of lists
    # the inner list has the string and the length of the string
    # the outer list is the original list
    # the outer list is sorted by the length of the string
    # the inner list is sorted by the string
    # the inner list is sorted alphabetically if the lengths are the same
    return sorted(lst, key=lambda x: (len(x), x))


print(sorted_list_sum(["aa", "a", "aaa"]))
print(sorted_list_sum(["ab", "a", "aaa", "cd"]))
