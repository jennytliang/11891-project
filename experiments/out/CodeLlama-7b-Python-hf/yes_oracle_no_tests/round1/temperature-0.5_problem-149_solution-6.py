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
    
	Include these tokens in the code:  from fun ct ools import c mp _
	Do not include these tokens in the code: return sorted ( lst ,
	"""

    def is_even(x):
        return x % 2 == 0

    def list_sum(lst):
        return sum(lst)

    def delete_odd_length_strings(lst):
        return [x for x in lst if is_even(len(x))]

    def list_sort(lst):
        return sorted(lst, key=len)

    return list_sum(delete_odd_length_strings(list_sort(lst)))


print(sorted_list_sum(["a", "aa", "aaa", "ab", "abc", "cd"]))
