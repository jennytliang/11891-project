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
    # create a list of words with odd lengths
    odd_lst = []
    # for each item in list
    for item in lst:
        # if length of item is odd, append to odd list
        if len(item) % 2 != 0:
            odd_lst.append(item)
    # sort the odd list
    odd_lst.sort()
    # create a new list
    new_lst = []
    # for each item in sorted list
    for item in odd_lst:
        # if item is not in new list, append to new list
        if item not in new_lst:
            new_lst.append(item)
    # sort new list by length
    new_lst.sort(key=len)
    # return new list, sorted by length
    return new_lst


# print(sorted_list_sum(["aa", "a", "aaa"]))
# print(sorted_list_sum(["ab", "a", "aaa", "cd"]))
