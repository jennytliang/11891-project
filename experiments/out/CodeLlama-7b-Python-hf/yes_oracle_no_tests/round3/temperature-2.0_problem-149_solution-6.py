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
    # o(n*log(n)) time | o(n) space
    # def sorted_list_sum(lst):
    #     lst.sort(key=lambda x: (len(x), x))
    #     return lst

    # 2nd solution
    # o(n) time | o(n) space
    # def sorted_list_sum(lst):
    #     new_list = []
    #     for i in lst:
    #         if len(i) % 2 == 0:
    #             new_list.append(i)
    #     new_list.sort(key=lambda x: (len(x), x))
    #     return new_list

    # 3rd solution
    # o(n*log(n)) time | o(n) space
    # def sorted_list_sum(lst):
    #     lst.sort(key=lambda x: (len(x), x))
    #     return lst

    # 4th solution
    # o(n) time | o(n) space
    # def sorted_list_sum(lst):
    #     new_lst = []
    #     for i in lst:
    #         if len(i) % 2 == 0:
    #             new_lst.append(i)
    #     new_lst.sort(key=lambda x: (len(x), x))
    #     return new_lst

    # 5th solution
    # o(n) time | o(n) space
    # def sorted_list_sum(lst):
    #     return sorted(lst, key=lambda x: (len(x), x))

    # 6th solution
    # o(n) time | o(n) space
    # def sorted_list_sum(lst):
    #     return sorted(lst, key=lambda x: (-len(x) % 2, x))

    # 7th solution
    # o(n*log(n)) time | o(n) space
    # def sorted_list_sum(lst):
