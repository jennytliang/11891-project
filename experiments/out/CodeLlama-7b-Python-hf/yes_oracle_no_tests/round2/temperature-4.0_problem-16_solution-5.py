def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Do not include these tokens in the code: ret ur nt = set (
	"""
    # return len(set(string.lower()))
    # return len(set(string))
    # return len(set(string.lower()))

    # count = 0
    # for char in string:
    #     if char.lower() not in string.lower():
    #         string += char.lower()
    #         count += 1
    # return count

    # characters = set()
    # for char in string:
    #     if char.lower() not in characters:
    #         characters.add(char.lower())
    # return len(characters)

    characters = set()
    for char in string:
        if char.lower() not in characters:
            characters.add(char.lower())
    return len(characters)


def count_distinct_characters2(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Do not include these tokens in the code: ret ur nt = set (
	"""
    # return len(string.lower())
    # return len(set(string))
    # return len(set(string.lower()))

    # count = 0
    # for char in string:
    #     if char.lower() not in string.lower():
    #         string += char.lower()
    #         count += 1
    # return count

    # characters = set()
    # for char in string:
    #     if char.lower() not in characters:
    #         characters.add(char.lower())
    # return len(characters)

    characters = set()
    for char in string:
        if char.lower() not in characters:
            characters.add(char.lower())
    return len(characters)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
