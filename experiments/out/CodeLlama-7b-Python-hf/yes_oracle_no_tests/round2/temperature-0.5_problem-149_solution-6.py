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

    # Create a new list to put the correct strings in
    lst_new = []

    # Loop through the list
    for word in lst:
        # If the length of the word is even
        if len(word) % 2 == 0:
            # Append the word to the new list
            lst_new.append(word)

    # Sort the new list
    lst_new.sort()

    # Return the new list
    return lst_new


# Test the function
lst = ["aa", "a", "aaa"]
print(sorted_list_sum(lst))

lst = ["ab", "a", "aaa", "cd"]
print(sorted_list_sum(lst))
