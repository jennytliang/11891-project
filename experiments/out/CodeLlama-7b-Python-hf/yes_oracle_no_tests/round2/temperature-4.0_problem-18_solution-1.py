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
    counter = 0
    for i in range(0, len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            counter += 1
    return counter


if __name__ == "__main__":
    import doctest
    doctest.testmod()
