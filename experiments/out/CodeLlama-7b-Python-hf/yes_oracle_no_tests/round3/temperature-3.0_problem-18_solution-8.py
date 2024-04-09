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
    if len(substring) > len(string):
        return 0
    else:
        return string.count(substring)


def how_many_times_optimized(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times_optimized('', 'a')
    0
    >>> how_many_times_optimized('aaa', 'a')
    3
    >>> how_many_times_optimized('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences =
	"""
    if len(substring) > len(string):
        return 0
    else:
        return string.count(substring)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
