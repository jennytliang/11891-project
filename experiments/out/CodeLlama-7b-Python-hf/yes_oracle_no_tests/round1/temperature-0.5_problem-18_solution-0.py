def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code:  occur ences =  0 
	"""

    # Initialize 
    occur_ences = 0

    # Search substring in string
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            occur_ences += 1

    return occur_ences


if __name__ == "__main__":
    import doctest
    doctest.testmod()
