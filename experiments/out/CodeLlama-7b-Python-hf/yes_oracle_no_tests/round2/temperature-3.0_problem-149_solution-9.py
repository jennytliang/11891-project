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
    # create a list of tuples containing the word and its length
    lst_of_tuples = [(i, len(i)) for i in lst]
    # sort the list by the length
    sorted_lst = sorted(lst_of_tuples, key=lambda x: x[1])
    # create a list of tuples containing the word and its alphabetical order
    sorted_lst_of_tuples = sorted(sorted_lst, key=lambda x: x[0])
    # create a list of tuples containing the word and its alphabetical order
    sorted_lst_of_tuples = sorted(sorted_lst, key=lambda x: x[0])
    # create a list of tuples containing the word and its alphabetical order
    sorted_lst_of_tuples = sorted(sorted_lst, key=lambda x: x[0])
    # create a list of tuples containing the word and its alphabetical order
    sorted_lst_of_tuples = sorted(sorted_lst, key=lambda x: x[0])
    # create a list of tuples containing the word and its alphabetical order
    sorted_lst_of_tuples = sorted(sorted_lst, key=lambda x: x[0])
    # create a list of tuples containing the word and its alphabetical order
    sorted_lst_of_tuples = sorted(sorted_lst, key=lambda x: x[0])
    # create a list of tuples containing the word and its alphabetical order
    sorted_lst_of_tuples = sorted(sorted_lst, key=lambda x: x[0])
    # create a list of tuples containing the word and its alphabetical order
    sorted_lst_of_tuples = sorted(sorted_lst, key=lambda x: x[0])
    # create a list of tuples containing the word and its alphabetical order
    sorted_lst_of_tuples = sorted(sorted_lst, key=lambda x: x[0])
    # create a list of tuples containing the word and its alphabetical order
    sorted_lst_of_tuples = sorted(sorted_lst, key=lambda x: x[0])
   