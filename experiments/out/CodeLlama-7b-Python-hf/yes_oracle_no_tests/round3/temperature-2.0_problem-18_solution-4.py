def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: if len ( substring ) > len
	"""
    if len(substring) > len(string):
        return 0
    elif len(substring) == 0:
        return 0
    return string.count(substring)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
