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
    def sum_it(lst):
        return sum(lst)

    def sort_it(lst):
        return lst.sort()

    def odd_it(lst):
        if len(lst) % 2 == 0:
            return lst
        else:
            return sum_it(lst)

    def even_it(lst):
        return lst

    def odd_sum(lst):
        return sum_it(odd_it(lst))

    def even_sum(lst):
        return sum_it(even_it(lst))

    def sort_odd(lst):
        return sort_it(odd_it(lst))

    def sort_even(lst):
        return sort_it(even_it(lst))

    def odd_sum_sort(lst):
        return sort_odd(odd_sum(lst))

    def even_sum_sort(lst):
        return sort_even(even_sum(lst))

    return odd_sum_sort(lst)


sorted_list_sum(["aa", "a", "aaa", "cd"])
