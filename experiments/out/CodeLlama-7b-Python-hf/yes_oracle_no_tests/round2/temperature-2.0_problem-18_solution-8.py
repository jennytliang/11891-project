def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: ]. starts with
	Do not include these tokens in the code: i + len
	"""

    occurences = 0
    for i in range(len(string)):
        if stri(string[i:i + len(substring)] == substring):
            occurences += 1
    return occurences


def stri(string: str) -> bool:
    """ Check if string is empty.
    >>> stri('')
    True
    >>> stri('a')
    False
    """
    return not bool(string)
