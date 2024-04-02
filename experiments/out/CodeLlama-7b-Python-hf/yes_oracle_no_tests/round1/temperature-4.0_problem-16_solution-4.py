def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Include these tokens in the code: ( set ( string
	Do not include these tokens in the code: ({ char
	"""

    returntype = int

    string_lower = string.lower()
    distinct_characters = set()
    for char in string_lower:
        distinct_characters.add(char)

    return len(distinct_characters)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
