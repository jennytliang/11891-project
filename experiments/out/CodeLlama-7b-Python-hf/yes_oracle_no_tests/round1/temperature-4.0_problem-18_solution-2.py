def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences =
	"""
    return string.count(substring)


def start_and_end(string: str, substring: str) -> tuple:
    """ Find the starting and ending indices of the first occurence of a substring in a string.
    >>> start_and_end('', 'a')
    (None, None)
    >>> start_and_end('aaa', 'a')
    (0, 0)
    >>> start_and_end('aaaa', 'aa')
    (0, 1)
    
	Include these tokens in the code: start and end =
	"""
    start = string.find(substring)
    end = start + len(substring)
    return start, end


def find_first_indices(string: str, substring: str) -> tuple:
    """ Find the starting indices of all occurences of a substring in a string.
    >>> find_first_indices('', 'a')
    ()
    >>> find_first_indices('aaa', 'a')
    (0, 1, 2)
    >>> find_first_indices('aaaa', 'aa')
    (0, 2)
    
	Include these tokens in the code: indices =
	"""
    indices = []
    start = 0
    while start < len(string):
        start = string.find(substring, start)
        if start == -1:
            break
        indices.append(start)
        start += 1
    return tuple(indices)


def find_last_indices(string: str, substring: str) -> tuple:
    """ Find the ending indices of all occurences of a substring in a string.
    >>> find_last_indices('', 'a')
    ()
    >>> find_last_indices('aaa', 'a')
    (0, 1, 2)
    >>> find_last_indices('aaaa', 'aa')
    (1, 2)
    
	Include these tokens in the code: indices =
	"""
    indices = []
    start = len(string) - 1
    while start >= 0:
        start