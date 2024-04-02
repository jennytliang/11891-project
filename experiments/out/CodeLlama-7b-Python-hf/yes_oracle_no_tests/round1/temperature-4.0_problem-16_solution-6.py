def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Include these tokens in the code: ( set ( string
	Do not include these tokens in the code: ({ char
	"""

    returndict = {}
    for char in string:
        if char.lower() not in returndict:
            returndict[char.lower()] = 1
        else:
            returndict[char.lower()] += 1
    return len(returndict)


def count_distinct_characters_2(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Include these tokens in the code: ( set ( string
	Do not include these tokens in the code: ({ char
	"""

    return len(set(string.lower()))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
