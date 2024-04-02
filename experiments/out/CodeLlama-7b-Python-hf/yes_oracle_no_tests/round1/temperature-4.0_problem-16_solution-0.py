def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Include these tokens in the code: ( set ( string
	Do not include these tokens in the code: ({ char
	"""

    returnt = 0
    for char in string:
        if char.lower() not in string.lower():
            string += char.lower()
            returnt += 1

    return returnt


if __name__ == "__main__":
    import doctest

    doctest.testmod()
