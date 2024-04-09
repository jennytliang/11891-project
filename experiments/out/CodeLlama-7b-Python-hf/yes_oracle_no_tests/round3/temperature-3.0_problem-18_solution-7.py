def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences =
	Do not include these tokens in the code: if len ( substring ) > len
	"""
    how_many = 0
    for i in range(len(string)):
        if string[i] == substring[0] and string[i:i + len(substring)] == substring:
            how_many += 1
    return how_many


def how_many_times_faster(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    >>> how_many_times_faster('', 'a')
    0
    >>> how_many_times_faster('aaa', 'a')
    3
    >>> how_many_times_faster('aaaa', 'aa')
    3
    """
    how_many = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            how_many += 1
    return how_many


print(how_many_times_faster('abcabc', 'abc'))