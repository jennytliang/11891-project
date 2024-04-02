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
    from functools import cmp_to_key
    
    lst_len = []
    
    for i in lst:
        lst_len.append(len(i))
    
    lst_len.sort()   # This will sort the list by length
    
    lst_comp = [0] * len(lst_len)   # This is a dummy list for holding
                                    # the sorted list.
    
    for i in range(len(lst_comp)):
        for j in range((len(lst) - 1), -1, -1):
            if len(lst[j]) == lst_len[i]:
                lst_comp[i] = lst[j]
    
    sorted_lst = sorted(lst_comp, key=cmp_to_key(lambda x, y: (
        len(x) > len(y), len(x) < len(y), x < y, x > y)[
                                                     len(x) == len(y)]))
    
    return sorted_lst
    
print(sorted_list_sum(["aa", "bb", "a", "aaa", "b", "c"]))
