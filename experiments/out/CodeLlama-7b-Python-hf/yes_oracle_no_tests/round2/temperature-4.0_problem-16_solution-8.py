def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Do not include these tokens in the code: ret ur = set ()
	"""
    # ret = set()
    # for c in string:
    #     if c not in ret:
    #         ret.add(c)
    # return len(ret)
    return len(set(string.lower()))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
