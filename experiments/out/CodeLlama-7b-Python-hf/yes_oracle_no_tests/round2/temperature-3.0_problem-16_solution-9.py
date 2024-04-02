def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Include these tokens in the code: string
	Do not include these tokens in the code: s
	"""


    return leet_567_count_distinct_characters(string)

def leet_567_count_distinct_characters(string: str) -> int:
    """
    >>> leet_567_count_distinct_characters('xyzXYZ')
    3
    >>> leet_567_count_distinct_characters('Jerry')
    4
    """
    # set is a data type that contains no duplicates
    # it is like a list but it only contains unique elements
    # https://www.w3schools.com/python/python_sets.asp
    # https://docs.python.org/3/tutorial/datastructures.html#sets
    return len(set(string.lower()))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
