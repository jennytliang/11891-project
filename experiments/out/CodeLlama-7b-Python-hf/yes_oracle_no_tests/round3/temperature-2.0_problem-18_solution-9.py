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


# print(how_many_times('', 'a'))
# print(how_many_times('aaa', 'a'))
# print(how_many_times('aaaa', 'aa'))
