def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret ur _ value =
	"""
    return len(set(string.lower()))


def count_distinct_characters_alt(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret ur _ value =
	"""
    return len(set(string.lower()))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
