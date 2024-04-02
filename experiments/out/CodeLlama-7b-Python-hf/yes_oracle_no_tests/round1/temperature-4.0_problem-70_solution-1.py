def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list = sorted ( lst )
	'''
    # Your code here
    return sorted(lst)


def strange_sort_string(string):
    '''
    Given string, return string in strange order.
    Strange sorting, is when you start with the letter "a", then "z", then "y", and so on...

    Examples:
    strange_sort_string('hello') == 'elloh'
    strange_sort_string('Hello World!') == 'elloh!dlroW'
    strange_sort_string('123456789') == '123456789'
    strange_sort_string('Lorem ipsum') == 'emsi psumloR'
    strange_sort_string('') == ''
    
	Include these tokens in the code: sorted _ string = sorted ( string )
	'''
    # Your code here
    return ''.join(sorted(string))


def longest_word(lst):
    '''
    Given list of strings, return the longest string.
    If there are multiple strings with the same length, return the one which comes first when you sort alphabetically.
    
    Examples:
    longest_word(['a', 'z', 'apple']) == 'apple'
    longest_word(['a', 'aa', 'apple']) == 'apple'
    longest_word(['a', 'b', 'apple', 'google', 'facebook']) == 'facebook'
    longest_word(['a', 'e', 'i', 'o', 'u', 'y']) == 'u'
    longest_word(['a', 'e', 'i', 'o', 'u', 'y', 'y']) == 'y'
    longest_word(['a', 'a', 'a', 'a', 'a', 'a', 'a']) == 'a'
    longest_word(['a', 'b', 'a']) == 'b'
    longest_word(['a', 'b', 'a', 'c']) == 'c'
    
	Include these tokens in the code: sorted _ lst = sorted ( lst )
	'''
    # Your code here
    return sorted(lst)[-1]


def filter_list(lst):
