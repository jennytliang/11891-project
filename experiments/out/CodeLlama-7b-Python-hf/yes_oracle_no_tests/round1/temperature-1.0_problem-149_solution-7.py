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

    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    # 		  The tests are already written (below).
    # 		  Be sure that you understand the code in the test cases. 
    # 		  Run pytest to see the test cases.
    # 		  You should recognize this solution because:
    #
    #			1. You will use a list comprehension as you did in
    #			   mUltIpLE_strings.
    #			2. You will use an OFFSET-BASED FOR-loop.
    #			3. You will use OFFSET-BASED CLUSTERING.
    #			4. You will use a tuple of two lists (one input, one output)
    #			   as your return value instead of a list.
    # -------------------------------------------------------------------------
    cleaned_strings = [s for s in lst if len(s) % 2 == 0]
    sorted_lengths = sorted(set(len(s) for s in cleaned_strings))

    list_length = len(cleaned_strings)
    answer = []
    for length in sorted_lengths:
        # offset of start of all words of this length
        start = 0
        while start < list_length:
            if len(cleaned_strings[start]) == length:
                answer.append(cleaned_strings[start])
            start += len(cleaned_strings[start]) + 1

    return tuple(answer)
