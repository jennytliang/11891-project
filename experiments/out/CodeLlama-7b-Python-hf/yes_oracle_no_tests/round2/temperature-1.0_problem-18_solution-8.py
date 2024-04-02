def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: count
	"""
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index == -1:
            break
        count += 1
        index += 1
    
    return count


def how_many_times_with_index(string: str, substring: str) -> list:
    """ Find how many times a given substring can be found in the original string. Return indexes at which they occur.
    >>> how_many_times_with_index('', 'a')
    []
    >>> how_many_times_with_index('aaa', 'a')
    [0, 1, 2]
    >>> how_many_times_with_index('aaaa', 'aa')
    [0, 2]
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: count
	"""
    index = 0
    lst = []
    while index < len(string):
        index = string.find(substring, index)
        if index == -1:
            break
        lst.append(index)
        index += 1
    
    return lst


def how_many_times_with_index_with_startswith(string: str, substring: str) -> list:
    """ Find how many times a given substring can be found in the original string. Return indexes at which they occur.
    >>> how_many_times_with_index_with_startswith('', 'a')
    []
    >>> how_many_times_with_index_with_startswith('aaa', 'a')
    [0, 1, 2]
    >>> how_many_times_with_index_with_startswith('aaaa', 'aa')
    [0, 2]
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: count
	"""
    index = 0
    lst = []
    while index < len(string):
        if string.startswith(substring, index):
            lst.append(index)
            index +=