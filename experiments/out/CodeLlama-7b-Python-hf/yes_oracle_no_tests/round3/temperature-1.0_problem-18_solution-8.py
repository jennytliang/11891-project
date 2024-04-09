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
    # pass
    return string.count(substring)

def how_many_times_v2(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Do not count overlaping cases.
    >>> how_many_times_v2('', 'a')
    0
    >>> how_many_times_v2('aaa', 'a')
    1
    >>> how_many_times_v2('aaaa', 'aa')
    2
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: count
	"""
    # pass
    return string.count(substring, 0, len(string))

def how_many_times_v3(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Do not count overlaping cases.
    >>> how_many_times_v3('', 'a')
    0
    >>> how_many_times_v3('aaa', 'a')
    1
    >>> how_many_times_v3('aaaa', 'aa')
    2
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: count
	"""
    # pass
    return string.count(substring, 0, len(string) - len(substring) + 1)