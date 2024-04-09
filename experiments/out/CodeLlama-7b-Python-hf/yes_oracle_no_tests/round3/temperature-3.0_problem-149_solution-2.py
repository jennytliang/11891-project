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
    # Convert the list to a set to remove duplicates
    lst = set(lst)
    lst = list(lst)
    # Sort the list by length
    lst.sort(key=len)
    # Create a new list to store the filtered list
    lst2 = []
    # Iterate through the list
    for word in lst:
        # Check the length of each word
        if len(word) % 2 == 0:
            # If the length is even, append to the new list
            lst2.append(word)
    # Sort the list alphabetically
    lst2.sort()
    return lst2
