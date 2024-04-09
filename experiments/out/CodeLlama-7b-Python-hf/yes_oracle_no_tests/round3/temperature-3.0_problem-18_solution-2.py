def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: counter
	"""
    return string.count(substring)


def how_many_times_no_count(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times_no_count('', 'a')
    0
    >>> how_many_times_no_count('aaa', 'a')
    3
    >>> how_many_times_no_count('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: counter
	"""
    if len(substring) == 0:
        return 0
    if len(string) == 0:
        return 0
    if string == substring:
        return 1
    return how_many_times_no_count(string[1:], substring) + how_many_times_no_count(string[1:], substring)


def how_many_times_no_count_2(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times_no_count_2('', 'a')
    0
    >>> how_many_times_no_count_2('aaa', 'a')
    3
    >>> how_many_times_no_count_2('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: counter
	"""
    if len(substring) == 0:
        return 0
    if len(string) == 0:
        return 0
    if string == substring:
        return 1
    return how_many_times_no_count_2(string[1:], substring) + 1 if string.startswith(substring) else how_many_times_no_count_2(string[1:], substring)


def how_many_times_no_count_3(string: str, substring: str