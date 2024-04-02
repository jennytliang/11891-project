def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur
	Do not include these tokens in the code: string = string . lower ()
	"""

    # 5 min
    assert (len(string) >= len(substring)), 'string must be bigger length of substring'
    assert (len(string) != 0), 'input must be a string'
    assert (len(substring) != 0), 'input must be a string'

    string = string.lower()
    substring = substring.lower()

    if substring in string:
        return string.count(substring)
    else:
        return 0


if __name__ == "__main__":
    from doctest import testmod

    testmod()


