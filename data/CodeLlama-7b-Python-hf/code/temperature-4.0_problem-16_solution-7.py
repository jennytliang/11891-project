def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return len({char.casefold(): 0 for char in string})


# Pybites solution
# https://github.com/pybites/challenges/issues/94
# def count_distinct_characters
