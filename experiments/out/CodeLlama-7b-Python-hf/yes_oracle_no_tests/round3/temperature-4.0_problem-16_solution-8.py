def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Do not include these tokens in the code: # ret = set ()
	"""
    # pass
    # unique_char = set()
    # for char in string:
    #     unique_char.add(char.lower())
    # return len(unique_char)
    unique_char = set()
    for char in string:
        if char.lower() not in unique_char:
            unique_char.add(char.lower())
    return len(unique_char)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
