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
    
	Include these tokens in the code: from
	Do not include these tokens in the code: import
	"""
    lst = sorted(lst)
    lst_sorted = []
    for i in range(len(lst)):
        if len(lst[i]) % 2 == 0:
            lst_sorted.append(lst[i])
    return sorted(lst_sorted)


def main():
    print(sorted_list_sum(["aa", "a", "aaa"]))
    print(sorted_list_sum(["ab", "a", "aaa", "cd"]))


if __name__ == "__main__":
    main()
