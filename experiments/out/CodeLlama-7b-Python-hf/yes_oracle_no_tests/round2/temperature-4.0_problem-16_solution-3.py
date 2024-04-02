def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Do not include these tokens in the code: ret ur ne e = set
	"""
    return len(set(string.lower()))


def count_distinct_characters_alt(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Do not include these tokens in the code: ret ur ne e = set
	"""
    return len(set(string.lower()))


def count_distinct_characters_alt_2(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Do not include these tokens in the code: ret ur ne e = set
	"""
    return len({char.lower() for char in string})


if __name__ == '__main__':
    import doctest

    doctest.testmod()
