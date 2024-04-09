def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list
	Do not include these tokens in the code: lst
	'''

    # code goes here
    return sorted(lst, key=lambda x: (x, -x))

# 24
def filter_long_words(lst, length):
    '''
    Given list of strings, return list with strings longer than length.
    Examples:
    filter_long_words(["Career", "ADVISE", "everyday"], 5) == ["Career", "ADVISE"]
    filter_long_words(["cat", "dog", "mouse"], 4) == []
    filter_long_words(["cat", "dog", "mouse"], 6) == ["cat", "dog"]
    filter_long_words([], 6) == []
    '''

    # code goes here
    return [i for i in lst if len(i) > length]

# 25
def filter_vowels(lst):
    '''
    Given list of strings, return list with vowels from each string.
    Examples:
    filter_vowels(["Water", "leaves", "and", "fish"]) == ["ea", "e", "a", ""]
    filter_vowels(["Career", "ADVISE", "everyday"]) == ["ea", "ea", "ea"]
    filter_vowels(["cat", "dog", "mouse"]) == ["at", "og", "ue"]
    filter_vowels([]) == []
    '''

    # code goes here
    return [i.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '') for i in lst]

# 26
def reverse_list_of_lists(lst):
    '''
    Given list of lists, return list of lists with elements reversed.
    Examples:
    reverse_list_of_lists([[1, 2], [3, 4], [5, 6]]) == [[2, 1], [4, 3], [6, 5]]
    reverse_list_of_lists([[100, 200, 300],