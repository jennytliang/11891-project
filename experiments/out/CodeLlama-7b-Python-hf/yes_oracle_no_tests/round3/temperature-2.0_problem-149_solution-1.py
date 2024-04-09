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

    # O(n log n)
    # lst.sort(key=lambda x: (len(x), x))

    # O(n)
    # for i in range(len(lst)):
    #     for j in range(i + 1, len(lst)):
    #         if len(lst[i]) != len(lst[j]):
    #             if len(lst[i]) > len(lst[j]):
    #                 lst[i], lst[j] = lst[j], lst[i]
    #             break
    #         elif lst[i] > lst[j]:
    #             lst[i], lst[j] = lst[j], lst[i]

    # O(n)
    lst.sort(key=lambda x: (len(x), x))
    new_lst = []
    for i in range(len(lst)):
        if len(lst[i]) % 2 == 0:
            new_lst.append(lst[i])
    return new_lst


if __name__ == "__main__":
    print(sorted_list_sum(["aa", "a", "aaa"]))
    print(sorted_list_sum(["ab", "a", "aaa", "cd"]))
