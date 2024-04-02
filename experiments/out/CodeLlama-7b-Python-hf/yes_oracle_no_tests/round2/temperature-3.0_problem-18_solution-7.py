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
    if len(substring) > len(string):
        return 0
    if len(substring) == 0:
        return 1
    if len(string) == 0:
        return 0
    if string[0] == substring[0]:
        return how_many_times(string[1:], substring) + how_many_times(string[1:], substring[1:])
    else:
        return how_many_times(string[1:], substring)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
