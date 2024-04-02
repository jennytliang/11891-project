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

    # Create a list of the lengths of each word
    lengths = [len(x) for x in lst]

    # Sort the lengths
    sorted_lengths = sorted(lengths)

    # Create a list of the words sorted by length
    sorted_words = [lst[i] for i in sorted_lengths]

    # Create a list of the words sorted by length
    sorted_words = [lst[i] for i in sorted_lengths]

    # Create a list of the odd length words
    odd_length_words = [x for x in sorted_words if len(x) % 2 == 1]

    # Create a list of the even length words
    even_length_words = [x for x in sorted_words if len(x) % 2 == 0]

    # Create a list of the sorted even length words
    sorted_even_length_words = sorted(even_length_words)

    # Create a list of the sorted odd length words
    sorted_odd_length_words = sorted(odd_length_words)

    # Create a list of the sorted odd and even length words
    sorted_words = sorted_odd_length_words + sorted_even_length_words

    return sorted_words


# 1.

# lst = ["aa", "a", "aaa"]
# print(sorted_list_sum(lst))

# 2.

lst = ["ab", "a", "aaa", "cd"]
print(sorted_list_sum(lst))
